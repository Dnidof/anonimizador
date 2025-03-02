from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from io import BytesIO
import os
import uuid
import fitz
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import math

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the Hugging Face model
model_name = "Dnidof/NER-MEDDOCAN"
print("Loading...", model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)
classifier = pipeline("token-classification", model=model_name, tokenizer=model_name, aggregation_strategy="simple")

def use_model(text):
	tokens = tokenizer.tokenize(text)
	splits = math.ceil(len(tokens) / tokenizer.model_max_length) + 1
	print(f"Hay {len(tokens)} tokens: hacemos {splits} trozos de texto")

	processed_text = ""
	size = int(len(text)/splits)

	for split in range(splits - 1):
		new_text = text[split*size:(split+1)*size]
		processed_text += process_split(new_text)

	new_text = text[(splits-1)*size:]
	processed_text += process_split(new_text)

	return processed_text

def use_model_ents(text):
	tokens = tokenizer.tokenize(text)
	splits = math.ceil(len(tokens) / tokenizer.model_max_length) + 1
	print(f"Hay {len(tokens)} tokens: hacemos {splits} trozos de texto", flush=True)

	ents = []
	size = int(len(text)/splits)

	for split in range(splits):
		new_text = text[split*size:(split+1)*size]
		new_ents = classifier(new_text)
		print("------")
		print(new_text)
		print(new_ents, flush=True)
		ents += new_ents
	return ents

def process_split(t):
	ents = classifier(t)
	print(ents, flush=True)
	new_text = t
	for ent in ents:
		start = int(ent["start"])
		end = int(ent["end"])
		new_text = new_text[:start] + "#" * (end - start) + new_text[end:]
	return new_text

def modify_pdf(file_path, ents):
	doc = fitz.open(file_path)
	pii_words = {ent["word"].strip().strip('.') for ent in ents}
	print(pii_words, flush=True)
	for page in doc:
		for pii_word in pii_words:
			hits = page.search_for(pii_word)  # list of rectangles where to replace

			for rect in hits:
				page.add_redact_annot(rect, fill=(0,0,0))  # more parameters

		page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
	return doc.write()


@app.route('/submit', methods=['POST'])
def submit():
	if 'file' in request.files:
		file = request.files['file']
		file_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}_{file.filename}")
		file.save(file_path)

		# Determine file type and read content accordingly
		if file.filename.endswith('.txt'):
			file_content = read_text(file_path)
			result = use_model(file_content)
			bytes = str(result).encode('utf-8')
			buffer = BytesIO()
			buffer.write(bytes)
			buffer.seek(0)
			response = send_file(buffer, mimetype='application/text', download_name=f"anm_{file.filename}", as_attachment=True)
		elif file.filename.endswith('.pdf'):
			file_content = read_pdf(file_path)
			ents = use_model_ents(file_content)
			bytes = modify_pdf(file_path, ents)
			buffer = BytesIO()
			buffer.write(bytes)
			buffer.seek(0)
			response = send_file(buffer, mimetype='application/pdf', download_name=f"anm_{file.filename}", as_attachment=True)
		else:
			response = "Unsupported file format.", 400
		os.remove(file_path)
		return response

	elif 'text' in request.form:
		input_text = request.form['text']

		# Use the Hugging Face model to process the input text
		result = use_model(input_text)

		response_text = f"{result}"
		return response_text

	else:
		return "No file or text provided.", 400


def read_text(file_path):
	with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
		return f.read()

def read_pdf(file_path):
	doc = fitz.open(file_path)
	text = ""
	for page in doc:
		text += page.get_text("text")
	print(text, flush=True)
	return text

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=4444, debug=True)



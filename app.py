from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import uuid
import PyPDF2  # or `import pdfplumber` if you prefer pdfplumber for PDF parsing
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import math

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the Hugging Face model
model_name = "Dnidof/NER-MEDDOCAN"
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


def process_split(t):
	ents = classifier(t)
	print(ents)
	new_text = t
	for ent in ents:
		start = int(ent["start"])
		end = int(ent["end"])
		new_text = new_text[:start] + "#" * (end - start) + new_text[end:]
	return new_text


@app.route('/submit', methods=['POST'])
def submit():
	if 'file' in request.files:
		file = request.files['file']
		file_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}_{file.filename}")
		file.save(file_path)

		# Determine file type and read content accordingly
		if file.filename.endswith('.txt'):
			file_content = read_text(file_path)
		elif file.filename.endswith('.pdf'):
			file_content = read_pdf(file_path)
		else:
			os.remove(file_path)
			return "Unsupported file format.", 400

		result = use_model(file_content)
		response_text = f"Processed content of the uploaded document:\n\n{result}"
		os.remove(file_path)
		return response_text

	elif 'text' in request.form:
		input_text = request.form['text']

		# Use the Hugging Face model to process the input text
		result = use_model(input_text)

		response_text = f"Processed content of the submitted text:\n\n{result}"
		return response_text

	else:
		return "No file or text provided.", 400


def read_text(file_path):
	with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
		return f.read()

def read_pdf(file_path):
	with open(file_path, 'rb') as f:
		pdf_reader = PyPDF2.PdfReader(f)
		text = ''
		for page in pdf_reader.pages:
			text += page.extract_text()
		return text


if __name__ == '__main__':
	app.run(port=4444)

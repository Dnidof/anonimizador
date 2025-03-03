from io import BytesIO
import glob
import fitz
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import math

# Load the Hugging Face model
model_name = "Dnidof/NER-MEDDOCAN"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)
classifier = pipeline("token-classification", model=model_name, tokenizer=model_name, aggregation_strategy="simple")

def parse_txt(text):
	tokens = tokenizer.tokenize(text)
	splits = math.ceil(len(tokens) / tokenizer.model_max_length) + 1

	processed_text = ""
	size = int(len(text)/splits)

	for split in range(splits - 1):
		new_text = text[split*size:(split+1)*size]
		processed_text += process_split(new_text)

	new_text = text[(splits-1)*size:]
	processed_text += process_split(new_text)

	return processed_text

def parse_pdf(text):
	tokens = tokenizer.tokenize(text)
	splits = math.ceil(len(tokens) / tokenizer.model_max_length) + 1

	ents = []
	size = int(len(text)/splits)

	for split in range(splits):
		new_text = text[split*size:(split+1)*size]
		new_ents = classifier(new_text)
		for ent in new_ents:
			ent["word"] = ent["word"].strip().strip('.')
			if len(ent["word"]) == 1:
				start = ent["start"] - 1
				end = ent["end"] + 2
				ent["word"] = new_text[start:end]
		ents += new_ents
	return ents

def process_split(t):
	ents = classifier(t)
	new_text = t
	for ent in ents:
		start = int(ent["start"])
		end = int(ent["end"])
		new_text = new_text[:start] + "#" * (end - start) + new_text[end:]
	return new_text

def modify_pdf(file_path, ents):
	doc = fitz.open(file_path)
	pii_words = {ent["word"] for ent in ents}
	for page in doc:
		for pii_word in pii_words:
			hits = page.search_for(pii_word)  # list of rectangles where to replace

			for rect in hits:
				page.add_redact_annot(rect, fill=(0,0,0))  # more parameters

		page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
	return doc.write()

def anonymize_folder(input_folder = "./input/", output_folder = None, pattern = "*"):
	if output_folder is None:
		output_folder = input_folder
	files = glob.glob(input_folder + pattern)
	directory_len = len(input_folder)
	for file_path in files:
		try:
			bytes = None

			# Determine file type and parse content accordingly
			if file_path.endswith('.pdf'):
				file_content = read_pdf(file_path)
				ents = parse_pdf(file_content)
				bytes = modify_pdf(file_path, ents)
			elif file_path.endswith('.txt'):
				file_content = read_txt(file_path)
				result = parse_txt(file_content)
				bytes = str(result).encode('utf-8')
			else:
				print(f"{file_path} must be txt or pdf", flush=True)
				continue
			buffer = BytesIO()
			buffer.write(bytes)
			buffer.seek(0)
			new_file_path = output_folder + "ANM_" + file_path[directory_len:]
			with open(new_file_path, "wb") as f:
				f.write(buffer.getbuffer())
		except Exception:
			pass

def read_pdf(file_path):
	doc = fitz.open(file_path)
	text = ""
	for page in doc:
		text += page.get_text("text")
	return text

def read_txt(file_path):
	with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
		return f.read()

if __name__ == '__main__':
	anonymize_folder("./input/", "./output/")



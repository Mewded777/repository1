from flask import Flask, render_template, request
from difflib import SequenceMatcher
from PyPDF2 import PdfReader
from docx import Document

app = Flask(__name__)

def extract_text(file):
    filename = file.filename.lower()

    # if the user's input is a text file
    if filename.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")
    
    # if the user's input is a PDF file
    elif filename.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    # if the user's input is a word file
    elif filename.endswith(".docx"):
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    
    # anything else then nothing is returned
    else:
        return None

def check_plagiarism(file1, file2):
    # Returns a ratio of similarity between 0 and 1
    matcher = SequenceMatcher(None, file1, file2)
    return matcher.ratio() * 100

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    f1 = request.files.get("file1")
    f2 = request.files.get("file2")

    if not f1 or not f2:
        return "Please upload both files.", 400

    content1 = extract_text(f1)
    content2 = extract_text(f2)

    if content1 is None or content2 is None:
        return "Invalid file format. Please upload TXT, PDF, or DOCX files.", 400

    score = round(check_plagiarism(content1, content2), 2)
    # To make sure of a professional way of writing percentages
    similarity_score = f"{score:g}"
    
    # Extra comments based on the value of the similarity score
    if float(similarity_score) <= 5:
        detection = "Your file is not plagiarized"
    if 5 < float(similarity_score) < 20:
        detection = "Your file is very mildly plagiarized"
    if 20 < float(similarity_score) < 50:
        detection = "Your file is mildly plagiarized"
    if 50 < float(similarity_score) < 85:
        detection = "Your file is mostly plagiarized"
    if 85 < float(similarity_score) < 95:
        detection = "Your file is almost completely plagiarized"
    if float(similarity_score) > 95:
        detection = "Your file is completely plagiarized"

    return render_template("check.html", similarity_score=similarity_score , detection = detection)

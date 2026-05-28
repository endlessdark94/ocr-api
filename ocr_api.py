from flask import Flask, request, jsonify
import pytesseract
from pdf2image import convert_from_path

app = Flask(__name__)

@app.route('/ocr-pdf', methods=['POST'])
def ocr_pdf():
    file = request.files['file']
    pdf_path = "/tmp/input.pdf"
    file.save(pdf_path)

    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img, lang="eng") + "\n"

    return jsonify({"extracted_text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

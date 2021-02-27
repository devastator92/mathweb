from flask import Flask
from flask_tex import render_to_pdf

app = Flask(__name__)

@app.route("/")
def return_pdf_response():
    return render_to_pdf("tex_template.tex", foo="Hello World")

    
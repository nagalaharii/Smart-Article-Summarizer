from flask import Flask, render_template, request

from utils.summarizer import generate_summary
from utils.url_reader import extract_text_from_url

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    summary = ""

    if request.method == "POST":

        input_type = request.form["input_type"]

        if input_type == "text":

            text = request.form["text_input"]

            summary = generate_summary(text)

        elif input_type == "url":

            url = request.form["url_input"]

            article_text = extract_text_from_url(url)

            summary = generate_summary(article_text)

    return render_template(
        "index.html",
        summary=summary
    )


if __name__ == "__main__":
    app.run(debug=True)
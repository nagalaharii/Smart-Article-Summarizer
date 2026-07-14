import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")

    article_text = ""

    for paragraph in paragraphs:
        article_text += paragraph.get_text() + "\n"

    return article_text


if __name__ == "__main__":

    text = extract_text_from_url(
        "https://en.wikipedia.org/wiki/Natural_language_processing"
    )

    print(text)
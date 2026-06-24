import os
from pypdf import PdfReader


def load_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        text += page.extract_text() + "\n"

    return text


def load_txt(file_path):

    with open(file_path, "r", encoding="utf-8") as file:

        return file.read()


def load_json(file_path):

    with open(file_path, "r", encoding="utf-8") as file:

        return file.read()


def load_knowledge(folder):

    documents = []

    for filename in os.listdir(folder):

        path = os.path.join(folder, filename)

        if filename.endswith(".pdf"):

            documents.append(load_pdf(path))

        elif filename.endswith(".txt"):

            documents.append(load_txt(path))

        elif filename.endswith(".json"):

            documents.append(load_json(path))

    return documents
import os
from .type import Texts, Text

def get_texts() -> Texts:
    texts = []
    for filename in os.listdir('data/texts'):
        with open('data/texts/' + filename, 'r') as file:
            texts.append(Text(filename, file.read()))
    return Texts(texts=texts)

def update_texts(texts: Texts):
    for text in texts.texts:
        with open('data/texts/' + text.filename, 'w') as file:
            file.write(text.content)
    return texts
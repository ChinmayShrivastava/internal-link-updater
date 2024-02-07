from ILUpdate import ILUpdate
from utilities import get_texts, update_texts
from data.LINKS import LINKS

def main():
    texts = get_texts()
    ilu = ILUpdate(links=LINKS, texts=texts)
    updated_texts = ilu()
    update_texts(updated_texts)

if __name__ == '__main__':
    main()
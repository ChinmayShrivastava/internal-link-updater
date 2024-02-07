from pydantic import BaseModel

class LinkToUpdate(BaseModel):
    old_link: str
    new_link: str

class LinksToUpdate(BaseModel):
    links: list[LinkToUpdate]

class Text(BaseModel):
    filename: str
    content: str

class Texts(BaseModel):
    texts: list[Text]
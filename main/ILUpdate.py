from type import LinksToUpdate, Texts, Text

class ILUpdate:

    """Update internal links in markdowns."""

    def __init__(
            self, 
            links: LinksToUpdate,
            texts: Texts
        ):
        self.links = links
        self.texts = texts

    def __repr__(self):
        return f'ILUpdate(links={self.links}, texts={self.texts})'
    
    # for a given text (of markdown format) find the internal links following the regex pattern matching the old link
    # and replace them with the new link
    def _update_links(self, text: str) -> str:
        for link in self.links.links:
            text = text.replace(link.old_link, link.new_link)
        return text
    
    def _update_texts(self, texts: Texts) -> Texts:
        return Texts(texts=[Text(filename=text.filename, content=self._update_links(text.content)) for text in texts.texts])
    
    def update(self) -> Texts:
        return self._update_texts(self.texts)
    
    def __call__(self) -> Texts:
        return self.update()
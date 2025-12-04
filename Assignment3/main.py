class Book:
    def __init__(self, title, author, isbn, issued=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.issued = issued

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "issued": self.issued,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d.get("title"), d.get("author"), d.get("isbn"), d.get("issued", False))

    def issue(self):
        if self.issued:
            return False
        self.issued = True
        return True

    def return_book(self):
        if not self.issued:
            return False
        self.issued = False
        return True

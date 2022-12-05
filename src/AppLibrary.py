import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "https://green-water-3233.fly.dev/"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    
    def create_book(self, identifier, author, editor, title, publisher, year):
        data = {
            "identifier": identifier,
            "author": author,
            "editor": editor,
            "title": title,
            "publisher": publisher,
            "year": year

        }

        requests.post(f"{self._base_url}", data=data)
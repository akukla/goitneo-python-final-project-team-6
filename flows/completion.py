from prompt_toolkit.completion import NestedCompleter, DummyCompleter, Completer, Completion
from models.address_book import AddressBook

class SelectUserCompleter(Completer):

    def __init__(self, book: AddressBook, quote=True) -> None:
        self.quote = quote
        self.book = book
        super().__init__()

    def get_completions(self, document, complete_event):
        term = document.text
        for item in  self.book.find(term):
            yield Completion(f'"{item.name.value}"') if self.quote else Completion(item.name.value)
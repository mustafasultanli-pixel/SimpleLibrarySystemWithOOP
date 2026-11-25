from dataclasses import dataclass, field


class Book:
    book_id: str
    title: str
    author: str
    is_borrowed: bool = False
    borrowed_by: str | None = None


@dataclass
class Member:
    member_id: str
    name: str



class Library:
    def __init__(self, name: str) = None:
        self.name = name
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    def add_book(self, book: Book) -> None:
        if book.book_id in self.books:

    def register_member(self, member: Member) -> None:
        if member.member_id in self.members:
            raise ValueError(f"Member ID '{member.member_id}' already exists.")
        self.members[member.member_id] = member

    def borrow_book(self, member_id: str, book_id: str) -> str:
        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if not member:
            return "Member not found."
        if not book:
            return "Book not found."
        if book.is_borrowed:
            return f"'{book.title}' is already borrowed by {book.borrowed_by}."

        book.is_borrowed = True
        book.borrowed_by = member.member_id
        member.borrowed_book_ids.append(book.book_id)
        return f"'{book.title}' borrowed by {member.name}."

    def return_book(self, member_id: str, book_id: str) -> str:
        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if not member or not book:
            return "Invalid member ID or book ID."
        if book.book_id not in member.borrowed_book_ids:
            return f"{member.name} did not borrow '{book.title}'."

        book.is_borrowed = False
        book.borrowed_by = None
        member.borrowed_book_ids.remove(book.book_id)
        return f"'{book.title}' returned by {member.name}."

    def list_books(self) -> list[Book]:
        return list(self.books.values())



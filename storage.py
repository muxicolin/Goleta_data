"""JSON-backed storage for book records."""

import json
from pathlib import Path
from typing import Any


class BookStorage:
    """Read and write books in a JSON file next to this module."""

    def __init__(self, file_path: str | Path | None = None) -> None:
        self.file_path = Path(file_path) if file_path else Path(__file__).with_name("books.json")

    def _read(self) -> list[dict[str, Any]]:
        if not self.file_path.exists():
            return []
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as exc:
            raise ValueError(f"数据文件格式错误：{self.file_path}") from exc
        if not isinstance(data, list) or any(not isinstance(item, dict) for item in data):
            raise ValueError(f"数据文件内容格式错误：{self.file_path}")
        # Records created before loan tracking was added default to available.
        for book in data:
            book.setdefault("borrowed", False)
        return data

    def _write(self, books: list[dict[str, Any]]) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=2)

    def add_book(self, title: str, author: str) -> dict[str, str]:
        book = {"title": title.strip(), "author": author.strip(), "borrowed": False}
        if not book["title"]:
            raise ValueError("书名不能为空。")
        if not book["author"]:
            raise ValueError("作者不能为空。")
        books = self._read()
        books.append(book)
        self._write(books)
        return book

    def get_all_books(self) -> list[dict[str, Any]]:
        return self._read()

    def search_by_title(self, query: str) -> list[dict[str, Any]]:
        keyword = query.strip().casefold()
        if not keyword:
            return []
        return [book for book in self._read() if keyword in str(book.get("title", "")).casefold()]

    def filter_by_author(self, query: str) -> list[dict[str, Any]]:
        """Find books whose author contains the given keyword."""
        keyword = query.strip().casefold()
        if not keyword:
            return []
        return [book for book in self._read() if keyword in str(book.get("author", "")).casefold()]

    def delete_book(self, index: int) -> dict[str, Any] | None:
        """Delete the book at a one-based position in the current list."""
        books = self._read()
        if index < 1 or index > len(books):
            return None
        removed = books.pop(index - 1)
        self._write(books)
        return removed

    def set_borrowed(self, index: int, borrowed: bool) -> dict[str, Any] | None:
        """Set the loan status of the book at a one-based list position."""
        books = self._read()
        if index < 1 or index > len(books):
            return None
        books[index - 1]["borrowed"] = borrowed
        self._write(books)
        return books[index - 1]

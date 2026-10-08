"""Small input and display helpers for the command-line application."""

from typing import Any


def prompt_non_empty(prompt: str) -> str:
    """Prompt until the user enters a non-blank value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("此项不能为空，请重新输入。")


def print_books(books: list[dict[str, Any]]) -> None:
    """Print book records in a readable format."""
    if not books:
        print("没有找到图书。")
        return
    for index, book in enumerate(books, start=1):
        print(f"{index}. 《{book.get('title', '未知书名')}》 — {book.get('author', '未知作者')}")

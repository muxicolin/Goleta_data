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
        status = "已借出" if book.get("borrowed", False) else "在馆"
        print(f"{index}. 《{book.get('title', '未知书名')}》 — {book.get('author', '未知作者')} [{status}]")


def prompt_book_index(prompt: str, book_count: int) -> int | None:
    """Read a one-based book number; return None when input is invalid."""
    if book_count == 0:
        print("当前没有图书可操作。")
        return None
    value = input(prompt).strip()
    try:
        index = int(value)
    except ValueError:
        print("请输入列表中的数字编号。")
        return None
    if not 1 <= index <= book_count:
        print("编号超出范围。")
        return None
    return index

"""Command-line interface for the local book manager."""

from storage import BookStorage
from utils import prompt_non_empty, print_books


def main() -> None:
    storage = BookStorage()
    print("=== 本地图书管理系统 ===")
    while True:
        print("\n1. 添加图书\n2. 查看全部图书\n3. 按书名搜索\n0. 退出")
        choice = input("请选择操作：").strip()

        if choice == "1":
            title = prompt_non_empty("书名：")
            author = prompt_non_empty("作者：")
            storage.add_book(title, author)
            print(f"已添加《{title}》。")
        elif choice == "2":
            print_books(storage.get_all_books())
        elif choice == "3":
            query = prompt_non_empty("请输入书名关键词：")
            print_books(storage.search_by_title(query))
        elif choice == "0":
            print("已退出。")
            break
        else:
            print("无效选项，请输入 1、2、3 或 0。")


if __name__ == "__main__":
    main()

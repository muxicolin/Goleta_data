"""Command-line interface for the local book manager."""

from storage import BookStorage
from utils import prompt_book_index, prompt_non_empty, print_books


def main() -> None:
    storage = BookStorage()
    print("=== 本地图书管理系统 ===")
    while True:
        print("\n1. 添加图书\n2. 查看全部图书\n3. 按书名搜索\n4. 删除图书\n5. 按作者筛选\n6. 借书\n7. 还书\n0. 退出")
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
        elif choice == "4":
            books = storage.get_all_books()
            print_books(books)
            index = prompt_book_index("请输入要删除的图书编号：", len(books))
            if index is not None:
                removed = storage.delete_book(index)
                print(f"已删除《{removed['title']}》。" if removed else "未找到该图书。")
        elif choice == "5":
            query = prompt_non_empty("请输入作者姓名或关键词：")
            print_books(storage.filter_by_author(query))
        elif choice in ("6", "7"):
            books = storage.get_all_books()
            print_books(books)
            index = prompt_book_index("请输入图书编号：", len(books))
            if index is not None:
                borrowed = choice == "6"
                book = storage.set_borrowed(index, borrowed)
                if book:
                    action = "已借出" if borrowed else "已归还"
                    print(f"《{book['title']}》{action}。")
        elif choice == "0":
            print("已退出。")
            break
        else:
            print("无效选项，请输入 0 至 7 之间的菜单编号。")


if __name__ == "__main__":
    main()

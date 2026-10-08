# 本地图书管理系统

一个使用 Python 标准库构建的简易命令行图书管理项目。图书信息以 JSON 格式保存在本地，程序重启后仍可读取。

## 环境与依赖

- Python 3.10 或更高版本
- 无第三方依赖（仅使用 Python 标准库）

## 运行

在终端进入 `book_manager` 目录，执行：

```bash
python main.py
```

Windows 上也可以使用 `py main.py`。

## 功能

- 添加图书：录入书名和作者，不能为空。
- 查看全部图书：显示已保存的所有记录。
- 按书名搜索：输入关键词，按不区分大小写的部分匹配查找。
- JSON 持久化：数据保存在项目目录下的 `books.json`；首次添加图书时自动创建。

## 文件结构

```text
book_manager/
├── main.py       # 命令行主程序
├── storage.py    # JSON 读写、添加和搜索
├── utils.py      # 输入校验和图书列表显示
├── books.json    # 运行后自动生成的数据文件
└── README.md     # 项目说明
```

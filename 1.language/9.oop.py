## 可重载运算符：自定义类可以通过实现 __iadd__、__isub__ 等方法来支持复合赋值操作。
## 以实现 `__contains__` 来定义成员测试的行为

class Book:
    def __init__(self, isbn, title, author):
        self._isbn = isbn
        self.title = title
        self.author = author
        self._borrowed = False

    @property
    def isbn(self):
        return self._isbn

    @property
    def borrowed(self):
        return self._borrowed

    def borrow(self):
        if self._borrowed:
            raise ValueError(f"书籍《{self.title}》已被借出")
        self._borrowed = True

    def return_book(self):
        if not self._borrowed:
            raise ValueError(f"书籍《{self.title}》未被借出")
        self._borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self._isbn}', '{self.title}', '{self.author}')"

class Library:
    def __init__(self, name):
        self.name = name
        self._books = {}   # isbn -> Book

    def add_book(self, book):
        if book.isbn in self._books:
            raise ValueError(f"书籍 ISBN {book.isbn} 已存在")
        self._books[book.isbn] = book

    def get_book(self, isbn):
        book = self._books.get(isbn)
        if not book:
            raise KeyError(f"未找到 ISBN {isbn}")
        return book

    def list_available_books(self):
        return [book for book in self._books.values() if not book.borrowed]

    def __len__(self):
        return len(self._books)

# 使用示例
lib = Library("市图书馆")
book1 = Book("978-7-111-00001", "Python编程", "Guido")
book2 = Book("978-7-111-00002", "设计模式", "GoF")
lib.add_book(book1)
lib.add_book(book2)

book1.borrow()
print([str(b) for b in lib.list_available_books()])  # ['设计模式 by GoF']
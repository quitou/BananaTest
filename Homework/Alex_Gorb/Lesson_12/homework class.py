"""Библиотека
Первый класс
Создайте класс book с атрибутами:

материал страниц
наличие текста
название книги
автор
кол-во страниц
ISBN

флаг зарезервирована ли книга или нет (True/False).
Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
"""
class Book:
    material = 'paper'
    isText = True

    def __init__(self, name, author, count_paper, ISBN, reserv):
        self.name = name
        self.author = author
        self.count_paper = count_paper
        self.ISBN = ISBN
        self.reserv = reserv

"""Создайте несколько (штук 5) экземпляров разных книг."""

book1 = Book('Monte cristo', 'Duma',900, 1, True)
book2 = Book('Ono', 'Stiven King', 1234, 2, False)
book3 = Book('Lixo', 'Kuprin', 50, 3, False)
book4 = Book('Tripalo', 'Tareverdiev', 237, 4, True)
book5 = Book('Bokvary', 'Lupachov', 30, 5, True)


"""
После создания пометьте одну книгу как зарезервированную.
"""
book3.reserv = True

"""
Распечатайте детали о каждой книге в таком виде:
Если книга зарезервирована:
Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
"""
"""
если не зарезервирована:
Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага
"""
book_list = [book1, book2, book3, book4, book5]
for book in book_list:
    if book.reserv:
        print('Название:', book.name,
              'Автор:', book.author,
              'страниц:', book.count_paper,
              'материал:', book.material,
              'зарезервирована')
    else:
        print('Название:', book.name,
              'Автор:', book.author,
              'страниц:', book.count_paper,
              'материал:', book.material,)



"""
Второй класс
Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
предмет (типа математика, история, география),
класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
наличие заданий (bool)
"""
class SchoolBook(Book):

    def __init__(self, name, author, count_paper, ISBN, reserv, subject, school_class):
        super().__init__(name, author, count_paper, ISBN, reserv)
        self.subject = subject
        self.scholl_class = school_class


"""
Создайте несколько экземпляров учебников.
После создания пометьте один учебник как зарезервированный.
"""
book6 = SchoolBook('Geography in world',
                   'Tatyanova',
                   200,
                   6, True, 'Geography', '6a')

book7 = SchoolBook('Math for biginier',
                   'Tulpatov',
                   367,
                   7, False, 'Math', '10b')

"""
Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
если не зарезервирован:
Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9"""
shcool_book_list = [book6, book7]

for book in shcool_book_list:
    if book.reserv:
        print('Название:', book.name,
              'Автор:', book.author,
              'страниц:', book.count_paper,
              'материал:', book.material,
              'класс:', book.scholl_class,
              'зарезервирована')
    else:
        print('Название:', book.name,
              'Автор:', book.author,
              'страниц:', book.count_paper,
              'материал:', book.material,
              'класс:', book.scholl_class,)
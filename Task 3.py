# Створіть клас Book з атрибутами title (назва книги), author (автор) та genre (жанр).
# Додайте метод display_info,
# який виведе інформацію про книгу у вигляді
# "Назва: {title}, Автор: {author}, Жанр: {genre}".

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

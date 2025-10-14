# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44  # Oбъем дискеты (Мб).
num_of_pages = 100  # Количество страниц в книге.
lines_page = 50  # Число строк на странице.
char_line = 25  # Количество символов в строке.
code_size = 4  # Одному символу нужно 4 байта.

# Объем заниамаемый одной книгой в байтах.
book_size = num_of_pages * lines_page * char_line * code_size
# Объем книги в Мбайтах.
one_mb = 1024 ** 2  # 1Мб = 1024 ** 2 (байта).
book_size_mb = book_size / one_mb

# Количество книг, помещающихся на дискету.
number_books = int(disk_size // book_size_mb)
print("Количество книг, помещающихся на дискету:", number_books)

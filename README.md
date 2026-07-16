# BooksCollector — юнит-тесты

Проект содержит класс `BooksCollector` для работы с коллекцией книг и набор pytest-тестов.

## Запуск тестов

```bash
pytest -v tests.py
```

## Реализованные тесты

| Тест | Метод(ы) | Что проверяет |
|------|----------|---------------|
| `test_add_new_book_add_one_book` | `add_new_book` | Книга добавляется в словарь без жанра |
| `test_add_new_book_does_not_add_invalid_name` | `add_new_book` | Пустое название и название длиннее 40 символов не добавляются (параметризация) |
| `test_add_new_book_does_not_add_duplicate` | `add_new_book` | Одну и ту же книгу нельзя добавить повторно |
| `test_set_book_genre` | `set_book_genre` | Жанр успешно устанавливается для существующей книги |
| `test_set_book_genre_does_not_set_for_unknown_book` | `set_book_genre` | Жанр не устанавливается для несуществующей книги |
| `test_set_book_genre_does_not_set_invalid_genre` | `set_book_genre` | Жанр не устанавливается, если он не входит в список допустимых (параметризация) |
| `test_get_book_genre` | `get_book_genre` | Возвращается жанр книги по её названию |
| `test_get_books_with_specific_genre` | `get_books_with_specific_genre` | Возвращается список книг с заданным жанром |
| `test_get_books_genre` | `get_books_genre` | Возвращается текущий словарь «книга — жанр» |
| `test_get_books_for_children_includes_book_without_age_rating` | `get_books_for_children` | Книги без возрастного рейтинга попадают в список для детей (параметризация) |
| `test_get_books_for_children_excludes_book_with_age_rating` | `get_books_for_children` | Книги с возрастным рейтингом не попадают в список для детей (параметризация) |
| `test_add_book_in_favorites` | `add_book_in_favorites` | Книга добавляется в избранное и не дублируется при повторном добавлении |
| `test_delete_book_from_favorites` | `delete_book_from_favorites` | Книга удаляется из избранного |
| `test_get_list_of_favorites_books` | `get_list_of_favorites_books` | Возвращается список избранных книг |

## Параметризованные тесты

- `test_add_new_book_does_not_add_invalid_name` — проверка граничных значений длины названия
- `test_set_book_genre_does_not_set_invalid_genre` — недопустимые жанры
- `test_get_books_for_children_includes_book_without_age_rating` — жанры без возрастного рейтинга
- `test_get_books_for_children_excludes_book_with_age_rating` — жанры с возрастным рейтингом

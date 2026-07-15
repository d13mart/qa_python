import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


def test_add_new_book_add_one_book(collector):
    collector.add_new_book('Город которого нет')
    assert collector.books_genre.get('Город которого нет') == ''


@pytest.mark.parametrize(
    'book_name',
    [
        '',
        'А' * 41,
    ],
)
def test_add_new_book_does_not_add_invalid_name(collector, book_name):
    collector.add_new_book(book_name)
    assert book_name not in collector.books_genre


def test_add_new_book_does_not_add_duplicate(collector):
    collector.add_new_book('1984')
    collector.add_new_book('1984')
    assert list(collector.books_genre.keys()).count('1984') == 1


def test_set_book_genre(collector):
    collector.add_new_book('1984')
    collector.set_book_genre('1984', 'Фантастика')
    assert collector.get_book_genre('1984') == 'Фантастика'


def test_set_book_genre_does_not_set_for_unknown_book(collector):
    collector.set_book_genre('Несуществующая книга', 'Фантастика')
    assert 'Несуществующая книга' not in collector.books_genre


@pytest.mark.parametrize(
    'invalid_genre',
    ['Научная фантастика', 'Драма'],
)
def test_set_book_genre_does_not_set_invalid_genre(collector, invalid_genre):
    collector.add_new_book('1984')
    collector.set_book_genre('1984', invalid_genre)
    assert collector.get_book_genre('1984') == ''


def test_get_book_genre(collector):
    collector.add_new_book('Мастер и Маргарита')
    collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
    assert collector.get_book_genre('Мастер и Маргарита') == 'Фантастика'


def test_get_books_with_specific_genre(collector):
    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    collector.set_book_genre('Книга 1', 'Комедии')
    collector.set_book_genre('Книга 2', 'Фантастика')
    assert collector.get_books_with_specific_genre('Комедии') == ['Книга 1']


def test_get_books_genre(collector):
    collector.add_new_book('Дюна')
    collector.set_book_genre('Дюна', 'Фантастика')
    assert collector.get_books_genre() == {'Дюна': 'Фантастика'}


@pytest.mark.parametrize(
    'book_name, genre, expected_in_children',
    [
        ('Винни-Пух', 'Мультфильмы', True),
        ('Сияние', 'Ужасы', False),
        ('Шерлок Холмс', 'Детективы', False),
    ],
)
def test_get_books_for_children(collector, book_name, genre, expected_in_children):
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    children_books = collector.get_books_for_children()
    if expected_in_children:
        assert book_name in children_books
    else:
        assert book_name not in children_books


def test_add_book_in_favorites(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    assert collector.favorites == ['Гарри Поттер']


def test_delete_book_from_favorites(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    collector.delete_book_from_favorites('Гарри Поттер')
    assert collector.favorites == []


def test_get_list_of_favorites_books(collector):
    collector.add_new_book('Книга A')
    collector.add_new_book('Книга B')
    collector.add_book_in_favorites('Книга A')
    collector.add_book_in_favorites('Книга B')
    assert collector.get_list_of_favorites_books() == ['Книга A', 'Книга B']

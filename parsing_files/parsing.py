import csv
import json


with open('books.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    books = [row[0] for row in reader]


with open('users.json', mode='r', encoding='utf-8') as userprofile:
    users = json.load(userprofile)


for user in users:
    if '_id' not in user:
        raise KeyError(f"User object {user} does not contain '_id' key")


def distribute_books(books, num_users):
    num_books = len(books)
    books_per_user = num_books // num_users
    extra_books = num_books % num_users
    book_index = 0
    distributed_books = []

    for i in range(num_users):
        user_books = books[book_index:book_index + books_per_user]
        book_index += books_per_user
        if i < extra_books:
            user_books.append(books[book_index])
            book_index += 1
        distributed_books.append(user_books)

    return distributed_books


result = [
    {'user_id': user['_id'], 'books': user_books}
    for user, user_books in zip(users, distribute_books(books, len(users)))
]


with open('result.json', mode='w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

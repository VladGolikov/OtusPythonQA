import csv
import json
from files.files import JSON_FILE_PATH
from files.files import CSV_FILE_PATH


dict_books = {}
books_list = []
users_list = []
dict_users = {}

with open(JSON_FILE_PATH, 'r') as f:
    users = json.load(f)
    for user in users:
        dict_users['name'] = user['name']
        dict_users['gender'] = user['gender']
        dict_users['address'] = user['address']
        dict_users['age'] = user['age']
        users_list.append(dict_users)
        dict_users = {}

with open(CSV_FILE_PATH, newline='') as data:
    for row in csv.DictReader(data):
        dict_books['title'] = row.get('Title')
        dict_books['author'] = row.get('Author')
        dict_books['pages'] = int(row.get('Pages'))
        dict_books['genre'] = row.get('Genre')
        books_list.append(dict_books)
        dict_books = {}

while books_list:
    for user in users_list:
        if not books_list:
            break
        if 'books' in user:
            users_books = user.get('books')
        else:
            user['books'] = []
            users_books = user.get('books')
        users_books.append(books_list.pop(0))

with open("result.json", "w") as final_json:
    final_data = json.dumps(users_list, indent=4)
    final_json.write(final_data)

from flask import Flask, render_template
book = Flask(__name__)

books=[
    {'id': 1, 'name': 'Harry Potter', 'Author': 'J.K. Rowling','cover':'https://pbs.twimg.com/media/B_MYtNrW0AERKJP.jpg'},
    {'id': 2, 'name': 'Avengers Assemble', 'Author': 'J.R.R. Tolkien','cover':'https://weirdsciencemarvelcomics.files.wordpress.com/2019/09/img_4229.jpg?w=793'},
    {'id': 3, 'name': 'Marvel Avengers', 'Author': 'Stan Lee','cover':'https://weirdsciencemarvelcomics.files.wordpress.com/2019/09/img_4229.jpg?w=793'}
    ]

@book.route('/')
def index():
    return render_template('books.html', books = books )

@book.route('/book/<int:book_id>')
def show_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None )
    if book:
        return render_template('bookdetails.html', book=book)
    else:
        return "book not found!"

if __name__ == '__main__':
    book.run(debug = True)
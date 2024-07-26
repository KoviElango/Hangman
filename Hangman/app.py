from flask import Flask, render_template, request, session, redirect, url_for
from hangman import HangmanGame, get_country
from countries_data import countries

app = Flask(__name__)
app.secret_key = 'kira'
@app.route('/')
def index():
    if 'word' not in session or request.args.get('reset'):
        word = get_country(countries)
        session['word'] = word
        session['guessed_letters'] = []
        session['lives'] = 10
        session['used_letters'] = []
    
    word = session['word']
    guessed_letters = set(session['guessed_letters'])
    lives = session['lives']
    used_letters = set(session['used_letters'])

    game = HangmanGame(word, lives)
    game.guessed_letters = guessed_letters
    game.used_letters = used_letters

    return render_template('index.html', game=game, word=word, guessed_letters=guessed_letters, lives=lives, used_letters=used_letters)

@app.route('/guess', methods=['POST'])
def guess():
    letter = request.form.get('letter').upper()
    word = session['word']
    guessed_letters = set(session['guessed_letters'])
    lives = session['lives']
    used_letters = set(session['used_letters'])

    game = HangmanGame(word, lives)
    game.guessed_letters = guessed_letters
    game.used_letters = used_letters

    game.guess(letter)
    
    session['guessed_letters'] = list(game.guessed_letters)
    session['lives'] = game.lives
    session['used_letters'] = list(game.used_letters)

    if game.is_finished():
        if game.is_won():
            return redirect(url_for('won'))
        else:
            return redirect(url_for('lost'))

    return redirect(url_for('index'))

@app.route('/won')
def won():
    word = session['word']
    return render_template('won.html', word=word)

@app.route('/lost')
def lost():
    word = session['word']
    return render_template('lost.html', word=word)

if __name__ == "__main__":
    app.run(debug=True)

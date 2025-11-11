from flask import Flask
import random

number = random.randint(0, 9)
print(number)

app = Flask(__name__)

@app.route('/')
def home_route():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />')

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < number:
        return ('<h1>Number too low</h1>'
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />')
    elif guess > number:
        return (
            '<h1>Number too high</h1>'
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'
        )
    else:
        return (
            '<h1>Congratulations! You are right!</h1>'
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'
        )

if __name__ == "__main__":
    app.run(debug=True)


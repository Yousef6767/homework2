from flask import Flask, render_template, request

app = Flask(__name__)

def check_guess(guess, answer):
    if guess.lower() == answer.lower():
        return True
    return False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    score = None
    if request.method == 'POST':
        guess1 = request.form.get('guess1')
        guess2 = request.form.get('guess2')
        guess3 = request.form.get('guess3')

        score = 0
        if check_guess(guess1, "polar bear"):
            score += 1
        if check_guess(guess2, "cheetah"):
            score += 1
        if check_guess(guess3, "blue whale"):
            score += 1

    return render_template('quiz.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
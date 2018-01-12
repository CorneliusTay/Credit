from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('HomePage.html')

@app.route('/CreditSystem')
def creditsystem():
    return render_template('CreditSystem.html')


if __name__ == '__main__':
    app.run()

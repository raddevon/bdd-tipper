from flask import Flask, render_template, request

app = Flask(__name__)


def format_currency(value):
    return "${:,.2f}".format(value)

app.jinja_env.filters['currency'] = format_currency


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def results():
    result = float(request.form['meal_cost']) * \
        (float(request.form['tip_percentage']) / 100)
    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

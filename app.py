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
    context = {'errors': []}

    try:
        assert float(request.form['meal_cost']) > 0
        meal_cost = float(request.form['meal_cost'])
        context['meal_cost'] = request.form['meal_cost']
    except ValueError:
        context['errors'].append('The meal cost must be numeric.')
    except AssertionError:
        context['errors'].append('The meal cost must be greater than 0.')

    try:
        assert float(request.form['tip_percentage']) >= 0
        tip_percentage = float(request.form['tip_percentage'])
        context['tip_percentage'] = request.form['tip_percentage']
    except ValueError:
        context['errors'].append('The tip percentage must be numeric.')
    except AssertionError:
        context['errors'].append('The tip percentage cannot be negative.')

    try:
        result = meal_cost * (tip_percentage / 100)
    except (ValueError, UnboundLocalError):
        return render_template('home.html', **context)

    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

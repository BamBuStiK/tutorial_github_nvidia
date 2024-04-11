
# pip install flask

from flask import Flask, request, render_template

# rendering the html file
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        number1 = request.form.get('number1', type=float)
        number2 = request.form.get('number2', type=float)
        #print(number1, number2)
        operation = request.form.get('operation')

        print(operation)

        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            if number2 == 0:
                result = 'Invalid Error'
            else:
                result = number1 / number2
        # server sends a request to client and receives response
        return render_template('first_template.html', result=result)
    else:
        return render_template('first_template.html', result=None)


if __name__ == '__main__':
    app.run(debug=True, port='5050')



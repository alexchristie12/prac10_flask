from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)<h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius="0"):
    celsius = float(celsius)
    return celsius_to_fahrenheit(celsius)


def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"{celsius} degrees celsius converts to {fahrenheit} degrees fahrenheit."


if __name__ == '__main__':
    app.run()

from flask import Flask
from flask import request, render_template

application = app = Flask(__name__)


@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    fahrenheit = fahrenheit_from(celsius)
    return render_template('index.html', fahrenheit=fahrenheit)


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return ""
    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

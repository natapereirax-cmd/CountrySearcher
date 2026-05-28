from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BASE_URL = "https://restcountries.com/v3.1/name/"


@app.route('/', methods=['GET', 'POST'])
def home():

    country_data = None
    error = None

    if request.method == 'POST':

        country_name = request.form.get('country')

        try:
            response = requests.get(BASE_URL + country_name, timeout=5)

            if response.status_code == 404:
                error = "No country found"

            else:
                response.raise_for_status()

                data = response.json()[0]

                currencies = data.get('currencies', {})
                currency_name = "Not informed"

                if currencies:
                    currency_name = list(currencies.values())[0]['name']

                country_data = {
                    'name': data['name']['official'],
                    'capital': data.get('capital', ['Not informed'])[0],
                    'region': data.get('region', 'Not informed'),
                    'population': data.get('population', 'Not informed'),
                    'currency': currency_name
                }

        except requests.exceptions.RequestException as error_message:
            error = f'Erro: {error_message}'

    return render_template(
        'index.html',
        country=country_data,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
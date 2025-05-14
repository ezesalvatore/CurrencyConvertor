from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

CURRENCIES = {
    'USD': 'US Dollar',
    'EUR': 'Euro',
    'GBP': 'British Pound',
    'JPY': 'Japanese Yen',
    'CAD': 'Canadian Dollar'
}

CURRENCY_INFO = {
    'USD': {
        'name': 'US Dollar',
        'symbol': '$',
        'country': 'United States',
        'image': 'USD.jpeg'
    },
    'EUR': {
        'name': 'Euro',
        'symbol': '€',
        'country': 'European Union',
        'image': 'EUR.jpeg'
    },
    'GBP': {
        'name': 'British Pound',
        'symbol': '£',
        'country': 'United Kingdom',
        'image': 'GBP.jpeg'
    },
    'JPY': {
        'name': 'Japanese Yen',
        'symbol': '¥',
        'country': 'Japan',
        'image': 'JPY.jpg'
    },
    'CAD': {
        'name': 'Canadian Dollar',
        'symbol': 'C$',
        'country': 'Canada',
        'image': 'CAD.jpg'
    }
}

API_KEY = "89b158f9bc89cf872b350fce"

@app.route('/')
def index():
    return render_template('index.html', currencies=CURRENCIES)

@app.route('/gallery')
def gallery():
    return render_template('currency-gallery.html', currency_info=CURRENCY_INFO)

@app.route('/convert', methods=['POST'])
def convert():
    amount = request.form.get('amount', 1)
    from_currency = request.form.get('from_currency', 'USD')
    to_currency = request.form.get('to_currency', 'EUR')
    
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    
    response = requests.get(url)
    data = response.json()
    
    if data.get('result') == 'success':
        rate = data['conversion_rates'][to_currency]
        
        converted_amount = float(amount) * rate
        
        date = data.get('time_last_update_utc', '').split(' ', 1)[1]
        
        return render_template(
            'index.html',
            currencies=CURRENCIES,
            amount=amount,
            from_currency=from_currency,
            to_currency=to_currency,
            converted_amount=converted_amount,
            rate=rate,
            date=date,
            success=True
        )
    else:
        error = "Sorry, something went wrong. Please try again."
        return render_template(
            'index.html',
            currencies=CURRENCIES,
            error=error
        )

if __name__ == '__main__':
    app.run(debug=True)
# Simple currency converter app
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Just a few currencies for simplicity
CURRENCIES = {
    'USD': 'US Dollar',
    'EUR': 'Euro',
    'GBP': 'British Pound',
    'JPY': 'Japanese Yen',
    'CAD': 'Canadian Dollar'
}

# API key
API_KEY = "89b158f9bc89cf872b350fce"

@app.route('/')
def index():
    return render_template('index.html', currencies=CURRENCIES)

@app.route('/convert', methods=['POST'])
def convert():
    # Get form data
    amount = request.form.get('amount', 1)
    from_currency = request.form.get('from_currency', 'USD')
    to_currency = request.form.get('to_currency', 'EUR')
    
    # API URL
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    
    # Get data from API
    response = requests.get(url)
    data = response.json()
    
    # Check if request was successful
    if data.get('result') == 'success':
        # Get exchange rate
        rate = data['conversion_rates'][to_currency]
        
        # Calculate converted amount
        converted_amount = float(amount) * rate
        
        # Get the date
        date = data.get('time_last_update_utc', '').split(' ', 1)[1]
        
        # Return results to template
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
        # Return error
        error = "Sorry, something went wrong. Please try again."
        return render_template(
            'index.html',
            currencies=CURRENCIES,
            error=error
        )

if __name__ == '__main__':
    app.run(debug=True)
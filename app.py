"""
Course: CST 205 - Python Multimedia Programming
Title: Currency Converter
Abstract: A Flask-based web application that allows users to convert between 
different currencies using real-time exchange rates from the ExchangeRate API. 
The application also features a currency gallery with interactive image filters (grayscale, sepia, and negative) 
applied to currency images.
Authors: Salvatore Eze
Date: 5/14/2025

Project Structure:
- Since this is a solo project

Important Code Blocks:
1. Flask Routes (/app.py):
   - @app.route('/'): The index route that renders the landing page
   - @app.route('/gallery'): Renders the currency gallery with image filter
   - @app.route('/convert', methods=['POST']): Handles the currency conversion using the ExchangeRate API

2. API Integration (/app.py):
   - The convert() function makes a request to the ExchangeRate API using the requests library
   - API_KEY = "89b158f9bc89cf872b350fce"

3. Image Manipulation (/static/js/image-filters.js):
   - applyFilter(): Core function that takes a filter function and applies it to the canvas
   - applyGrayscale(): Implements grayscale filter
   - applySepia(): Creates a sepia tone 
   - applyNegative(): Inverts all colors
   
Sources:
- Exchange Rate API: https://www.exchangerate-api.com/
- Bootstrap 5.3.0: https://getbootstrap.com/
"""

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
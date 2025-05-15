# Currency Converter

A full-featured web application that provides real-time currency conversion with an interactive currency gallery and image filtering capabilities.

## Overview

Currency Converter is a Flask-based web application designed for travelers and professionals who need conversions. The app fetches real-time exchange rates from the ExchangeRate API.

## Team Member

- Salvatore Eze

## Course Information

- **Course**: CST 205 - Python Multimedia Programming
- **Institution**: CSUMB
- **Date of Completion**: May 14, 2025

## Features

- **Real-time Currency Conversion**: Convert between USD, EUR, GBP, JPY, and CAD with current exchange rates
- **Currency Gallery**: Browse information about different currencies with visual representation
- **Interactive Image Filters**: Apply professional-quality filters:
  - Grayscale: Classic black and white effect
  - Sepia: Vintage brown-toned effect
  - Negative: Inverted color effect


## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/ezesalvatore/CurrencyConvertor.git
   cd CurrencyConvertor
   ```

2. **Install the required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application**
   ```bash
   # Development mode
   flask run --debug
   ```

4. **Access the application**
   
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## API

This project uses the [ExchangeRate API](https://www.exchangerate-api.com/) to fetch current exchange rates. The API call is made in the `/convert` route when a user submits the conversion form.

```python
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
```

## Important Links

- **GitHub Repository**: [https://github.com/ezesalvatore/CurrencyConvertor](https://github.com/ezesalvatore/CurrencyConvertor)
- **Trello Board**: [https://trello.com/b/4jO4z41W/currency-convertor](https://trello.com/b/4jO4z41W/currency-convertor)
- **ExchangeRate API**: [https://www.exchangerate-api.com/](https://www.exchangerate-api.com/)

## Future Work


1. **Historical Exchange Rate Visualization**: Implement charts to show rate trends over time
2. **User Accounts**: Add authentication for personalized experiences
3. **Expanded Currency Support**: Add support for 50+ global currencies
4. **Cryptocurrency Integration**: Add support for Bitcoin, Ethereum, and other cryptocurrencies

---

*This project was created as part of the CST 205 - Python Multimedia Programming course at CSUMB.*
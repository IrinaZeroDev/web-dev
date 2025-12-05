from flask import Flask, render_template, jsonify, request
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Функция для получения цитаты с ZenQuotes API
def get_zen_quote():
    try:
        response = requests.get('https://zenquotes.io/api/random')
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                quote_data = data[0]
                return {
                    'quote': quote_data.get('q', 'No quote available'),
                    'author': quote_data.get('a', 'Unknown'),
                    'source': 'ZenQuotes'
                }
    except Exception as e:
        print(f"Error fetching from ZenQuotes: {e}")
    return None

# Функция для получения цитаты с API Ninjas
def get_ninja_quote():
    try:
        headers = {'X-Api-Key': 'your_api_key_here'}
        response = requests.get('https://api.api-ninjas.com/v1/quotes?limit=1', headers=headers)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                quote_data = data[0]
                return {
                    'quote': quote_data.get('quote', 'No quote available'),
                    'author': quote_data.get('author', 'Unknown'),
                    'source': 'API Ninjas'
                }
    except Exception as e:
        print(f"Error fetching from API Ninjas: {e}")
    return None

@app.route('/')
def index():
    quote = None
    error = None
    api_source = request.args.get('api', 'zenquotes')
    
    if api_source == 'ninjas':
        quote = get_ninja_quote()
        if not quote:
            error = 'Ошибка при получении цитаты с API Ninjas. Попробуйте позже.'
    else:
        quote = get_zen_quote()
        if not quote:
            error = 'Ошибка при получении цитаты с ZenQuotes. Попробуйте позже.'
    
    return render_template('index.html', quote=quote, error=error, api_source=api_source)

@app.route('/api/quote')
def api_quote():
    api_source = request.args.get('api', 'zenquotes')
    
    if api_source == 'ninjas':
        quote = get_ninja_quote()
    else:
        quote = get_zen_quote()
    
    if quote:
        return jsonify({'success': True, 'data': quote})
    else:
        return jsonify({'success': False, 'error': 'Failed to fetch quote'}), 400

if __name__ == '__main__':
    app.run(debug=True)

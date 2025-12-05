# VD08 - Flask Random Quotes API App

## Description

A simple Flask web application that fetches random quotes from public APIs and displays them on a web page. The application allows users to switch between different quote sources and displays quotes with beautiful Bootstrap styling.

## Features

- **Dual API Integration**: Supports two different quote APIs
  - ZenQuotes API (https://zenquotes.io/api/random)
  - API Ninjas Quotes API (https://api-ninjas.com/api/quotes)
- **Beautiful UI**: Bootstrap-based responsive design with gradient backgrounds
- **Quote Display**: Shows quotes in cards with author information
- **Error Handling**: Graceful error messages if API calls fail
- **API Switching**: Users can switch between different quote sources

## Project Structure

```
VD08/
├── app.py                 # Flask application with API integration
├── templates/
│   └── index.html        # HTML template with Bootstrap styling
└── README.md             # This file
```

## Technologies Used

- **Python 3**: Programming language
- **Flask**: Web framework for building the application
- **Requests**: Library for making HTTP requests to APIs
- **Bootstrap 5**: CSS framework for responsive design
- **Jinja2**: Templating engine for HTML rendering

## Installation & Running

1. Install required dependencies:
   ```bash
   pip install flask requests
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## How It Works

1. **Home Page**: The index route displays a random quote on page load
2. **Get Quote Buttons**: Click the buttons to fetch quotes from different APIs
3. **Error Handling**: If an API fails, an error message is displayed
4. **Responsive Design**: Works on desktop, tablet, and mobile devices

## API Details

### ZenQuotes API
- Endpoint: `https://zenquotes.io/api/random`
- Returns: Random quote with author
- Rate Limit: Generous (no strict rate limiting)

### API Ninjas Quotes API
- Endpoint: `https://api-ninjas.com/api/quotes`
- Returns: Quote with category information
- Note: May require API key for higher rate limits

## Code Highlights

The `app.py` file contains:
- `get_zen_quote()`: Fetches quotes from ZenQuotes API
- `get_ninja_quote()`: Fetches quotes from API Ninjas
- `index()`: Main route that renders the HTML template
- Error handling with try-except blocks

## Future Enhancements

- Add more API sources
- Implement quote favorites/bookmarking
- Add quote categories filter
- Database integration for storing favorites
- User preferences and themes

## Author

Created as part of web development coursework (VD08 assignment)

## License

Open source - feel free to use and modify

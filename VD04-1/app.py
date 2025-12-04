from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Получаем текущие дату и время
    current_time = datetime.now()
    
    # Форматируем в удобный вид
    formatted_date = current_time.strftime('%d.%m.%Y')
    formatted_time = current_time.strftime('%H:%M:%S')
    formatted_datetime = current_time.strftime('%d.%m.%Y %H:%M:%S')
    
    return render_template('index.html', 
                         date=formatted_date, 
                         time=formatted_time,
                         datetime_str=formatted_datetime)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Список для сохранения данных о доставителях
users_data = []

@app.route('/', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        
        # Проверяем, что все поля заполнены
        if name and city and hobby and age:
            # Добавляем данные в список
            users_data.append({
                'name': name,
                'city': city,
                'hobby': hobby,
                'age': age
            })
    
    # Отображаем темплейт с данными
    return render_template('form.html', users=users_data)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

# Меню для всех страниц
navigation = [
    {'title': 'Главная', 'url': '/'},
    {'title': 'Блог', 'url': '/blog'},
    {'title': 'Контакты', 'url': '/contacts'}
]

@app.route('/')
def index():
    return render_template('index.html', nav=navigation, current_page='index')

@app.route('/blog')
def blog():
    blog_posts = [
        {'title': 'Что такое Flask?', 'excerpt': 'Flask это микросервис для web-разработки...'},
        {'title': 'Python для веб-разработки', 'excerpt': 'Пытон используется для создания web-аппликаций...'},
        {'title': 'Jinja2 в Flask', 'excerpt': 'Jinja2 это мощный темплейтор для Flask...'}
    ]
    return render_template('blog.html', nav=navigation, current_page='blog', posts=blog_posts)

@app.route('/contacts')
def contacts():
    contact_info = {
        'email': 'example@mail.com',
        'phone': '+7 (999) 123-45-67',
        'address': 'Москва, Россия'
    }
    return render_template('contacts.html', nav=navigation, current_page='contacts', contact=contact_info)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модель пользователя
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

# Данные сессии (для простоты)
current_user = None

@app.route('/')
def home():
    return render_template('home.html', user=current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Проверка валидации
        if not username or not email or not password or not confirm_password:
            flash('Пожалуйста, заполните все поля', 'danger')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Пароли не совпадают', 'danger')
            return redirect(url_for('register'))
        
        # Проверка на существование
        if User.query.filter_by(username=username).first():
            flash('Пользователь с этим именем уже существует', 'danger')
            return redirect(url_for('register'))
        
        # Создание пользователя
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Пользователь успешно зарегистрирован', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    global current_user
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            current_user = user
            flash(f'Нормально вошли в {user.username}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Неверные креденциалы', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    global current_user
    current_user = None
    flash('Вы вышли', 'info')
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if not current_user:
        flash('Пожалуйста, войдите в свой аккаунт', 'warning')
        return redirect(url_for('login'))
    return render_template('profile.html', user=current_user)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    global current_user
    if not current_user:
        flash('Пожалуйста, войдите в свой аккаунт', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        new_username = request.form.get('username')
        new_email = request.form.get('email')
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        # Проверка старого пароля
        if not current_user.check_password(old_password):
            flash('Неверный текущий пароль', 'danger')
            return redirect(url_for('edit_profile'))
        
        # Обновление имени
        if new_username and new_username != current_user.username:
            if User.query.filter_by(username=new_username).first():
                flash('Это имя уже заято', 'danger')
                return redirect(url_for('edit_profile'))
            current_user.username = new_username
        
        # Обновление почты
        if new_email and new_email != current_user.email:
            if User.query.filter_by(email=new_email).first():
                flash('Эта почта уже регистрирована', 'danger')
                return redirect(url_for('edit_profile'))
            current_user.email = new_email
        
        # Обновление пароля
        if new_password:
            if new_password != confirm_password:
                flash('Новые пароли не совпадают', 'danger')
                return redirect(url_for('edit_profile'))
            current_user.set_password(new_password)
        
        db.session.commit()
        flash('Профиль успешно обновлен', 'success')
        return redirect(url_for('profile'))
    
    return render_template('edit_profile.html', user=current_user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

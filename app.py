from flask import Flask, render_template, request, redirect
from telebot import TeleBot
import time
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite'
token = 'token'
bot = TeleBot(token)


def send_trouble(msg):
    chat = 'id'
    bot.send_message(chat, f"{msg}")


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        kb = request.form['kab']
        txt = request.form['info']
        msg = 'Кабинет № - ' + str(kb) + '\n' 'Проблема - ' + str(txt) + '\n' + time.strftime("Заявка отправлена в %H:%M", time.localtime())
        send_trouble(msg)
        return "<p>Сообщение доставлено</p><br><a href='/'>Нажмите что бы вернуться</a>"
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

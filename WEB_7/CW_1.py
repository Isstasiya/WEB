from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def sl():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>\
            Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!"

@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="https://media.salon.com/2021/01/life-on-mars-growing-0129211.jpg" width=40%>
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""

@app.route('/promotion_image')
def bootstrap():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link href="{url_for('static', filename='style/style.css')}" rel="stylesheet" type="text/css">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="https://media.salon.com/2021/01/life-on-mars-growing-0129211.jpg" width=40%>
                    <p class="alert-dark" role="alert">Человечество вырастает из детства.</p>
                    <p class="alert-success" role="alert">Человечеству мала одна планета.</p>
                    <p class="alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class="alert-warning" role="alert">И начнем с Марса!</p>
                    <p class="alert-danger" role="alert">Присоединяйся!</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
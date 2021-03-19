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

@app.route('/astronaut_selection')
def astronaut():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <link href="{url_for('static', filename='style/style.css')}" rel="stylesheet" type="text/css">
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <div style='margin-left:35%'>
                      <h1 style='margin-left:5%; color: black'">Анкета претендента</h1>
                      <h3 style='margin-left:5%'>на участие в миссии</h3>
                      <div>
                        <form class="form" class="login_form" method="post">
                          <input type="text" class="form-control" id="surname" aria-describedby="surnamelHelp" placeholder="Введите фамилию" name="surname">         
                          <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                          <br>
                          <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                          <div class="form-group">
                            <label for="eduSelect">Какое у Вас образование?</label>
                            <select class="form-control" id="classSelect" name="edu">
                              <option>Начальное</option>
                              <option>Среднее</option>
                              <option>Выше среднего</option>
                              <option>Супер!</option>
                            </select>
                          </div>
                          <label for="eduSelect">Какие у Вас есть профессии?</label>
                          <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="prof" name="prof">
                            <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                            <br>
                            <input type="checkbox" class="form-check-input" id="prof" name="prof1">
                            <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                            <br>
                            <input type="checkbox" class="form-check-input" id="prof" name="prof2">
                            <label class="form-check-label" for="acceptRules">Пилот</label>
                            <br>
                            <input type="checkbox" class="form-check-input" id="prof" name="prof3">
                            <label class="form-check-label" for="acceptRules">Метеоролог</label>
                            <br>
                            <input type="checkbox" class="form-check-input" id="prof" name="prof4">
                            <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                            <br>
                            <input type="checkbox" class="form-check-input" id="prof" name="prof5">
                            <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                            <br>
                            <input type="checkbox" class="form-check-input" id="prof" name="prof6">
                            <label class="form-check-label" for="acceptRules">Врач</label>
                            <br>
                            <input type="checkbox" class="form-check-input" id="prof" name="prof7">
                            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                          </div>
                          <div class="form-group">
                            <label for="form-check">Укажите пол</label>
                            <div class="form-check">
                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                              <label class="form-check-label" for="male">
                                Мужской
                              </label>
                            </div>
                            <div class="form-check">
                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                              <label class="form-check-label" for="female">
                                Женский
                              </label>
                            </div>
                          </div>
                          <div class="form-group">
                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                          </div>
                          <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                          </div>
                          <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                          </div>
                          <button type="submit" class="btn btn-primary">Отправить</button>
                        </form>
                      </div>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
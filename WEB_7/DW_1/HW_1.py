from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/load_photo', methods=['GET'])
def lget():
    file = url_for('static', filename='img/robo.jpg')
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <style>
                      div{{
                        background-color: rgb(214, 191, 163);
                        width: 50%;
                      }}
                    </style>
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <center>
                      <h1>Загрузка фотографии</h1>
                      <h3>Для участиия в миссии</h3>
                      <div>
                          <form class="login_form" method="post" enctype="multipart/form-data">
                          <div class="form-group">
                              <label for="photo">Приложите фотографию</label>
                              <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                            <img src="{file}">
                            <br>
                            <button type="submit" class="btn btn-primary">Отправить</button>
                          </form>
                      </div>
                    </center>
                  </body>
                </html>"""

@app.route('/load_photo', methods=['POST'])
def lpost():
    f = request.files['file']
    file = url_for('static', filename=f'img/{f.filename}')
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <style>
                      div{{
                        background-color: rgb(214, 191, 163);
                        width: 50%;
                      }}
                    </style>
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <center>
                      <h1>Загрузка фотографии</h1>
                      <h3>Для участиия в миссии</h3>
                      <div>
                          <form class="login_form" method="post" enctype="multipart/form-data">
                          <div class="form-group">
                              <label for="photo">Приложите фотографию</label>
                              <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                            <img src="{file}">
                            <br>
                            <button type="submit" class="btn btn-primary">Отправить</button>
                          </form>
                      </div>
                    </center>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
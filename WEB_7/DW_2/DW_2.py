from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/carousel', methods=['GET', 'POST'])
def lget():
    file1 = url_for('static', filename='img/pic_1.jpg')
    file2 = url_for('static', filename='img/pic_2.jpg')
    file3 = url_for('static', filename='img/pic_3.jpg')
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
                    integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
                    integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
                    <title>Пейзажи Марса</title>
                  </head>
                  <body>
                    <center>
                      <h1>Пейзажи Марса</h1>
                      <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                        <ol class="carousel-indicators">
                          <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                          <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                          <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                        </ol>
                        <div class="carousel-inner" role="listbox" style="width:50%">
                          <div class="carousel-item active">
                            <img class="d-block w-100" src="{file1}" alt="First slide">
                          </div>
                          <div class="carousel-item">
                            <img class="d-block w-100" src="{file2}" alt="Second slide">
                          </div>
                          <div class="carousel-item">
                            <img class="d-block w-100" src="{file3}" alt="Third slide">
                          </div>
                        </div>
                      </div>
                    </center>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
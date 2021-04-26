import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from design import Ui_Frame
from PyQt5 import uic, QtWidgets
from PIL.ImageQt import ImageQt
from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QBitmap
import requests
import math

coord_to_geo_x = 0.0000428
coord_to_geo_y = 0.0000428

def show_map(jll, spn, k, pt=None):
    if pt:
        map_params = {
        "ll": jll,
        "spn": spn,
        "l": k,
        "pt": f"{pt},pm2dgl"
        }
    else:
        map_params = {
        "ll": jll,
        "spn": spn,
        "l": k
        }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    print(response.url)
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except Exception as a:
        print(a)

class Example(QMainWindow, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.address, self.spn = input().split()
        self.k = "map"
        self.pt = None
        show_map(self.address, self.spn, self.k)
        self.address = [float(i) for i in self.address.split(",")]
        self.spn = [float(i) for i in self.spn.split(",")]
        im = QPixmap("map.png")
        self.label.setPixmap(im)
        self.radioButton_4.setChecked(True)
        self.radioButton_2.clicked.connect(self.nk)
        self.radioButton_3.clicked.connect(self.nk)
        self.checkBox.clicked.connect(self.nf)
        self.pushButton_2.clicked.connect(self.nf)
        self.pushButton.clicked.connect(self.nt)
        self.show()

    def nk(self):
        if self.sender().text() == 'Спутник':
            self.k = "sat"
        elif self.sender().text() == 'Карта':
            self.k = "map"
        else:
            self.k = "sat,skl"
        self.sh()

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            if event.x() > 0 and event.x() < 571:
                if event.y() > 70 and event.y() < 481:
                    st = []
                    st.append(-(285.5 - event.x()))
                    st.append(-(240.5 - event.y() - 70))
                    lx = self.address[0] + st[1] * coord_to_geo_x * self.spn[0]
                    ly = self.address[1] + st[0] * coord_to_geo_y * math.cos(math.radians(self.address[1])) * self.spn[0]
                    s = ",".join([str(lx), str(ly)])
                    req = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={s}&format=json"
                    res = requests.get(req)
                    if res:
                        js = res.json()
                    else:
                        raise RuntimeError('Ошибка')
                    top = js["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                    if self.checkBox.isChecked():
                        txt = top["metaDataProperty"]["GeocoderMetaData"]["text"] + ", " + top["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
                        self.lineEdit_2.setText(txt)
                    else:
                        self.lineEdit_2.setText(top["metaDataProperty"]["GeocoderMetaData"]["text"])
                    self.pt = s
                    self.lineEdit_2.setText('')
                    self.lineEdit.setText('')
                    self.sh()
        elif (event.button() == Qt.RightButton):
            if event.x() > 0 and event.x() < 571:
                if event.y() > 70 and event.y() < 481:
                    st = []
                    st.append(-(285.5 - event.x()))
                    st.append(-(240.5 - event.y() - 70))
                    lx = self.address[0] + st[1] * coord_to_geo_x * math.pow(2, 2 - self.spn[0])
                    ly = self.address[1] - st[0] * coord_to_geo_y * math.cos(math.radians(self.address[1])) * math.pow(2, 2 - self.spn[0])
                    s = ",".join([str(lx), str(ly)])
                    req = f"https://search-maps.yandex.ru/v1/?apikey=dda3ddba-c9ea-4ead-9010-f43fbc15c6e3&ll={s}&format=json&type=biz&text=Москва&lang=ru_RU"
                    res = requests.get(req)
                    if res:
                        js = res.json()
                    else:
                        raise RuntimeError('Ошибка')
                    top = js["features"][0]
                    k = [float(i) for i in top["geometry"]["coordinates"]]
                    we = ((k[0] - self.address[0]) ** 2 + (k[1] - self.address[1]) ** 2) ** 0.5 * 111
                    if we <= 5000:
                        k = ",".join([str(i) for i in k])
                        req = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={k}&format=json"
                        res = requests.get(req)
                        if res:
                            js = res.json()
                        else:
                            raise RuntimeError('Ошибка')
                        top = js["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                        if self.checkBox.isChecked():
                            txt = top["metaDataProperty"]["GeocoderMetaData"]["text"] + ", " + top["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
                            self.lineEdit_2.setText(txt)
                        else:
                            self.lineEdit_2.setText(top["metaDataProperty"]["GeocoderMetaData"]["text"])
                        self.pt = s
                        self.lineEdit_2.setText('')
                        self.lineEdit.setText('')
                        self.sh()

    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == Qt.Key_Up:
            self.address[0] += 0.001 * math.pow(2, 10 - self.spn[0])
        elif event.key() == Qt.Key_Down:
            self.address[0] -= 0.001 * math.pow(2, 10 - self.spn[0])
        elif event.key() == Qt.Key_Right:
            self.address[1] += 0.01 * math.pow(2, 10 - self.spn[0])
        elif event.key() == Qt.Key_Left:
            self.address[1] -= 0.01 * math.pow(2, 10 - self.spn[0])
        elif event.key() == Qt.Key_PageUp:
            if self.spn[0] < 5:
                self.spn[0] += 0.01
                self.spn[1] += 0.01
        elif event.key() == Qt.Key_PageDown:
            if self.spn[1] >= 0.001:
                self.spn[0] -= 0.001
                self.spn[1] -= 0.001
        self.sh()

    def nf(self):
        s = self.lineEdit.text()
        req = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={s}&format=json"
        res = requests.get(req)
        if res:
            js = res.json()
        else:
            raise RuntimeError('Ошибка')
        top = js["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        coor = top["Point"]["pos"]
        if self.checkBox.isChecked():
            txt = top["metaDataProperty"]["GeocoderMetaData"]["text"] + ", " + top["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
            self.lineEdit_2.setText(txt)
        else:
            self.lineEdit_2.setText(top["metaDataProperty"]["GeocoderMetaData"]["text"])
        coor = ','.join(coor.split())
        self.pt = coor
        self.address = [float(i) for i in coor.split(",")]
        self.sh()

    def nt(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.pt = None
        self.sh()
    
    def sh(self):
        show_map(",".join([str(i) for i in self.address]), ",".join([str(i) for i in self.spn]), self.k, self.pt)
        im = QPixmap("map.png")
        self.label.setPixmap(im)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
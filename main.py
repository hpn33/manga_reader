import os
import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)

path = 'image/'
image_list = os.listdir(path)

for i in range(len(image_list)):
	image_list[i] = f'{path}{image_list[i]}'

formLayout = QFormLayout()
groupBox = QGroupBox("This Is Group Box")

labelLis = []
max_width = 0

for i in range(0, len(image_list)):
	image_address = image_list[i]
	
	label = QLabel()
	pixmap = QPixmap(image_address)
	label.setPixmap(pixmap)
	label.setAlignment(Qt.AlignCenter)
	
	hb = QHBoxLayout()
	hb.addWidget(label)
	
	labelLis.append(hb)
	
	formLayout.addRow(labelLis[i])
	
	max_width = max(max_width, pixmap.width())

groupBox.setLayout(formLayout)

scroll = QScrollArea()
scroll.setWidget(groupBox)
scroll.setWidgetResizable(True)

layout = QVBoxLayout(window)
layout.addWidget(scroll)

window.resize(max_width, 800)
window.show()

sys.exit(app.exec_())

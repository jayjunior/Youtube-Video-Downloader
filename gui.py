from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit, QWidget,QFormLayout,QPushButton,QMessageBox,QLabel
from PyQt5.QtCore import Qt as al
import download

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Youtube Video Download 🔥")




        layout = QFormLayout()

        widget = QWidget()

        self.setMinimumWidth(250)
        self.setMaximumHeight(100)

        self.input = QLineEdit()
        self.button = QPushButton("download")
        self.button.setStyleSheet("background-color:green;color:white;")

        self.button.clicked.connect(self.download_video)
       
        self.button.move(100,0)
        self.input.setAlignment(al.AlignLeft)
        self.input.setStyleSheet("border:1px solid black;background-color:white;")
        
        

        layout.addRow("URL",self.input)
        layout.addRow("",self.button)



        widget.setLayout(layout)


        self.setCentralWidget(widget)

    def create_dialog_box(self,message):
        dlg = QMessageBox(self)
        dlg.setText(message)
        dlg.setIcon(QMessageBox.Information)
        dlg.exec()

    def download_video(self):

        path = download.download_video(self.input.text())
        if(path == None):
            self.create_dialog_box("Something went Wrong !! check the url and the internet connection")
        else:
            self.create_dialog_box("Download Finished!")
            


app = QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec()
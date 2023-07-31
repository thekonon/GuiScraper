import sys, re, webbrowser
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from MainWindowGUI_ui import Ui_MainWindow

def is_valid_url(url):
    # Regular expression pattern to match a valid URL
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return bool(re.match(url_pattern, url))

class GuiLoader(QMainWindow, Ui_MainWindow):
    """_summary_
    This class is responsible for handling loading ui file and it adds actions 
    Args:
        QMainWindow (_type_):   PySide class
        Ui_MainWindow:          PySide editor class output defined in .py file
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Set the buttons actions
        self.setup_button_actions()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.tableWidget.editItem(self.tableWidget.currentItem())
            
    def setup_button_actions(self):
        # Connect button clicks to respective slot or function
        self.scrapeAllButton.clicked.connect(self.on_scrape_all_button_clicked)
        self.BRButton.clicked.connect(self.on_br_button_clicked)
        self.UDButton.clicked.connect(self.on_ud_button_clicked)
        self.tableWidget.itemDoubleClicked.connect(self.on_table_widget_item_clicked)        
    # Define the functions to be executed when buttons are clicked
    def on_scrape_all_button_clicked(self):
        table_widget = self.tableWidget
        df_table = self.data_table
        
        if not hasattr(self, 'data_table'):
            # Create a new row with the necessary data
            df_table = pd.DataFrame([['Data 1', 'Data 2', 'Data 3']])  # Replace with your actual data
            table_widget.setColumnCount(df_table.shape[1])
            table_widget.setRowCount(1)
        else:
            table_widget.setRowCount(df_table.shape[0])
            table_widget.setColumnCount(df_table.shape[1])
            table_widget.setHorizontalHeaderLabels(df_table.columns)

        for row in range(df_table.shape[0]):
            for col in range(df_table.shape[1]):
                value = str(df_table.iat[row, col])
                item = QTableWidgetItem(value)
                table_widget.setItem(row, col, item)
        table_widget.resizeColumnsToContents()
    def on_br_button_clicked(self):
        print("BezRealitky button clicked!")
    def on_ud_button_clicked(self):
        print("UlovDomov button clicked!")    
    def on_table_widget_item_clicked(self, item):
        if is_valid_url(item.text()):
            webbrowser.open(item.text())

class ScrapperApp(GuiLoader):
    def __init__(self, table:pd.DataFrame):
        # Set necessary attributes and settings before creating the QGuiApplication instance
        QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
        QApplication.setAttribute(Qt.AA_UseSoftwareOpenGL)
        self.data_table = table
        self.app = QApplication(sys.argv)
        super().__init__()
        self.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    window = ScrapperApp()
    

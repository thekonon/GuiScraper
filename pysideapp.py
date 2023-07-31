import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

class GuiLoader(QMainWindow):
    """_summary_
    This class is responsible for handling loading .ui file and it adds actions 
    Args:
        QMainWindow (_type_): _description_
    """
    def __init__(self):
        super().__init__()

        # Load the UI file
        self.load_ui()
        
        # Set the buttons actions
        self.setup_button_actions()

    def load_ui(self):
        # Load the UI file using QUiLoader
        ui_file = QFile("MainWindowGUI.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        # Set the loaded UI as the central widget of the main window
        if self.ui:
            self.setCentralWidget(self.ui)
        else:
            print("Error: Unable to load UI file.")
            
    def setup_button_actions(self):
        # Find buttons by their names (matching the names in the UI file)
        scrape_all_button   = self.ui.scrapeAllButton
        br_button           = self.ui.BRButton
        ud_button           = self.ui.UDButton

        # Connect button clicks to respective slot or function
        scrape_all_button.clicked.connect(self.on_scrape_all_button_clicked)
        br_button.clicked.connect(self.on_br_button_clicked)
        ud_button.clicked.connect(self.on_ud_button_clicked)

    # Define the functions to be executed when buttons are clicked
    def on_scrape_all_button_clicked(self):
        # Create a new row with the necessary data
        new_row_data = ['Data 1', 'Data 2', 'Data 3']  # Replace with your actual data

        # Add the new row to the QTableWidget
        table_widget = self.ui.tableWidget
        table_widget.setColumnCount(3)
        row_count = table_widget.rowCount()
        table_widget.insertRow(row_count)

        for col, data in enumerate(new_row_data):
            item = QTableWidgetItem(data)
            table_widget.setItem(row_count, col, item)

    def on_br_button_clicked(self):
        print("BezRealitky button clicked!")

    def on_ud_button_clicked(self):
        print("UlovDomov button clicked!")

class ScrapperApp(GuiLoader):
    def __init__(self):
        # Set necessary attributes and settings before creating the QGuiApplication instance
        QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
        QApplication.setAttribute(Qt.AA_UseSoftwareOpenGL)
        
        self.app = QApplication(sys.argv)
        super().__init__()
        self.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    window = ScrapperApp()
    

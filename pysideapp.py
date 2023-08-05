import sys, re, webbrowser, json, glob, os
from typing import Optional
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QDialog
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from MainWindowGUI_ui import Ui_MainWindow
from SettingsDialog_ui import Ui_Dialog
from scrapers import BezrealitkyScraper, get_current_datetime_string, ScrapedDataComparator

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



class SettingsDialogWrapper(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.initialize_values()
        self.saveButton.clicked.connect(self.on_save_button_clicked)
    
    def initialize_values(self):
        self.BRUrlEdit.setText(self.parent.bez_realitky_url) 
        self.BRUrlEdit.setCursorPosition(0)
        self.UDUrlEdit.setText(self.parent.ulov_domov_url)
        self.UDUrlEdit.setCursorPosition(0)
        if self.parent.browser == "Chrome":
            # self.BrowserSelectCombo.itm
            print('setting Chrome')
            self.BrowserSelectCombo.setCurrentText("Chrome")
        elif self.parent.browser == "Firefox":
            if self.parent.is_silent:
                print('Firefox - silent')
                self.BrowserSelectCombo.setCurrentText("Firefox - silent")
            else:
                print('Firefox - normal')
                self.BrowserSelectCombo.setCurrentText("Firefox - normal")
    
    def on_save_button_clicked(self):
        print("Save button clicked!")
        self.parent.bez_realitky_url = self.BRUrlEdit.text()
        self.parent.ulov_domov_url = self.UDUrlEdit.text()
        if self.BrowserSelectCombo.currentText() == "Chrome":
            self.parent.browser = "Chrome"
        elif self.BrowserSelectCombo.currentText() == "Firefox - silent":
            self.parent.browser = "Firefox"
            self.parent.is_silent = 1
        elif self.BrowserSelectCombo.currentText() == "Firefox - normal":
            self.parent.browser = "Firefox"
            self.parent.is_silent = 0
        self.parent.save_config()
        
    def show(self):
        # Show the settings dialog
        self.setWindowTitle("Settings Dialog")
        super().exec_()

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
        self.scrapeAllButton.clicked.connect(self.print_table)
        self.BRButton.clicked.connect(self.on_br_button_clicked)
        self.UDButton.clicked.connect(self.on_ud_button_clicked)
        self.ExportButton.clicked.connect(self.on_export_button_clicked)
        self.tableWidget.itemDoubleClicked.connect(self.on_table_widget_item_clicked)       
        self.tableWidget.itemSelectionChanged.connect(self.on_column_selected)
        self.settingsButton.clicked.connect(self.on_settings_button_clicked)
        self.CurrentListingButton.clicked.connect(self.on_current_listing_button_clicked)
        self.NewListingButton.clicked.connect(self.on_new_listing_button_clicked)
        self.RemoveListingButton.clicked.connect(self.on_remove_listing_button_clicked)  
    def on_ud_button_clicked(self):
        print("UlovDomov button clicked!")    
    def on_table_widget_item_clicked(self, item):
        url = item.text()
        if is_valid_url(url):
            try:
                print("Opening page: "+url)
                webbrowser.open('http://seznam.cz',new=0)
            except Exception as e:
                pass
            finally:
                print('done')
            # if webbrowser.get("firefox").open_new_tab("about:blank"):
            #     # If Firefox is responsive, open the URL in a new tab
            #     webbrowser.get("firefox").open_new_tab(url)
            # else:
            #     # If Firefox is not responsive, use a different browser
            #     webbrowser.get("chrome").open(url)
    def on_column_selected(self):
        if len(self.tableWidget.selectedItems())>1:
            selected_columns = list({index.column() for index in self.tableWidget.selectedIndexes()})
            self.data_table = self.data_table.sort_values(by=self.data_table.columns[selected_columns[0]])
            print('Sorting')
            self.print_table()
    def on_settings_button_clicked(self):
        print('Settings being opened')
        dialog = SettingsDialogWrapper(self)
        self.setEnabled(False)
        dialog.show()
        self.setEnabled(True)


class ScrapperApp(GuiLoader):
    def __init__(self):
        # Set necessary attributes and settings before creating the QGuiApplication instance
        QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
        QApplication.setAttribute(Qt.AA_UseSoftwareOpenGL)
        self.app = QApplication(sys.argv)
        super().__init__()
        self.init_variables()
        self.show()
        sys.exit(self.app.exec())
    
    def init_variables(self):
        """Internal variables are initialized here"""
        self._json_data_file_name = "config.json"
        #Tries to find json file
        try:
            with open(self._json_data_file_name, 'r') as json_file:
                loaded_list = json.load(json_file)     
        except:
            #Default values
            print('config.json not found setting default values')
            loaded_list = {'bez_realitky_url': "www.bezrealitky.cz",
                           'ulov_domov_url': "www.ulovdomov.cz",
                           'browser': 'firefox',
                           'is_silent': 0}
        self.__dict__.update(loaded_list)
    def save_config(self):
        loaded_list = {'bez_realitky_url': self.bez_realitky_url,
                           'ulov_domov_url': self.ulov_domov_url,
                           'browser': self.browser,
                           'is_silent': self.is_silent}
        print('saving')
        with open(self._json_data_file_name, 'w') as json_file:
            json.dump(loaded_list, json_file)
        print('Done')
    def on_br_button_clicked(self):
        print("BezRealitky button clicked!")
        try:
            self.bez_realitky_scraper = BezrealitkyScraper(browser=self.browser, web_page_link=self.bez_realitky_url, IS_SILENT=self.is_silent)
            self.data_table = self.bez_realitky_scraper.scraped_data.get_dataframe()
        except Exception as e:
            print('Error appealed during scraping')
        finally:    
            print('Closing browser')
            self.bez_realitky_scraper.driver.close()
        self.print_table()
    def on_export_button_clicked(self):
        print('Exporting table')
        self.remove_old_excels()
        self.data_table.to_excel(f"ScrapedData{get_current_datetime_string()}.xlsx")
    def on_current_listing_button_clicked(self):
        self.print_table(table = 0)
    def on_new_listing_button_clicked(self):
        self.load_old_excel()
        self.comparator = ScrapedDataComparator(self.data_table, self.old_data_table)
        self.print_table(table=1)
    def on_remove_listing_button_clicked(self):
        self.load_old_excel()
        self.comparator = ScrapedDataComparator(self.data_table, self.old_data_table)
        self.print_table(table=2)
    def print_table(self, table = 0):
        table_widget = self.tableWidget
        if table == 0:
            df_table = self.data_table
        elif table == 1:
            print('Setting new data: ')
            print(self.comparator.new_data)
            df_table = self.comparator.new_data
        elif table == 2:
            print('Setting removed data: ')
            print(self.comparator.missing_data)
            df_table = self.comparator.missing_data
            
        table_widget.setRowCount(df_table.shape[0])
        table_widget.setColumnCount(df_table.shape[1])
        table_widget.setHorizontalHeaderLabels(df_table.columns)

        for row in range(df_table.shape[0]):
            for col in range(df_table.shape[1]):
                value = str(df_table.iat[row, col])
                item = QTableWidgetItem(value)
                table_widget.setItem(row, col, item)
                
        table_widget.resizeColumnsToContents() 
    def set_progress_bar(self, percent:float):
        self.progressBar.setValue(percent)
    def remove_old_excels(self):
        files_to_remove = glob.glob(os.path.join('', "ScrapedData*.xlsx"))
        if len(files_to_remove) == 0:
            print("No files found matching the pattern.")
        else:
            # Confirm your intentions before removing the files
            print(f"Found {len(files_to_remove)} files matching the pattern:")
            for file_path in files_to_remove:
                print(file_path)
                os.remove(file_path)
            print("Files removed successfully.")
    def load_old_excel(self):
        files = glob.glob(os.path.join('', "ScrapedData*.xlsx"))
        if len(files)>1:
            print('Warning: multiple files found, selecting first of them')
            file = files[0]
        else:
            file = files[0]
        self.old_data_table = pd.read_excel(file, sheet_name=0)
        self.old_data_table = self.old_data_table.drop(self.old_data_table.columns[0], axis=1)
if __name__ == "__main__":
    window = ScrapperApp()
    

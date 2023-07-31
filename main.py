from pysideapp import ScrapperApp
import pandas as pd

def import_excel_to_dataframe(file_path):
    try:
        # Read the Excel file and load the specified sheet into a DataFrame
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error: Unable to import Excel table from '{file_path}'. Error details: {e}")
        return None

if __name__ =="__main__":
    table = import_excel_to_dataframe("Data/Bezrealitky2023-07-31-11-55-51.xlsx",)
    print(table)
    app = ScrapperApp(table)
    
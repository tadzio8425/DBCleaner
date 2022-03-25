import pandas as pd
import unidecode


class DBCleaner:
    def __init__(self, csv_name: str) -> None:
        self.df = pd.read_csv(csv_name, sep=";", encoding="latin-1")
        
        cols = self.df.columns
        self.df[cols] = self.df[cols].applymap(lambda x: unidecode.unidecode(str(x)))

    def delete_column(self, column_index: int):
        """Elimina una columna con un índice dado"""
        self.df.drop(columns=self.df.columns[column_index], inplace=True)
        
    def rename_columns(self, new_column_names: list):
        """Le cambia el nombre a todas las columnas del DataFrame"""
        self.df.columns = new_column_names

    def filter_column(self, column_name: str, separator: str):
        """Filtra una columna, dejando únicamente el primer elemento antes del separador provisto."""
        self.df[column_name] = self.df[column_name].apply(lambda row: str(row).split(separator)[0].strip())

    def filter_cellphone(self, column_name: str):
        """Filtra un número de telefono, tomando únicamente los primeros 10 digitos"""

        def filter_cell(row):
            cellphone = ""
            row = str(row)
            count = 0
            for char in row:
                if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] and count < 10:
                    cellphone += char
                count += 1
            return cellphone

        self.df[column_name] = self.df[column_name].apply(filter_cell)

    def strip_column(self, column_name: str):
        """Le remueve el espacio en blanco en los extremos a todos los elementos de una columna"""
        self.df[column_name] = self.df[column_name].apply(lambda row: str(row).strip())

    def save_as_csv(self, new_csv_name: str):
        """Almacena el DataFrame en un nuevo archivo CSV"""
        self.df.to_csv(new_csv_name, encoding="utf-8")



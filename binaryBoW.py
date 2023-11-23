from main import Main

file_path: str = 'DataSets/Dataset.xlsx'

excel_column = Main.read_excel(file_path, 'جملات')

# Proceed only if the excel_column is not None
if excel_column is not None:
    results = []
    for i, row in excel_column.items():
        char_presence = [1 if char in row else 0 for char in Main.combined_alphabet]
        results.append(char_presence)

Main.write_excel(file_path, results)
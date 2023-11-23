from collections import Counter
from main import Main


file_path = 'DataSets/Dataset_Normed.xlsx'

excel_column = Main.read_excel(file_path, 'جملات')
results = []

if excel_column is not None:
    for i, row in excel_column.items():
        char_counts = Counter(row)
        char_presence = [char_counts[char] / len(row) if char in row else 0 for char in Main.combined_alphabet]
        results.append(char_presence)
    Main.write_excel(file_path, results)
else:
    print("Couldn't find the sentences.")

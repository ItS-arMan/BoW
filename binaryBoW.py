from Main import Basic

file_path: str = 'DataSets/Dataset.xlsx'
binaryBoW = Basic()

excel_column = Basic.read_excel(binaryBoW, file_path, 'جملات')

# Proceed only if the excel_column is not None
if excel_column is not None:
    results = []
    for i, row in excel_column.items():
        char_presence = [1 if char in row else 0 for char in Basic.combined_alphabet]
        results.append(char_presence)

Basic.write_excel(binaryBoW, file_path, results)
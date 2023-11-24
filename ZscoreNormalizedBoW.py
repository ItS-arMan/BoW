import statistics
from collections import Counter
from main import Main

file_path = 'DataSets/Dataset_Normed_ZScore.xlsx'

excel_column = Main.read_excel(file_path, 'جملات')

# Proceed only if the excel_column is not None
if excel_column is not None:

    normalized_count_arrays = []
    results = []
    data_for_knn = []
    labels_for_knn = []

    for i, row in excel_column.items():
        char_counts = Counter(row)
        row_length = len(row)
        mean = statistics.mean(char_counts.values())
        stdev = statistics.stdev(char_counts.values())
        char_presence = [(char_counts[char] - mean) / stdev if stdev != 0 else 0 for char in Main.combined_alphabet]
        results.append(char_presence)

        if i in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
            data_for_knn.append(char_presence)
            labels_for_knn.append(i)

    Main.perform_knn(data_for_knn, labels_for_knn, results, 3, 'cosine')

    Main.write_excel(file_path, results)
else:
    print("Couldn't find the sentences.")

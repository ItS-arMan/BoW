from collections import Counter
from main import Main
from sklearn.neighbors import KNeighborsClassifier

file_path = 'DataSets/Dataset_Normed.xlsx'

excel_column = Main.read_excel(file_path, 'جملات')
if excel_column is not None:
    results = []
    data_for_knn = []
    labels_for_knn = []

    for i, row in excel_column.items():
        char_counts = Counter(row)
        char_presence = [char_counts[char] / len(row) if char in row else 0 for char in Main.combined_alphabet]
        results.append(char_presence)

        if i in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
            data_for_knn.append(char_presence)
            labels_for_knn.append(i)

    Main.perform_knn(data_for_knn, labels_for_knn, results, 1, 'euclidean')
    Main.write_excel(file_path, results)

else:
    print("Couldn't find the sentences.")

if excel_column is not None:
    for i, row in excel_column.items():
        char_counts = Counter(row)
        char_presence = [char_counts[char] / len(row) if char in row else 0 for char in Main.combined_alphabet]

        results.append(char_presence)

    Main.write_excel(file_path, results)

else:
    print("Couldn't find the sentences.")

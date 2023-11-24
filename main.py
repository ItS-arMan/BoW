import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


class Main:
    arabic_alphabet = ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع',
                       'غ',
                       'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']
    persian_alphabet = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض',
                        'ط',
                        'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']
    combined_alphabet = list(set(arabic_alphabet + persian_alphabet))

    combined_alphabet.sort()

    @staticmethod
    def read_excel(file_path, column_name):
        """

        :param str file_path: File path of the Excel Data set
        :param str column_name: name of the column that contains the strings
        :return:
        """
        try:
            data = pd.read_excel(file_path)

            column_data = data[column_name].astype(str)  #

            return column_data

        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None



    @staticmethod
    def perform_knn(data, labels, results, neighbors, metric):
        knn = KNeighborsClassifier(n_neighbors=neighbors, metric=metric)
        knn.fit(data, labels)

        # Predictions for specified rows
        for row_num in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
            index = row_num - 1  # Adjust index to start from 0
            prediction = knn.predict([results[index]])[0]
            print(f'K-NN Prediction for row {row_num}: {prediction}')

    @staticmethod
    def write_excel(file_path, results):
        """
        :param str file_path: File path of the Excel Data set
        :param List results: Final result contains result of the BoW
        """
        results_df = pd.DataFrame(results, columns=Main.combined_alphabet)

        data = pd.read_excel(file_path)

        final_data = pd.concat([data, results_df], axis=1)

        final_data.to_excel(file_path, index=False)

        print(f"Results has been successfully written to '{file_path}'.")

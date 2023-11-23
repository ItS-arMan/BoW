import pandas as pd


class Main:
    arabic_alphabet = ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع',
                       'غ',
                       'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']
    persian_alphabet = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض',
                        'ط',
                        'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']
    combined_alphabet = list(set(arabic_alphabet + persian_alphabet))
    combined_alphabet.sort()  # Sort the combined alphabet

    @staticmethod
    def read_excel(file_path, column_name):
        """

        :param str file_path: File path of the Excel Data set
        :param str column_name: name of the column that contains the strigns
        :return:
        """
        try:
            # Read the Excel file
            data = pd.read_excel(file_path)

            # Get the column data
            column_data = data[column_name].astype(str)  # Ensure the column is treated as strings

            return column_data

        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def write_excel(file_path, results):
        """
        :param str file_path: File path of the Excel Data set
        :param List results: Final result contains result of the BoW
        """
        # Create a DataFrame with the results
        results_df = pd.DataFrame(results, columns=Main.combined_alphabet)

        # Read the original Excel file again to append results to it
        data = pd.read_excel(file_path)

        # Concatenate the original data with the results (starting from the second column)
        final_data = pd.concat([data, results_df], axis=1)

        # Write the updated data to the same Excel file starting from column 2
        final_data.to_excel(file_path, index=True)

        print(f"Results has been successfully written to '{file_path}'.")

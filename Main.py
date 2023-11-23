import pandas as pd


class Basic:
    arabic_alphabet = ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع',
                       'غ',
                       'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']
    persian_alphabet = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض',
                        'ط',
                        'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']
    combined_alphabet = list(set(arabic_alphabet + persian_alphabet))
    combined_alphabet.sort()  # Sort the combined alphabet

    def read_excel(self, file_path, column_name):
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

    def write_excel(self, file_path, results):

        # Create a DataFrame with the results
        results_df = pd.DataFrame(results, columns=Basic.combined_alphabet)

        # Read the original Excel file again to append results to it
        data = pd.read_excel(file_path)

        # Concatenate the original data with the results (starting from the second column)
        final_data = pd.concat([data, results_df], axis=1)

        # Write the updated data to the same Excel file starting from column 2
        final_data.to_excel(file_path, index=True)

        print(f"Results has been successfully written to '{file_path}'.")


def __init__(self):
    pass

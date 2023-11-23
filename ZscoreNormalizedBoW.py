import statistics
import pandas as pd
from collections import Counter

# Function to read a column from Excel and return its data as an array
def read_excel_column(file_path, column_name):
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


# Read the specified column containing Arabic and Persian characters from the Excel file
file_path = 'Dataset_Normed_ZScore.xlsx'

excel_column = read_excel_column(file_path, 'جملات')

# Proceed only if the excel_column is not None
if excel_column is not None:
    # Create the combined alphabet array (union of Persian and Arabic alphabets)
    arabic_alphabet = ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ',
                       'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']
    persian_alphabet = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط',
                        'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']

    combined_alphabet = list(set(arabic_alphabet + persian_alphabet))
    combined_alphabet.sort()  # Sort the combined alphabet

    #create_normalized_count_array(excel_column, combined_alphabet)
    normalized_count_arrays = []
    # for row in combined_alphabet:
    #     char_counts = Counter(row)
    #     row_length = len(row)
    #     mean = statistics.mean(char_counts.values())
    #     stdev = statistics.stdev(char_counts.values())
    #     z_scores = [(char_counts[char] - mean) / stdev if stdev != 0 else 0 for char in combined_alphabet]
    #     normalized_count_arrays.append(z_scores)

    results = []
    for i, row in excel_column.items():
        char_counts = Counter(row)
        row_length = len(row)
        mean = statistics.mean(char_counts.values())
        stdev = statistics.stdev(char_counts.values())
        char_presence = [(char_counts[char] - mean) / stdev if stdev != 0 else 0 for char in combined_alphabet]
        results.append(char_presence)

    # Create a DataFrame with the results
    results_df = pd.DataFrame(results, columns=combined_alphabet)

    # Read the original Excel file again to append results to it
    data = pd.read_excel(file_path)

    # Concatenate the original data with the results (starting from the second column)
    final_data = pd.concat([data, results_df], axis=1)

    # Write the updated data to the same Excel file starting from column 2
    final_data.to_excel(file_path, index=False)

    print(f"Results written to '{file_path}' in columns 2 onwards.")
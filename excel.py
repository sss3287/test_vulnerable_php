import pandas as pd
import os

excel_file_path = '/Users/sohan_saimbhi/Desktop/Research Coop/php/vulnerabilities.xlsx'
column_name = 'CodeSnippet'
df = pd.read_excel(excel_file_path)
output_folder = '/Users/sohan_saimbhi/Desktop/Research Coop/php/codes_final'
os.makedirs(output_folder, exist_ok=True)

# Loop through the values in the specified column and save each value as a separate file
for index, value in enumerate(df[column_name], start=1):
    file_name = f"{index}.php"
    file_path = os.path.join(output_folder, file_name)
    
    with open(file_path, 'w') as file:
        file.write(str(value))
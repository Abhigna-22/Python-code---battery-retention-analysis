import pandas as pd
from google.colab import files


# Replace 'your_file.csv' with the actual path to your CSV file
uploaded = files.upload()
file_path = next(iter(uploaded)) # Get the name of the uploaded file


# Read the CSV file, skipping the first 17 rows and setting the 18th row as the header
df = pd.read_csv(file_path, skiprows=17, sep=',')

# Multiply the third column (index 2) by -1
df.iloc[:, 2] = df.iloc[:, 2] * -1

# Select only the first three columns (indices 0, 1, and 2) and reorder them
df = df.iloc[:, [1, 2, 0]]

# Get the number of data rows
row_count = len(df)

# Remove the header
df = df.reset_index(drop=True)

# Create a new row with the row count in the first column and empty strings in the rest
new_row = pd.DataFrame([[row_count] + [''] * (len(df.columns) - 1)], columns=df.columns)

# Concatenate the new row with the original DataFrame
df = pd.concat([new_row, df], ignore_index=True)

# Display the first few rows and the columns to verify
print(df.head())
print(df.columns)

# Get the filename from the user
output_filename_base = input("Enter the desired filename for the downloaded file (without extension): ")
output_filename = f"{output_filename_base}.eis"

# Download the DataFrame as a tab-separated file with the .eis extension, without including the header
df.to_csv(output_filename, index=False, sep='\t', header=False, quoting=3) # quoting=3 means quote_none

print(f"DataFrame successfully saved as {output_filename}")

# Offer the file for download
files.download(output_filename)

# Read the first few lines of the uploaded file to understand its structure
with open(file_path, 'r') as f:
    for i in range(20): # Read and print the first 20 lines
        print(f.readline().strip())

from google.colab import files

# Get the filename from the user
output_filename_base = input("Enter the desired filename for the downloaded file (without extension): ")
output_filename = f"{output_filename_base}.eis"

# Download the DataFrame as a tab-separated file with the .eis extension, without including the header
df.to_csv(output_filename, index=False, sep='\t', header=False, quoting=3) # quoting=3 means quote_none

print(f"DataFrame successfully saved as {output_filename}")

# Offer the file for download
files.download(output_filename)

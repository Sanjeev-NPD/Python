import re
import csv
import os

def extract_functions(c_file_path):
    if not os.path.isfile(c_file_path):
        raise FileNotFoundError(f"The file {c_file_path} does not exist or is not a file.")
    
    function_pattern = re.compile(r'\b\w+\s+\w+\s*\([^)]*\)\s*\{')
    
    functions = []
    
    try:
        with open(c_file_path, 'r') as file:
            content = file.read()
            
            matches = function_pattern.findall(content)
            
            for match in matches:
                func_name = match.split('(')[0].strip().split()[-1]
                functions.append(func_name)
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    
    return functions

def save_to_csv(functions, c_file_path):
    base, _ = os.path.splitext(c_file_path)
    output_csv_path = f"{base}_functions.csv"
    
    try:
        with open(output_csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Function Name'])
            for func in functions:
                writer.writerow([func])
        print(f"Extracted functions saved to {output_csv_path}")
    except IOError as e:
        print(f"An error occurred while writing to the CSV file: {e}")

# Example usage
try:
    c_file_path = input("Enter the path to the .c file: ")
    functions = extract_functions(c_file_path)
    save_to_csv(functions, c_file_path)
except Exception as e:
    print(f"An error occurred: {e}")

# import pandas as pd

# # Function to analyze the DTC message
# def analyze_dtc(dtc_string):
#     # Read the layout CSV file
#     layout_df = pd.read_csv('layout.csv')
#     # Read the DTC CSV file
#     dtc_df = pd.read_csv('dtc.csv')

#     # Split the input string
#     dtc_id, message = dtc_string.split(":")
#     message_bytes = message.strip().split()  # Split message into bytes

#     # Initialize a list to store results
#     results = []

#     # Analyze each byte in the message
#     for byte_index, byte_value in enumerate(message_bytes):
#         byte_int = int(byte_value, 16)  # Convert hex to int
#         byte_binary = f"{byte_int:08b}"  # Convert to binary string

#         # Check each bit in the byte
#         for bit_index in range(8):
#             if byte_binary[bit_index] == '1':  # If the bit is set
#                 # Get the corresponding value from the layout
#                 layout_value = layout_df.iloc[byte_index][f'bit{7 - bit_index}']  # Corrected indexing
#                 results.append(float(layout_value))  # Store as float for range checking

#     # Display results
#     print(f"DTC Code ID: {dtc_id.strip()}")
#     print("Set Values:")
#     for result in results:
#         print(f" - {result}")

#     # Display corresponding data from dtc.csv based on the layout values
#     print("\nCorresponding Data from DTC CSV:")
#     for result in results:
#         # Check against the layout ranges in dtc_df
#         for index, row in dtc_df.iterrows():
#             layout_range = row['Layout']
#             if '-' in layout_range:  # Check if it's a range
#                 min_value, max_value = map(float, layout_range.split('-'))
#                 if min_value <= result <= max_value:
#                     print(f" - Name: {row['Name']}, Data: {row['Data']}")
#             else:  # If it's a single value
#                 if float(layout_range) == result:
#                     print(f" - Name: {row['Name']}, Data: {row['Data']}")

# # Main program
# if __name__ == "__main__":
#     user_input = input("Enter the DTC string (e.g., '4CB:80 C0 00 00 00 00 00 27'): ")
#     analyze_dtc(user_input)


# without data coloumn information:

# import pandas as pd

# # Function to analyze the DTC message
# def analyze_dtc(dtc_string):
#     # Read the layout CSV file
#     layout_df = pd.read_csv('layout.csv')
#     # Read the DTC CSV file
#     dtc_df = pd.read_csv('dtc.csv')

#     # Split the input string
#     dtc_id, message = dtc_string.split(":")
#     dtc_id = dtc_id.strip().lower()  # Convert ID to lowercase for case insensitivity
#     message_bytes = message.strip().split()  # Split message into bytes

#     # Initialize a list to store results
#     results = []

#     # Analyze each byte in the message
#     for byte_index, byte_value in enumerate(message_bytes):
#         byte_int = int(byte_value, 16)  # Convert hex to int
#         byte_binary = f"{byte_int:08b}"  # Convert to binary string

#         # Check each bit in the byte
#         for bit_index in range(8):
#             if byte_binary[bit_index] == '1':  # If the bit is set
#                 # Get the corresponding value from the layout
#                 layout_value = layout_df.iloc[byte_index][f'bit{7 - bit_index}']  # Corrected indexing
#                 results.append(float(layout_value))  # Store as float for range checking

#     # Display results
#     print(f"DTC Code ID: {dtc_id.strip()}")
#     print("Set Values:")
#     for result in results:
#         print(f" - {result}")

#     # Display corresponding names from dtc.csv based on the layout values
#     print("\nCorresponding Names from DTC CSV:")
#     for index, row in dtc_df.iterrows():
#         row_id = row['ID'].strip().lower()  # Convert ID to lowercase for case insensitivity
#         if row_id == dtc_id:  # Check if ID matches
#             layout_range = row['Layout']
#             if '-' in layout_range:  # Check if it's a range
#                 min_value, max_value = map(float, layout_range.split('-'))
#                 # Check if any of the set values fall within the range
#                 for result in results:
#                     if min_value <= result <= max_value:
#                         print(f" - Name: {row['Name']}")
#             else:  # If it's a single value
#                 for result in results:
#                     if float(layout_range) == result:
#                         print(f" - Name: {row['Name']}")

# # Main program
# if __name__ == "__main__":
#     user_input = input("Enter the DTC string (e.g., '4CB:80 C0 00 00 00 00 00 27'): ")
#     analyze_dtc(user_input)
######################################################################

import tkinter as tk
from tkinter import filedialog
import pandas as pd

class DTCAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DTC Analyzer")
        self.root.geometry("1200x600")

        self.dtc_file = None
        self.layout_file = None

        # Create the main application layout
        self.create_main_layout()

    def create_main_layout(self):
        # Left frame for input and file selection
        left_frame = tk.Frame(self.root, width=600, padx=10, pady=10)
        left_frame.pack(side="left", fill="both", expand=False)

        input_label = tk.Label(left_frame, text="Enter the DTC string (e.g., '4CB:80 C0 00 00 00 00 00 27'):")
        input_label.pack(pady=5)

        self.dtc_entry = tk.Entry(left_frame, width=40)                   
        self.dtc_entry.pack(pady=10)

        # DTC and Layout buttons in the same row
        button_frame = tk.Frame(left_frame)
        button_frame.pack(pady=20)

        select_dtc_button = tk.Button(button_frame, text="Select DTC File", command=self.select_dtc_file)
        select_dtc_button.grid(row=0, column=0, padx=20)

        select_layout_button = tk.Button(button_frame, text="Select Layout File", command=self.select_layout_file)
        select_layout_button.grid(row=0, column=1, padx=20)

        # Analyze button below, centered
        analyze_button = tk.Button(left_frame, text="Analyze", command=self.analyze_dtc)
        analyze_button.pack(pady=20)

        # Right frame for displaying results
        self.right_frame = tk.Frame(self.root, width=600, padx=10, pady=10, bg="white")
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.result_label = tk.Label(self.right_frame, text="Results will be displayed here.", anchor="nw", justify="left", bg="white")
        self.result_label.pack(padx=10, pady=10, fill="both", expand=True)

    def select_dtc_file(self):
        self.dtc_file = filedialog.askopenfilename(title="Select DTC CSV File", filetypes=[("CSV files", "*.csv")])
        if self.dtc_file:
            print(f"DTC File Selected: {self.dtc_file}")  # Removed messagebox confirmation

    def select_layout_file(self):
        self.layout_file = filedialog.askopenfilename(title="Select Layout CSV File", filetypes=[("CSV files", "*.csv")])
        if self.layout_file:
            print(f"Layout File Selected: {self.layout_file}")  # Removed messagebox confirmation

    def analyze_dtc(self):
        if not self.dtc_file or not self.layout_file:
            print("Please select both the DTC and Layout files before analyzing.")  # Removed messagebox error
            return

        dtc_string = self.dtc_entry.get().strip()
        if not dtc_string:
            print("Please enter a valid DTC string.")  # Removed messagebox error
            return

        try:
            # Read the CSV files
            layout_df = pd.read_csv(self.layout_file)
            dtc_df = pd.read_csv(self.dtc_file)

            # Split the input string
            dtc_id, message = dtc_string.split(":")
            dtc_id = dtc_id.strip().lower()
            message_bytes = message.strip().split()

            # Initialize a list to store results
            results = []

            # Analyze each byte in the message
            for byte_index, byte_value in enumerate(message_bytes):
                byte_int = int(byte_value, 16)
                byte_binary = f"{byte_int:08b}"

                for bit_index in range(8):
                    if byte_binary[bit_index] == '1':
                        layout_value = layout_df.iloc[byte_index][f'bit{7 - bit_index}']
                        results.append(float(layout_value))

            # Prepare results for display
            result_text = f"DTC Code ID: {dtc_id}\nSet Values:\n"
            for result in results:
                result_text += f" - {result}\n"

            result_text += "\nCorresponding Names from DTC CSV:\n"
            for index, row in dtc_df.iterrows():
                row_id = row['ID'].strip().lower()
                if row_id == dtc_id:
                    layout_range = row['Layout']
                    if '-' in layout_range:
                        min_value, max_value = map(float, layout_range.split('-'))
                        for result in results:
                            if min_value <= result <= max_value:
                                result_text += f" - Name: {row['Name']}\n"
                    else:
                        for result in results:
                            if float(layout_range) == result:
                                result_text += f" - Name: {row['Name']}\n"

            self.display_results(result_text)

        except Exception as e:
            print(f"An error occurred: {e}")  # Removed messagebox error

    def display_results(self, result_text):
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DTCAnalyzerApp(root)
    root.mainloop()



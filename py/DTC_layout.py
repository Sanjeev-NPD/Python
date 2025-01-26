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

import pandas as pd

# Function to analyze the DTC message
def analyze_dtc(dtc_string):
    # Read the layout CSV file
    layout_df = pd.read_csv('layout.csv')
    # Read the DTC CSV file
    dtc_df = pd.read_csv('dtc.csv')

    # Split the input string
    dtc_id, message = dtc_string.split(":")
    dtc_id = dtc_id.strip().lower()  # Convert ID to lowercase for case insensitivity
    message_bytes = message.strip().split()  # Split message into bytes

    # Initialize a list to store results
    results = []

    # Analyze each byte in the message
    for byte_index, byte_value in enumerate(message_bytes):
        byte_int = int(byte_value, 16)  # Convert hex to int
        byte_binary = f"{byte_int:08b}"  # Convert to binary string

        # Check each bit in the byte
        for bit_index in range(8):
            if byte_binary[bit_index] == '1':  # If the bit is set
                # Get the corresponding value from the layout
                layout_value = layout_df.iloc[byte_index][f'bit{7 - bit_index}']  # Corrected indexing
                results.append(float(layout_value))  # Store as float for range checking

    # Display results
    print(f"DTC Code ID: {dtc_id.strip()}")
    print("Set Values:")
    for result in results:
        print(f" - {result}")

    # Display corresponding names from dtc.csv based on the layout values
    print("\nCorresponding Names from DTC CSV:")
    for index, row in dtc_df.iterrows():
        row_id = row['ID'].strip().lower()  # Convert ID to lowercase for case insensitivity
        if row_id == dtc_id:  # Check if ID matches
            layout_range = row['Layout']
            if '-' in layout_range:  # Check if it's a range
                min_value, max_value = map(float, layout_range.split('-'))
                # Check if any of the set values fall within the range
                for result in results:
                    if min_value <= result <= max_value:
                        print(f" - Name: {row['Name']}")
            else:  # If it's a single value
                for result in results:
                    if float(layout_range) == result:
                        print(f" - Name: {row['Name']}")

# Main program
if __name__ == "__main__":
    user_input = input("Enter the DTC string (e.g., '4CB:80 C0 00 00 00 00 00 27'): ")
    analyze_dtc(user_input)

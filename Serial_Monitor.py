import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import serial
import serial.tools.list_ports
import threading

# Function to list available COM ports
def get_com_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

# Function to update the list of available COM ports
def update_com_ports():
    com_ports = get_com_ports()
    com_port_combobox['values'] = com_ports
    if com_ports:
        com_port_combobox.current(0)

# Function to handle serial communication
def start_communication():
    com_port = com_port_combobox.get()
    baud_rate = int(baud_rate_combobox.get())
    
    try:
        ser = serial.Serial(com_port, baud_rate, timeout=1)
        output_text.insert(tk.END, f"Connected to {com_port} at {baud_rate} baud\n")
        
        # Function to read data from the serial port
        def read_from_serial():
            while True:
                if ser.in_waiting > 0:
                    data = ser.readline().decode('utf-8').strip()
                    if data:
                        output_text.insert(tk.END, f"Received: {data}\n")
                        output_text.yview(tk.END)
                
        # Start reading thread
        threading.Thread(target=read_from_serial, daemon=True).start()
        
        # Send data to serial port
        def send_data():
            message = input_text.get()
            if message:
                ser.write(message.encode('utf-8'))
                output_text.insert(tk.END, f"Sent: {message}\n")
                input_text.delete(0, tk.END)
                
        # Button to send data
        send_button.config(command=send_data)

    except Exception as e:
        output_text.insert(tk.END, f"Error: {e}\n")

# Function to save log to a file
def save_log():
    log_data = output_text.get(1.0, tk.END)  # Get all text from output area
    
    # Ask user where to save the log file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    
    if file_path:
        with open(file_path, 'w') as file:
            file.write(log_data)
        output_text.insert(tk.END, f"Log saved to {file_path}\n")

# Create the main window
window = tk.Tk()
window.title("UART Serial Monitor")

# Get the screen width and height of the laptop
screen_width = 1920
screen_height = 1080

# Set the window size to occupy 80% of the screen size
window.geometry(f"{int(screen_width * 0.8)}x{int(screen_height * 0.8)}")

# Create a frame for controls (COM port, Baud rate, etc.)
controls_frame = tk.Frame(window)
controls_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Create a frame for output display (Serial Monitor)
output_frame = tk.Frame(window)
output_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Configure grid column weight for resizing (5:95 ratio)
window.grid_columnconfigure(0, weight=1)   # 5% for controls
window.grid_columnconfigure(1, weight=19)  # 95% for output display

# Configure grid row weight for resizing
window.grid_rowconfigure(0, weight=1)      # Ensure the output fills the height

# Label for COM Port
com_port_label = tk.Label(controls_frame, text="Select COM Port:", font=("Arial", 12))
com_port_label.pack(pady=10)

# Combobox for COM Ports
com_port_combobox = ttk.Combobox(controls_frame, width=20)
com_port_combobox.pack(pady=10)

# Label for Baud Rate
baud_rate_label = tk.Label(controls_frame, text="Select Baud Rate:", font=("Arial", 12))
baud_rate_label.pack(pady=10)

# Combobox for Baud Rates
baud_rate_combobox = ttk.Combobox(controls_frame, values=[9600, 115200, 19200, 38400, 57600, 1152000], width=10)
baud_rate_combobox.set(9600)  # Default value
baud_rate_combobox.pack(pady=10)

# Button to update COM ports list
update_button = tk.Button(controls_frame, text="Update COM Ports", command=update_com_ports, font=("Arial", 12))
update_button.pack(pady=10)

# Button to start communication
start_button = tk.Button(controls_frame, text="Start Communication", command=start_communication, font=("Arial", 12))
start_button.pack(pady=20)

# Output text box to display received data
output_text = tk.Text(output_frame, wrap=tk.WORD, font=("Arial", 14))
output_text.pack(pady=10, fill=tk.BOTH, expand=True)

# Input field for sending data
input_text = tk.Entry(controls_frame, width=20, font=("Arial", 16))
input_text.pack(pady=10)

# Send button
send_button = tk.Button(controls_frame, text="Send", font=("Arial", 12))
send_button.pack(pady=10)

# Save Log button
save_button = tk.Button(controls_frame, text="Save Log", command=save_log, font=("Arial", 12))
save_button.pack(pady=10)

# Initial update of COM ports
update_com_ports()

# Run the GUI loop
window.mainloop()

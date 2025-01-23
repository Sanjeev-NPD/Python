import serial
import time

# Configure serial port
serial_port = "COM3"  # Update with your PC's COM port
baud_rate = 9600
hex_file = "path/to/your/hexfile.hex"

def send_hex_file():
    try:
        # Open serial port
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        print(f"Opened {serial_port} successfully.")

        # Open and read hex file
        with open(hex_file, 'r') as file:
            for line in file:
                line = line.strip()  # Remove extra whitespace
                if line:  # Send non-empty lines
                    ser.write(line.encode() + b'\n')  # Send line with newline
                    time.sleep(0.01)  # Small delay to ensure PIC can process
                    response = ser.readline().decode().strip()
                    print(f"Sent: {line}, Received: {response}")
        
        print("File transfer complete.")
        ser.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_hex_file()

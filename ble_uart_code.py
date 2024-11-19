import board
import busio

# Initialize UART
print("initializing uart")
uart = busio.UART(board.TX, board.RX, baudrate=9600)  # Adjust TX/RX pins as needed

# Basic send/receive example
def send_command(cmd):
    uart.write(cmd.encode() + b'\n')

def read_response():
    if uart.in_waiting:
        return uart.read()
    return None

print("sending the command many times now... go run bleak_eval_client.py and type something in the command line!!")
# Example usage
while True:
    send_command("AT")  # Send AT command
    response = read_response()
    if response:
        print(f"Received: {response}")
        # Echo back what was received
        send_command(f"Echo: {response.decode()}")

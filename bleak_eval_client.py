import asyncio
from bleak import BleakScanner, BleakClient

# Nordic UART Service UUID
UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
# Nordic UART Service characteristics
UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"  # Write
UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"  # Read/Notify

async def main():
    print("Scanning for Bluefruit UART Friend...")
    devices = await BleakScanner.discover()
    print("All discovered devices:")
    for d in devices:
        print(f"Name: {d.name}, Address: {d.address}")

    # Find your Bluefruit device
    uart_device = None
    for device in devices:
        # Adjust this name to match your device
        if device.name and "Bluefruit" in device.name:
            uart_device = device
            break

    if not uart_device:
        print("No Bluefruit device found")
        return

    async with BleakClient(uart_device.address) as client:
        print(f"Connected to {uart_device.name}")

        # Handle incoming data
        def handle_rx(sender, data):
            print(f"Received: {data.decode()}")

        # Start listening for incoming data
        await client.start_notify(UART_TX_CHAR_UUID, handle_rx)

        print("Ready to send messages. Type your message and press Enter.")
        print("Press Ctrl+C to exit.")

        while True:
            try:
                # Get input from user
                message = input("> ")
                # Send it to the Bluefruit
                await client.write_gatt_char(UART_RX_CHAR_UUID,
                                             (message + '\n').encode())
            except KeyboardInterrupt:
                break

        await client.stop_notify(UART_TX_CHAR_UUID)


# Run the script
asyncio.run(main())
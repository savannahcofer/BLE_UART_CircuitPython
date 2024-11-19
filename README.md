# BLE UART to Mac using CircuitPython
Starter code for connect the Bluefruit UART Friend to MacOS using CircuitPython

We are working with the Bluefruit UART Friend (https://www.adafruit.com/product/2479) and providing some simple code to connect the UART friend to your computer

The standard documentation using Arduino (.h and .cpp) is here: https://github.com/adafruit/Adafruit_BluefruitLE_nRF51

The Adafruit documentation shows the CircuitPython implementation, although the client end only works with devices like Raspberry Pi that support _bleio package which uses native BLE capability and cannot run on MacOS computer: https://learn.adafruit.com/circuitpython-ble-libraries-on-any-computer/ble-uart-example

_bleio documentaiton: https://docs.circuitpython.org/en/latest/shared-bindings/_bleio/

This repo contains two files:
ble_uart_code.py, which should be loaded as code.py to your CircuitPython supported device
bleak_eval_client.py, which you can run from your computer. Make sure you remember to pip3 install bleak before running.

First, load the ble_uart_code.py to the device to start advertising (streaming the test "AT") over and over again.
Then, run bleak_eval_client.py from your computer and see if it can detect a UART device. You can then send messages to the paired device by typing in the computer terminal and it will echo the command back to you.

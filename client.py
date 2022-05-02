import sys
import time
import socket

FILE = 'status.txt'
SERVER = '127.0.0.1', 54321

def running():
    is_running = True
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_s:
        while is_running:
            try:
                with open(FILE, 'r') as f:
                    lines = f.readlines()
                    line = [lines.rstrip() for lines in lines]   # delete \n
                    print(line)
                    message = (' '.join(str(i) for i in line))   # list to str
                    is_numeric = message.replace(" ", "")
                    if is_numeric.isnumeric():  # if the input data is correct
                        data = message.encode()
                        client_s.sendto(data, SERVER)
                        time_sleep()
                    else:
                        print("Input data is wrong")
                        time_sleep()
                        is_running = False
            except FileNotFoundError as e:
                print(e)
                is_running = False


def time_sleep():
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        print("Sending data is closed")
        sys.exit()


if __name__ == "__main__":
    running()


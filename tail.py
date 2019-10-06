import time

def logger(file_name, interval = 0.1):
    with open(file_name) as file:
        file.readlines()

        while True:
            new_line = file.readline().strip()
            if new_line: yield new_line

            time.sleep(interval)

import time

def logger(file_name, interval = 0.1):
    """
    A generator that returns any new lines added to a file.
    """

    # Open the file.
    with open(file_name) as file:
        # Read any already existing lines.
        file.readlines()

        # Constantly check for new line.
        while True:
            # Attempt to get a newline, and remove any whitespace.
            new_line = file.readline().strip()
            
            # If the attempt is successful, send the new line.
            if new_line: yield new_line

            # Wait some time.
            time.sleep(interval)
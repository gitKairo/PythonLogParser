import re
from collections import Counter


# Ask user for file path to the log file
log_file_path = input("Please enter the path to your web server log file: ")

# Regular expression pattern to match each component of the log entry
log_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+)'

# Compile the regular expression
log_regex = re.compile(log_pattern)

# Open the log file in read mode
with open(log_file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        match = log_regex.match(line)
        if match:
            ip, timestamp, request, status_code, size = match.groups()
            print(f"IP: {ip}, Timestamp: {timestamp}, Request: {request}, Status Code: {status_code}, Size: {size}")


            

# Initialize a Counter object to hold status code frequencies
status_code_counter = Counter()

# Open the log file in read mode
with open(log_file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        match = log_regex.match(line)
        if match:
            ip, timestamp, request, status_code, size = match.groups()
            # Increment the counter for this status code
            status_code_counter[status_code] += 1

# Print the status code frequencies
print("\nStatus Code Frequencies:")
for code, count in status_code_counter.items():
    print(f"Status Code {code}: {count} occurrences")
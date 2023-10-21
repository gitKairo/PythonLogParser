# Web Server Log Parser

## Overview

This Python script serves as a basic web server log parser. It reads a log file, extracts relevant information from each entry, and performs a simple analysis to count the frequency of HTTP status codes. This tool can be useful in a DevOps context for monitoring and troubleshooting web applications.

## Features

- Reads a web server log file line by line.
- Parses important data such as IP address, timestamp, request type, and status codes.
- Counts the frequency of each HTTP status code encountered in the log file.

## Usage

1. Download or clone this repository.
2. Run the script using Python 3.x.

    ```bash
    python logparser.py
    ```

3. When prompted, enter the full path to the log file you wish to analyze.

## Output

The script will output the parsed log entries in the following format:

IP: [IP Address], Timestamp: [Timestamp], Request: [HTTP Request], Status Code: [HTTP Status Code], Size: [Response Size]

At the end, it will display the frequency of each HTTP status code found in the log file.

## Dependencies

- Python 3.x
- `re` library for regular expressions
- `collections` library for counting occurrences

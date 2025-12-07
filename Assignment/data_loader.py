import csv
import sys

def load_frequencies(file_path):
    """
    Reads the CSV file containing letters and frequencies.
    Returns a dictionary {letter: frequency}.
    """
    data = {}
    try:
        # Open file with utf-8 encoding to handle Greek characters correctly
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    # Strip whitespace from letter and convert frequency to int
                    letter = row[0].strip()
                    try:
                        frequency = int(row[1].strip())
                        data[letter] = frequency
                    except ValueError:
                        print(f"Warning: Could not parse frequency for line: {row}")
                        continue
        print(f"Successfully loaded {len(data)} items from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
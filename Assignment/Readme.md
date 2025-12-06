# Assignment - Fano Coding

This project implements the Fano coding algorithm in Python to process character frequencies from the Greek Constitution text. It calculates probabilities, entropy, generates binary codes, and computes the average codeword length.

## Files Description

* **main.py**: The entry point of the application. Orchestrates the flow of execution.
* **data_loader.py**: Handles reading and parsing the `freq.csv` file.
* **probabilities.py**: Calculates the probability of occurrence for each character.
* **entropy.py**: Computes the Shannon Entropy of the source.
* **fano_coding.py**: Implements the recursive Fano algorithm to generate binary codes.
* **metrics.py**: Calculates the average codeword length based on probabilities and code lengths.
* **freq.csv**: Input data containing characters and their frequencies.

## Prerequisites

* Python 3.x

## How to Run

1.  Ensure all `.py` files and `freq.csv` are in the same directory.
2.  Open a terminal/command prompt.
3.  Run the main script:
    ```bash
    python main.py
    ```

## Output Explanation

The program will output:
1.  **Probabilities**: The calculated probability for every Greek letter found in the file.
2.  **Entropy**: The theoretical lower bound for the average number of bits per symbol.
3.  **Fano Codes**: The resulting binary code for each letter, sorted by probability.
4.  **Average Length**: The actual average bits per symbol achieved by the Fano code.

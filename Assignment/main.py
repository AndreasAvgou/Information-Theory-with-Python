import data_loader
import probabilities
import entropy
import fano_coding
import metrics

def main():
    print("--- Starting Assignment Execution ---")

    # 1. Load Data
    filename = "freq.csv"
    print(f"\n[Step 1] Loading data from {filename}...")
    freq_data = data_loader.load_frequencies(filename)
    
    # 2. Calculate Probabilities
    print("\n[Step 2] Calculating probabilities...")
    probs = probabilities.calculate_probabilities(freq_data)
    
    # Display Probabilities
    print(f"{'Letter':<10} | {'Count':<10} | {'Probability':<10}")
    print("-" * 35)
    for letter, p in probs.items():
        count = freq_data[letter]
        print(f"{letter:<10} | {count:<10} | {p:.6f}")

    # 3. Calculate Entropy
    print("\n[Step 3] Calculating Entropy...")
    H = entropy.calculate_entropy(probs)
    print(f"Entropy (H): {H:.6f} bits/symbol")

    # 4. Fano Coding
    print("\n[Step 4] Generating Fano Codes...")
    # Sort probabilities descending for Fano algorithm
    sorted_probs = sorted(probs.items(), key=lambda x: x[1], reverse=True)
    codes = fano_coding.fano_encoding(sorted_probs)
    
    print(f"{'Letter':<10} | {'Probability':<12} | {'Fano Code':<15} | {'Length':<5}")
    print("-" * 50)
    for letter, prob in sorted_probs:
        c = codes[letter]
        print(f"{letter:<10} | {prob:.6f}       | {c:<15} | {len(c):<5}")

    # 5. Average Length
    print("\n[Step 5] Calculating Average Codeword Length...")
    L = metrics.calculate_average_length(probs, codes)
    print(f"Average Length (L): {L:.6f} bits/symbol")

    # Efficiency (Optional but good to have)
    efficiency = (H / L) * 100 if L > 0 else 0
    print(f"Coding Efficiency: {efficiency:.2f}%")

    print("\n--- Execution Finished ---")

if __name__ == "__main__":
    main()
import information
import entropy
import joint_probs
import huffman
import fano
import elias

def main():
    print("==========================================")
    print("   INFORMATION THEORY: LABS 01 & 02      ")
    print("==========================================\n")

    # --- LAB 01 SCENARIOS ---
    print("--- [LAB 01] Information & Entropy ---")
    
    # Ex 1: 3 Outcomes
    probs = [0.1, 0.3, 0.6]
    print(f"\n[1.1] Information for probabilities {probs}:")
    for i, p in enumerate(probs):
        print(f"  Outcome {i+1}: {information.calculate_information(p):.4f} bits")
    
    # Ex 2: Rain/Wind Joint Entropy
    p_rain, p_wind = 0.65, 0.45
    print(f"\n[1.2] Joint Entropy (Rain={p_rain}, Wind={p_wind}):")
    joint_map = joint_probs.calculate_joint_probabilities(p_rain, p_wind)
    
    for k, v in joint_map.items():
        print(f"  P({k}) = {v:.4f}")
        
    h_joint = entropy.calculate_entropy(list(joint_map.values()))
    print(f"  -> Total Joint Entropy: {h_joint:.4f} bits")
    print("-" * 40)

    # --- LAB 02 SCENARIOS ---
    print("\n--- [LAB 02] Coding Algorithms ---")
    # Dataset from C++ slides
    data = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}
    total = sum(data.values())
    data_probs = {k: v/total for k, v in data.items()}
    
    print(f"Dataset: {data}")

    # 1. Huffman
    print("\n[2.1] Huffman Codes:")
    h_codes = huffman.build_huffman_codes(data)
    for c in sorted(h_codes):
        print(f"  {c}: {h_codes[c]}")

    # 2. Fano (requires sorting)
    print("\n[2.2] Shannon-Fano Codes:")
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    f_codes = fano.build_fano_codes(sorted_data)
    for c, _ in sorted_data:
        print(f"  {c}: {f_codes[c]}")

    # 3. Elias
    print("\n[2.3] Shannon-Fano-Elias Codes:")
    e_codes = elias.build_elias_codes(data_probs)
    for c in sorted(e_codes):
        print(f"  {c}: {e_codes[c]}")

    print("\n=== EXECUTION FINISHED ===")

if __name__ == "__main__":
    main()
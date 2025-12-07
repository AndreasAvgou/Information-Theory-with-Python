import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparator for min-heap
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_codes(freq_map):
    """
    Builds Huffman tree and returns codes.
    Input: Dictionary {char: frequency}
    """
    # Create leaf nodes
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    # Build Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Generate Codes
    root = heap[0]
    codes = {}

    def traverse(node, current_code):
        if not node:
            return
        if node.char is not None:
            codes[node.char] = current_code
            return
        traverse(node.left, current_code + "0")
        traverse(node.right, current_code + "1")

    traverse(root, "")
    return codes
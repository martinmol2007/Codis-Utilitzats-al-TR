import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    
    return codebook

def huffman_encode(data):
    if not data:
        return "", None

    frequency = Counter(data)
    huffman_tree = build_huffman_tree(frequency)
    huffman_codes = build_codes(huffman_tree)
    
    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data, huffman_tree, huffman_codes

def huffman_decode(encoded_data, huffman_tree):
    decoded_output = []
    current_node = huffman_tree
    
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.left is None and current_node.right is None:
            decoded_output.append(current_node.char)
            current_node = huffman_tree
    
    return ''.join(decoded_output)

def main():
    missatge = input("Introdueix el missatge a codificar: ")
    
    print("Missatge original:", missatge)
    
    encoded_message, huffman_tree, huffman_codes = huffman_encode(missatge)
    
    print("\nCodificació Huffman per a cada caràcter:")
    for char, code in huffman_codes.items():
        print(f"'{char}': {code}")
    
    print("\nMissatge codificat:", encoded_message)
    
    decoded_message = huffman_decode(encoded_message, huffman_tree)
    print("Missatge descodificat:", decoded_message)

if __name__ == "__main__":
    main()

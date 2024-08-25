from entropia import shannon_entropy
from huffman import huffman_encode, huffman_decode

def main():
    # Sol·licitar a l'usuari el missatge
    missatge = input("Introduïu el missatge per codificar: ")

    # Calcular i mostrar l'entropia
    entropia = shannon_entropy(missatge)
    print(f"\nH(X) = {entropia} bits. Aproximat a {round(entropia)} bits/símbol")
    print(f"Necessitareu aproximadament {len(missatge) * round(entropia)} bits per codificar òptimament '{missatge}'")

    # Codificació Huffman
    encoded_message, huffman_tree, huffman_codes = huffman_encode(missatge)
    print("\nCodificació Huffman per a cada caràcter:")
    for char, code in huffman_codes.items():
        print(f"'{char}': {code}")

    print("\nMissatge codificat:", encoded_message)

    # Decodificació Huffman
    decoded_message = huffman_decode(encoded_message, huffman_tree)
    print("Missatge descodificat:", decoded_message)

if __name__ == "__main__":
    main()
import math


def shannon_entropy(data):
    pila = {}
    llista_symbols = {}

    for character in data:
        pila[character] = round(data.count(character) / len(data), 5)
        llista_symbols[character] = data.count(character)
    print("\nFreqüència d'aparició dels símbols:\n")
    for symbol in pila:
        print("{0} --> {1} -- {2}".format(symbol, pila[symbol], llista_symbols[symbol]))
    return symbol_frequency(pila)


def symbol_frequency(symbol_set):
    bit_set = [round(symbol_set[symbol] * math.log2(symbol_set[symbol]), 5) for symbol in symbol_set]
    entropia = -1 * (round(sum(bit_set), 5))
    return entropia


if __name__ == "__main__":
    m = input("\nIntrodueix un missatge: ")
    bits = shannon_entropy(m)
    print("\nH(X) = {0} bits. Aproximat a {1} bits/símbol".format(bits, round(bits)))
    print("Necessitarà aproximadament {0} bits per codificar òptimament '{1}'".format(len(m) * round(bits), m))

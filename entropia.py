import math


def shannon_entropy(data):
    stack = {}
    symbol_list = {}

    for character in data:
        stack[character] = round(data.count(character) / len(data), 5)
        symbol_list[character] = data.count(character)
    print("\nFrequencia d'aparicio del simbols:\n")
    for symbol in stack:
        print("{0} --> {1} -- {2}".format(symbol, stack[symbol], symbol_list[symbol]))
    return symbol_frequency(stack)


def symbol_frequency(symbol_set):
    bit_set = [round(symbol_set[symbol] * math.log2(symbol_set[symbol]), 5) for symbol in symbol_set]
    entropy = -1 * (round(sum(bit_set), 5))
    return entropy


if __name__ == "__main__":
    m = input("\nIntrodueix un missatge: ")
    bits = shannon_entropy(m)
    print("\nH(X) = {0} bits. Aproximat a {1} bits/simbol, ".format(bits, round(bits)))
    print("Necessitara aproximadament {0} bits per codifiacr optimament '{1}'".format(len(m) * round(bits), m))
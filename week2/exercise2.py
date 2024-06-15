
def character_count(s: str):
    freqs = {}
    for c in s:
        f = freqs.get(c)
        f = (f + 1) if f is not None else 1
        freqs[c] = f

    return freqs


if __name__ == '__main__':
    print(character_count("engineering"))

    assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
    print(character_count('smiles'))

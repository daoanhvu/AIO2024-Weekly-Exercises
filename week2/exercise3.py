import re


def count_word(file_path):
    freqs = {}

    try:
        with open(file_path) as file:
            content = file.read()
            words = re.findall(r'\b\w+\b', content.lower())
            for w in words:
                f = freqs.get(w)
                f = (f + 1) if f is not None else 1
                freqs[w] = f
        return freqs
    except FileNotFoundError as ex:
        print(ex)
        return None


if __name__ == '__main__':
    file_path = '.\\P1_data.txt'
    result = count_word(file_path)
    assert result['who'] == 3
    print(result['man'])

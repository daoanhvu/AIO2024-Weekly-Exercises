
def find_max(one_d_slice, k):
    length = len(one_d_slice)
    max = one_d_slice[0]
    for i in range(1, length):
        tmp = one_d_slice[i]
        max = tmp if tmp > max else max
    return max


def max_kernel(num_list, k):
    result = []
    last_start = len(num_list) - k
    for i in range(last_start + 1):
        result.append(find_max(num_list[i:i+k], k))
    return result


if __name__ == '__main__':
    assert max_kernel(num_list=[3, 4, 5, 1, -44], k=3) == [5, 5, 5]

    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_kernel(num_list, k))

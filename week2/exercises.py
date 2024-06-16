
def check_the_numer(N):
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        list_of_numbers.append(i)

    if N in list_of_numbers:
        results = "True"
    if N not in list_of_numbers:
        results = "False"

    return results


def my_function_6(data, max, min):
    result = []

    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)

    return result


def my_function_7(x, y):
    x.extend(y)
    return x


def my_function_8(a_list):
    return min(a_list)


def my_function_9(a_list):
    return max(a_list)


def my_function_10(integers, number=1):
    return any(i == number for i in integers)


def my_function_11(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)


def my_function_12(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    # could be: return [i for i in data if i % 3 == 0]
    return var


def my_function_13(y):
    var = 1
    i = 1
    while i <= y:
        var = var * i
        i = i + 1

    return var


def my_function_14(x):
    return x[::-1]


def function_helper_15(x):
    return 'T' if x > 0 else 'N'


def my_function_15(data):
    return [function_helper_15(x) for x in data]


def function_helper_16(x, data):
    for i in data:
        if x == i:
            return 0
    return 1


def my_function_16(data):
    res = []
    for i in data:
        if function_helper_16(i, res):
            res.append(i)

    return res

# =================================================


def test_check_the_number():
    N = 7
    assert check_the_numer(N) == "False"
    N = 2
    results = check_the_numer(N)
    print(results)


def test_function_6():
    my_list = [5, 2, 5, 0, 1]
    max = 1
    min = 0
    assert my_function_6(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
    my_list = [10, 2, 5, 0, 1]
    max = 2
    min = 1
    print(my_function_6(max=max, min=min, data=my_list))


def test_my_function_7():
    list_num1 = ['a', 2, 5]
    list_num2 = [1, 1]
    list_num3 = [0, 0]
    assert my_function_7(list_num1, my_function_7(
        list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]
    list_num1 = [1, 2]
    list_num2 = [3, 4]
    list_num3 = [0, 0]
    print(my_function_7(list_num1, my_function_7(list_num2, list_num3)))


def test_my_function_8():
    my_list = [1, 22, 93, -100]
    assert my_function_8(a_list=my_list) == -100
    my_list = [1, 2, 3, -1]
    print(my_function_8(my_list))


def test_my_function_9():
    my_list = [1001, 9, 100, 0]
    assert my_function_9(a_list=my_list) == 1001
    my_list = [1, 9, 9, 0]
    print(my_function_9(my_list))


def test_my_function_10():
    my_list = [1, 3, 9, 4]
    assert my_function_10(my_list, -1) == False
    my_list = [1, 2, 3, 4]
    print(my_function_10(my_list, 2))


def test_my_function_11():
    assert my_function_11([4, 6, 8]) == 6
    print(my_function_11())


def test_my_function_12():
    assert my_function_12([3, 9, 4, 5]) == [3, 9]
    print(my_function_12([1, 2, 3, 5, 6]))


def test_my_function_15():
    data = [10, 0, -10, -1]
    assert my_function_15(data) == ['T', 'N', 'N', 'N']
    data = [2, 3, 5, -1]
    print(my_function_15(data))


def test_my_function_16():
    lst = [10, 10, 9, 7, 7]
    assert my_function_16(lst) == [10, 9, 7]
    lst = [9, 9, 8, 1, 1]
    print(my_function_16(lst))


if __name__ == '__main__':
    # test_function_6()
    # test_my_function_12()
    # assert my_function_14('I can do it') == 'ti od nac I'
    # print(my_function_14('apricot'))
    # test_my_function_15()
    test_my_function_16()

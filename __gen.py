import random


def increasing_list(size):

    return [i for i in range(size)]


def descending_list(size):

    return [i for i in range(size)][::-1]


def random_list(size):

    data = [i for i in range(size)]
    random.shuffle(data)
    return data


def recurring_list(size):

    numbers = [i for i in range(size)]

    data = []

    padding_num = random.choice(numbers)

    data = [padding_num] * size

    return data


def partially_list(size, div):
    pair_size = size // div
    print("pair_size =", pair_size)

    data = []
    if size > div:
        for i in range(0, size, pair_size):     # (0..39, шаг=1)
            for k in range(i + pair_size, i, -1):   # (0+1, 0, шаг=-1)
                data.append(k)

        if len(data) > size:
            data = data[:-(pair_size)]

        while len(data) < size:
            for num in range(size)[::-1]:
                if num not in data:
                    data.append(num)

    else:
        print("else")
        data = [i for i in range(size)]

    return data[::-1]

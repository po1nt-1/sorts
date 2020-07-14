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

    return [0, 1, 2, 3]

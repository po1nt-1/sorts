import random


def increasing_list(size):
    if size < 0:
        raise Exception("Слишком маленький предел последовательности")

    return [i for i in range(size)]


def descending_list(size):
    if size < 0:
        raise Exception("Слишком маленький предел последовательности")

    return [i for i in range(size)][::-1]


def random_list(size):
    if size < 0:
        raise Exception("Слишком маленький предел последовательности")

    data = [i for i in range(size)]
    random.shuffle(data)
    return data


def recurring_list(size):
    if size < 0:
        raise Exception("Слишком маленький предел последовательности")

    numbers = [i for i in range(size)]

    data = []
    for _ in range(len(numbers)):
        data.append(random.choice(numbers))

    return data


def partially_list(size):
    if size < 0:
        raise Exception("Слишком маленький предел последовательности")

    data1 = [i for i in range(int(size*0.7))]
    data2 = [i for i in range(int(size*0.7), size)]
    random.shuffle(data2)

    return data1 + data2


if __name__ == "__main__":
    pass

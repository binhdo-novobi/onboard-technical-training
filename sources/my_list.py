# Exercise 1
def exercise_1(a, threshold):
    print([i for i in a if i < threshold])


# Exercise 2
def exercise_2(a):
    print(sorted(a))
    print(list(filter(lambda x: x % 2 == 0, a)))
    print(list(filter(lambda x: x % 2 != 0, a)))


# Exercise 3
def exercise_3(a, b):
    print(list(set(a) & set(b)))


# Exercise 4
def exercise_4(a, n=1):
    if 2 * n > len(a):
        return a
    else:
        return a[:n] + a[-n:]


# Exercise 5
def exercise_5_1(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b


def exercise_5_2(a):
    return list(set(a))


if __name__ == "__main__":
    print("Exercise 1:")
    threshold = 15
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    exercise_1(a, threshold)

    print("\nExercise 2:")
    a = [1, 2, 1, 8, 5, 3, 89, 21, 34, 55, 13]
    exercise_2(a)

    print("\nExercise 3:")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    exercise_3(a, b)

    print("\nExercise 4:")
    a = [5, 10, 15, 20, 25]
    n = 3
    print(exercise_4(a, n))

    print("\nExercise 5:")
    a = [1, 1, 2, 3, 5, 5, 3, 10, 1]
    print(exercise_5_1(a))
    print(exercise_5_2(a))

def exercise_1(a, threshold):

    result = [item for item in a if item < threshold]
    return result

def exercise_2(a):
    
    a_sorted = sorted(a)
    a_even = list(filter(lambda x: x % 2 == 0, a_sorted))
    a_odd =  list(filter(lambda x: x % 2 != 0, a_sorted))

    return a_sorted, a_even, a_odd

def exercise_3(first, second):

    return list(set(filter(lambda e: e in first, second)))
    
def exercise_4(a, n):

    if n >= 3:
        return a
    else:
        return sorted(a[:n] + a[-n:])
        
def exercise_5_loop(a):

    result = []
    for item in a:
        if item not in result:
            result.append(item)
    return result

def exercise_5_set(a):

    return list(set(a))

if __name__ == "__main__":

    # Exercise 1
    a_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    threshold = 15
    res_1 = exercise_1(a_1, threshold)
    print(f"Exercise 1: {res_1}")

    # Exercise 2
    a_2 = [1, 2, 1, 8, 5, 3, 89, 21, 34, 55, 13]
    a_sorted, a_even, a_odd = exercise_2(a_2)
    print(f"Exercise 2, sorted list: {a_sorted}")
    print(f"Exercise 2, even: {a_even}")
    print(f"Exercise 2, odd: {a_odd}")

    # Exercise 3
    first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    common = exercise_3(first, second)
    print(f"Exercise 3: {common}")

    # Exercise 4
    a = [5, 20, 10, 1, 4, 15, 25, 95, 17, 83]
    n = 2
    res = exercise_4(a, n)
    print(f"Exercise 4: {res}")

    # Exercise 5
    print(f"Exercise 5 loop: {exercise_5_loop(first)}")
    print(f"Exercise 5 set : {exercise_5_set(first)}")
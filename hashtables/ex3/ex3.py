def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # initialize a dict:
    d = {}

    # we need to go through the arrays and when a number shows up in both arrays we need to add it to the d and return the d
    for i in arrays:
        for j in arrays:
            if j not in d:
                d[j] = 1
            else:
                d[j]+=1
    result = []

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

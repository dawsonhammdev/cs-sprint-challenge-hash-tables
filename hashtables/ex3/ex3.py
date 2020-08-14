def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # initialize a dict:
    d = {}
    result = []

    # we need to go through the arrays and when a number shows up in both arrays we need to add it to the d and return the d
    for i in arrays:
        for j in i:
            if j not in d:
                d[j] = 1
            else:
                d[j]+=1

    for x in d:
        if d[x] == len(arrays):
            result.append(x)

    # need to compare the values in the dictonary with the length of the arrays to see if there are dupicates and then return the results.
    

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

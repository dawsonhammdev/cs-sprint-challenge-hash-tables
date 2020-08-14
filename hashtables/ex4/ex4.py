def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    

    # for loop to go through a
    for i in a:
        d[i] = True
    result = []
    for x in a:
        if x > 0 and -x in d:
            result.append(x)
        

    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

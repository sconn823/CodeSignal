'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer a

    If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

    Guaranteed constraints:
    1 ≤ a.length ≤ 1000,
    -1 ≤ a[i] ≤ 1000.

    [output] array.integer
        Sorted array a with all the trees untouched.

'''


def sortByHeight(a):

    l = sorted([i for i in a if i > 0])
    for n, i in enumerate(a):
        if i == -1:
            l.insert(n, i)
    return l


if __name__ == "__main__":
    print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
    print(sortByHeight([-1, -1, -1, -1, -1]))
    print(sortByHeight([-1]))
    print(sortByHeight([4, 2, 9, 11, 2, 16]))
    print(sortByHeight([2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]))
    print(sortByHeight([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]))

'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

    For n = 1230, the output should be
    isLucky(n) = true;
    For n = 239017, the output should be
    isLucky(n) = false.
'''


def isLucky(n):
    n = [int(i) for i in str(n)]
    sideA = 0
    sideB = 0
    index = 0
    half = len(n)/2
    while(index < half):
        sideA += n[index]
        sideB += n[index + half]
        index += 1
    return sideA == sideB


if __name__ == "__main__":
    print(isLucky(1230))
    print(isLucky(239017))
    print(isLucky(134008))
    print(isLucky(10))
    print(isLucky(11))
    print(isLucky(1010))
    print(isLucky(261534))
    print(isLucky(100000))

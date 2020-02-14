'''Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].'''


def allLongestStrings(inputArray):
    return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]


if __name__ == "__main__":
    print(allLongestStrings(["aba",
                             "aa",
                             "ad",
                             "vcd",
                             "aba"]))
    print(allLongestStrings(["abc",
                             "eeee",
                             "abcd",
                             "dcd"]))
    print(allLongestStrings(["a",
                             "abc",
                             "cbd",
                             "zzzzzz",
                             "a",
                             "abcdef",
                             "asasa",
                             "aaaaaa"]))
    print(allLongestStrings(["enyky",
                             "benyky",
                             "yely",
                             "varennyky"]))
    print(allLongestStrings(["abacaba",
                             "abacab",
                             "abac",
                             "xxxxxx"]))
    print(allLongestStrings(["young",
                             "yooooooung",
                             "hot",
                             "or",
                             "not",
                             "come",
                             "on",
                             "fire",
                             "water",
                             "watermelon"]))
    print(allLongestStrings(["onsfnib",
                             "aokbcwthc",
                             "jrfcw"]))

example = "aabbcc"


def check_trailing_char(string):
    for i in string:
        if example.index(i) == example.rindex(i):
            print(i)
        print('-')


check_trailing_char(example)

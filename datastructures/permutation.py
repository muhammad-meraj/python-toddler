"""
This function return True if str1 is a permutation of str2
"""

def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    sum_s1 = sum_s2 = 0

    for i in range(0, len(s1)):
        sum_s1 += ord(s1[i])
        sum_s2 += ord(s2[i])

    if sum_s1 == sum_s2:
        return True

    return False


def main():
    a = 'abc'
    b = 'cba'

    print is_permutation(a, b)

    a = 'abcv'
    b = 'abcf'

    print is_permutation(a, b)

    return

if __name__ == '__main__':
    main()
    
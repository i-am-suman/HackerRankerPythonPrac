# Complete the solve function below.
def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))
    # return ' '.join( c.capitalize() for c in s.split())


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

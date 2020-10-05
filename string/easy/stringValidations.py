if __name__ == '__main__':
    i = input()
    print(any(s.isalnum() for s in i))
    print(any(s.isalpha() for s in i))
    print(any(s.isdigit() for s in i))
    print(any(s.islower() for s in i))
    print(any(s.isupper() for s in i))

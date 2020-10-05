def wrap(string, max_width):
    str = ""
    for i in range(0, len(string), max_width):
        str += string[i:i + max_width] + "\n"
    return str


if __name__ == '__main__':
    str = input()
    wid = int(input())
    result = wrap(str, wid)
    print(result)

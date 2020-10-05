def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip().upper()
    sub_string = input().strip().upper()
    print(count_substring(string, sub_string))
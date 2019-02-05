import sys


def main():
    """This program print count of lines/words/bytes in the file"""

    source = input('Choose your source: input "stdin" or "fileinput".\n'
                   'You can input "help" to get help.\n')
    arr = []

    if source == 'stdin':
        print('Windows: When you need to stop, go to the new line and then press "CTRL+Z" then "Enter".\n'
              'Mac or UNIX: press "CTRL+D"')
        for line in sys.stdin:
            arr.append(line.rstrip())
        condition(arr)

    if source == 'fileinput':
        file = input('Please input path to file then press "Enter".\n')
        with open(file, 'r') as file:
            arr = file.read().splitlines()
        condition(arr)

    if source == "help":
        print('Input "wc.py -l" to get the count of lines,\n'
              'input "wc.py -w" to get the count of words,\n'
              'input "wc.py -c" to get the count of bytes.')
        sys.exit(1)
    else:
        print("Unknown command")
        sys.exit(-1)


def condition(arr):
    if len(sys.argv) == 1:
        print(cnt_of_lines(arr), cnt_of_words(arr), cnt_of_bytes(arr))
        sys.exit(1)
    if sys.argv[1] == '-l':
        print('\n' + str(cnt_of_lines(arr)))
        sys.exit(1)
    if sys.argv[1] == '-w':
        print('\n' + str(cnt_of_words(arr)))
        sys.exit(1)
    if sys.argv[1] == '-c':
        print('\n' + str(cnt_of_bytes(arr)))
        sys.exit(1)


def cnt_of_lines(arr):
    return len(arr)


def cnt_of_words(arr):
    return len([word for string in arr for word in string.split()])


def cnt_of_bytes(arr):
    return sys.getsizeof(arr)


if __name__ == '__main__':
    main()

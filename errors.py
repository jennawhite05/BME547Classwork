# a = "The sky is blue"
# print(a)

# for letter in a:
#     print(letter)


def convert_string(string):
    try:
        number = int(string)
        print(number)
    except ValueError:
        print('cannot convert to integer')


def main():
    convert_string('2')
    convert_string('Hello')


if __name__ == "__main__":
    main()

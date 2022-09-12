#Написати програму, яка видаляє зі строки такі символи пунктуації:
# крапку, кому, крапку з комою, двокрапку, знаки оклику та питання.

if __name__ == '__main__':
    s = "Hello, World! How are you? We are here to learn programmimg, such a Python."
    chars = ['.', ',', '!', '?', ";", ":"]

    res = s.translate(str.maketrans('', '', ''.join(chars)))
    print(res)

# Task 1. Replace JAVA with PYTHON in given string. Also find how many time Java before replace string and how many time python after replace string.

# String example :: Java is a widely used programming language.
#                  The rules and syntax of Java are based on the C and C++ languages.
#                  I love Java more than Python. Python is JAva but JAva is python.

# Output

# String :: PYTHON is a widely used programming language.
#           The rules and syntax of PYTHON are based on the C and C++ languages.
#           I love PYTHON more than Python. Python is PYTHON but PYTHON is python.
#           Java before replace string :: X times Python after replace string :: X times

sentence = "Java is a widely used programming language. The rules and syntax of Java are based on the C and C++ languages. I love Java more than Python. Python is JAva but JAva is python."


def my_string(sentence):
    a = sentence.title()
    print(a)
    print()
    b = a.count("Java")
    print(f"Total Java Used in this sentance {b}")

    c = a.replace("Java", "Python")
    print()
    print(c)
    d = c.count("Python")
    print()
    print(f"Total Python Used in this sentance after replacing {d}")


my_string(sentence)

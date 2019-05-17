from sys import stdin

def fun():
    s = input()
    s2 = s.split("/")
    year = int(s2[0])
    month =int(s2[1])
    day = int(s2[2])

    if year < 2018:
        print("Heisei")
    elif month < 5:
        print("Heisei")
    else:
        print("TBD")


if __name__ == '__main__':
    fun()

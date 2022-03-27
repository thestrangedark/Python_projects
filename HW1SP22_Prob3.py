import random


def main():
    C = random.random()
    print(C)
    random.normalvariate(C, 1)
    print(C)
    return C

if __name__ == '__main__':
        main()
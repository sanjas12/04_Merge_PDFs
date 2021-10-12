import sys

def main(arg):
    print(type(arg[0]), arg)

if __name__ == '__main__':
    main(sys.argv[1:])

# --start
import sys

def volcano():  #add
    print('dif-tor heh smusma')  #add

def default():
    print('o que voce quer?')

def main():
    if sys.argv[1] == 'volcano':  #add
       volcano()  #add
    else:
       default()

if __name__ == '__main__':
    main()
# --end

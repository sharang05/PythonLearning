class inclusiveRange:
    def __init__(self, *args):
        numargs = len(args)
        if numargs <1: raise TypeError('Required at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step =1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError ('Expected at most 3 arguments, got {}'.format(numargs))


    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step

def main():
    o = inclusiveRange(5, 25, 3)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()


@profile
def a():
    for i in xrange(10000):
        j=i

@profile
def b():
    for k in xrange(100000):
        j=k

@profile
def h():
    for k in xrange(100000):
        j=k


@profile
def main():
    a()
    b()
    h()

if __name__ =='__main__':
    main()

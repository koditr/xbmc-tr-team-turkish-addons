s = 'bHR0dDpwLaE3OC4zMTEvMahvNDIwfG1tLx=='


def better_yop(s):
    def gen(h):
        for c in h:
            n = ord(c)-1
            if n == 96:
                yield 'z'
            elif 96<n<122:
                yield chr(n)
            else:
                yield c
    return ''.join(gen(s))

a=better_yop('bHR0dDpwLaE3OC4zMTEvMahvNDIw')
print a
print "aHR0cDovLzE3OC4yMTEuMzguNDIv"

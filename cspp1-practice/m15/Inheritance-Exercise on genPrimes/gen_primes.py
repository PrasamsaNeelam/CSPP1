#define the gen_primes function here
def genPrimes(a):
    n = 2
    c = 0
    while c < a:
        cnt = 0
        for i in range(1, n):
            if n%i == 0:
                cnt += 1
        if cnt == 1:
            yield n
            c += 1
        n += 1

def main():
    data = input()
    l = data.split()
    a = int(l[0])
    b = int(l[1])
    primeGenerator = genPrimes(a)
    for i in range(a):
        p = primeGenerator.__next__()
        if i%b == 0:
            print(p)
    
if __name__ == "__main__":
    main()

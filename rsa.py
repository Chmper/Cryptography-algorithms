import random
zakres = 1200

def prime_array(givenNumber):

    # Initialize a list
    primes = []
    for possiblePrime in range(2, givenNumber + 1):

        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(possiblePrime)

    return(primes)

array = prime_array(zakres)

def get_p_q():
    p = random.choice(array)
    q = random.choice(array)

    while abs(p.bit_length() - q.bit_length()) >= 3:
        q = random.choice(array)
        if p == q:
            q = random.choice(array)

    return p, q

def euler_function():
    return  (p-1)*(q-1)

def mod_n():
    return  p*q

def nwd( m, n ):
    while True:
        r = m % n
        if not r:
            return n
        m, n = n, r

def get_e():
    for i in range(2,n):
        if nwd(i, euler) == 1 and nwd(i, euler)%2 == 1:
            return i

def euklides(a, b):
    x = 1
    y = 0
    if(b != 0):
        euklides(b, a%b)
        pom = y
        y = x - a/b*y
        x = pom
    return x, y

def search_d(mnoznik, modulo):
    for i in range(modulo-1):
        if i*mnoznik % modulo == 1:
            return i

def find_array(x):
    powers = []
    i=1
    while i<= x:
        if i & x: # and bitowy
            powers.append(i)
        i <<= 1
    return powers

def code_array(arr, e, n):
    temp_arr = []
    for i in arr:
        temp_arr.append(i**e % n)

    return temp_arr

def decode_array(arr, d, n):
    temp_arr = []
    for i in arr:
        temp_arr.append(i**d % n)

    return temp_arr

if __name__ == '__main__':
    p, q = get_p_q()
    print("dlugosci bitowe: ", p.bit_length(), q.bit_length())
    euler = euler_function()
    n = mod_n()
    e = get_e()

    d = search_d(e, euler)
    print("p, q:", p,q)
    print("euler: ", euler)
    print("n: ", n)
    print("d: ", d)

    ## (e, n) -- public key
    ## (d, n) -- private key
    ## liczby z przedzialu 0 < t < n

    array = [random.randint(2, n-1) for x in range(10)] ## tekst
    print("przed zakodowaniem ", array)
    coded_array = code_array(array, e, n)
    decoded_array = decode_array(coded_array, d, n)

    print("po zakodowaniu ",coded_array)
    print("po odkodowaniu ",decoded_array)

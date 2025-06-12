def is_prime(n):
    if n>1 and n%1==0 and n%n==0:
        print(True)
    else:
        print(False)
is_prime(8)
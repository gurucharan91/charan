def factors(n):
    factorlist=[]
    for i in range(1,n+1):
        if n%i==0:
            factorlist=factorlist+[i]
    return(factorlist)
def is_prime(n):
    return(factors(n)==[1,n])
def primes_upto(n):
    prime_list=[]
    for i in range(1,n+1):
        if is_prime(i):
            prime_list=prime_list+[i]
    return(prime_list)
    

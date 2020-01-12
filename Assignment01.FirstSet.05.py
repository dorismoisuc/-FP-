n=int(input("Enter a number= "))
#if the number is less or equal to 2, then the max previous doesn't exist
if n <= 2: 
    print ("Such a number doesn't exist")
m = n
#function that verifies if a number is prime
def PrimeVerif(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False;
    return True
#getting the previous max prime
while (PrimeVerif(n) == False):
                          n=n-1

#if its equal to itself, find the previous
if n == m:
    n=n-1
    while (PrimeVerif(n) == False):
                          n=n-1
print ("The max previous prime number is: ",n)


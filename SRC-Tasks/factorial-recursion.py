def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    #end if
#end function
# n = int(input("Input a number: "))

# print(fac(n))

numbers = [3, 6, 2, 8, 1]

def sum(n, numbers):
    if n == -1:
        return 0
    else:
        return numbers[n] + sum(n-1, numbers)
    #end if
#end function
    
# print(sum(len(numbers)-1, numbers))

def fibiterative(n):
    fibonacci = [1,1]
    for i in range(2, n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    #next i
    return fibonacci[i-1]
#end function

# print(fibiterative(10))
        

fibdict = []


def fib(n):
    if n in fibdict:
        return fibdict[n]
    else:
        solution = fib(n-1) + fib(n-2)
        fibdict[n] = solution
    #end if
#end function

print(fib(1))
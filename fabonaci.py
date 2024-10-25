
## FIBONACI GENERATOR


def fibonaci(n):
    fibonaci_sequence = [0,1]
    for i in range(2,n):
        nxt_number = fibonaci_sequence[-1] + fibonaci_sequence[-2] 
        fibonaci_sequence.append(nxt_number)
    return fibonaci_sequence[:n]

n =int(input("Enter the numbers range :"))
print(fibonaci(n))

    
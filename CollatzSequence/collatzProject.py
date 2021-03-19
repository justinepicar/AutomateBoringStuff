#The Collatz Sequence
#Write a function named collatz() that has one parameter named number.
#If number is even, then collatz() should print number // 2 and return this value
#If number is odd, then collatz() should print and return 3 * number + 1.
#Then write a program that lets the user type in an integer
#and that keeps calling collatz() on that number until the function returns the value 1.

def collatz(number):
    if number%2 == 0:
        answer=number//2
        print(answer)
        return answer
    elif number%2 == 1:
        answer=3*number+1
        print(answer)
        return answer


while True:
    print('Press 0 to quit. Enter a positive number:')
    try:
        pick=int(input())
        if pick == 0:
            break
        elif pick < 0:
            print('Please choose a number greater than zero.')
            continue
        else:
            while pick != 1 and pick > 0:
                num=collatz(pick)
                pick=num
    except ValueError:
        print('Error. Only enter a number.')

print('Bye!')






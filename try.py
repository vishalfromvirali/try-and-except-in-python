try:
    mark1=int(input("enter your mark 1 :"))
    mark2=int(input("enter your mark 2 :"))
    total =mark1/mark2
    print("average mark : =",total)
except ZeroDivisionError:
    print("you have a arithmatic error in divide")    
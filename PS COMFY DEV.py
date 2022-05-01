#Code by Michaela Intemann
import statistics
cont = 1
print("This program finds the standard deviation of 10 temperatures and checks for comyfness.")
print("----------------------")
while cont == 1:
    T = []
    S=0
    M=0
    N=0
    while N != 10:
        T.append(float(input("Enter a temperature: ")))
        N=N+1
    for i in range(0,len(T)):
        S = S+T[i]
    STDEV = statistics.stdev(T)
    if STDEV > 1:
        C = "NOT COMFY"
    else:
        C = "COMFY"
    print("--------------------")
    print("Temperatures Given:",T,'\n',"-----------------------")   
    print("Total Values:",N)
    print("Standerd Deviation is:",round(STDEV,4))
    print("Rating is:",C,'\n','\n',"-----------------------")
    cont = int(input("Would you like to put in more temperatures? (enter 0 for no)"))
print("Goodbye!")



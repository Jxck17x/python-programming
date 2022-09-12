T=int(input("value of number T: "))
E=0
L=0
N=0
Mox=0
for i in range(1,T+1):
    E=int(input("value of entry: "))
    L=int(input("value of exit: "))
    N=N+E-L
    Mox=max(N,Mox)
    print("maximum",Mox)
    print("Hour",i,":")
    print("Entry:",E," ","Exit:",L)
    print("No. of guests on ship:",N)
    print("Hence,the maximum number of guests within {0} hours is {1}".format(T+1,Mox))

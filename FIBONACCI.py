#PROGRAM TO DISPLAY THE FIBONACCI SEQUENCE UPTO n-th TERMS
n_terms=int(input("how many terms the user wants to print?"))
n_1=0
n_2=1
count=0
if n_terms<=0:
    print("please enter a positive integer")
elif n_terms==1:
    print("the fibonacci sequence of the numbers upto",n_terms,":")
    print(n_1)
else:
    print("the fibonacci sequence of the numbers is:")
    while count<n_terms:
        print(n_1)
        nth=n_1+n_2
        n_1=n_2
        n_2=nth
        count+=1
        


Initial_number = input("Enter the Number: ") 
def ArmstrongNumber(number):
    
    length = len(Initial_number)
    if length == 1:
        print("This is an Armstrong number")
    else:
        summation = 0

        number = list(map(int, str(Initial_number))) 

        for item in number:
            exponential = item ** length
            summation = summation + exponential

        if summation == number:
            print(f"The total is {summation} which is equal to {Initial_number}\n" "This is an Armstrong number")
        
        else:
            print (f"The total is {summation} which is not equal to {Initial_number}")

        

       


ArmstrongNumber(Initial_number)
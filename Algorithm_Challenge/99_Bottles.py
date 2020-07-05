'''
99 bottles of beer on the wall, 99 bottles of beer. 
Take one down, pass it around, 98 bottles of beer on the 

One-hundred bottles of beer on the wall,
One-hundred bottles of beer!
Take one down,
Pass it around,
Ninety-nine bottles of beer on the wall!

'''



for i in reversed(range(100)):
    next = i - 1
    if i >=2:
        print(f"{i} bottles of beer on the wall,\n" "Take one down,\n" 
       "Pass it around,\n" f"{next} bottles of beer on the wall\n")
    elif i < 1:
        print(f"{i} bottle of beer on the wall,\n" "Take one down,\n" 
       "Pass it around,\n" "No bottle of beer on the wall\n")
    else: 
        print(f"{i} bottle of beer on the wall,\n" "Take one down,\n" 
       "Pass it around,\n" f"{next} bottle of beer on the wall\n")
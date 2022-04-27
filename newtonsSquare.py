n=float(input("enter the number"))
original_guess=n/2
new_calculated_guess=(original_guess+n/original_guess)/2
while True:
    new_calculated_guess=(original_guess+(n/original_guess))/2
    if(abs(original_guess-new_calculated_guess)<0.0000000000000000000000001):
        break
    original_guess=new_calculated_guess
print(new_calculated_guess)

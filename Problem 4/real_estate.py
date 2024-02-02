
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here
    
    
    print("This house is $" + str(current_price) + ". The change is $" + str(current_price - last_month_price) + " since last month.")
    #print("The estimated monthly mortgage is $" + str((current_price * 0.051)/12))
    print(f'The estimated monthly mortgage is ${((current_price * 0.051) / 12):.2f}.')


if __name__ == "__main__":
    real_estate()
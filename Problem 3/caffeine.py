
def caffeine():
    caffeine_mg = float(input())
    #after_6 = caffeine_mg/2
    #after_12 = caffeine_mg/4
    #after_24 = caffeine_mg/16

    print(f' After 6 hours:{caffeine_mg/2:.2f} mg')
    print(f' After 12 hours: {caffeine_mg/4:.2f} mg')
    print(f' After 24 hours: {caffeine_mg/16:.2f} mg')
    

    
if __name__ == "__main__":
    caffeine()
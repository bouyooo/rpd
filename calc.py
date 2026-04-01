def main():
    print("Let's implement division. Type two numbers for x and y")
    
    x = int(input("x > "))
    y = int(input("y > "))
    if divide(x, y) == None:
        pass
    else:
        print("%d / %d = %0.3f" % (x, y, divide(x, y)))    
    
def add(a, b):
    return a + b
    
    
# TODO: divide() 함수 정의
        
def divide(a, b ):
    if b != 0:
        return a/b 
    else : 
        print('Error: cannot divide by zero.')
        return None

if __name__ == "__main__":
    main()


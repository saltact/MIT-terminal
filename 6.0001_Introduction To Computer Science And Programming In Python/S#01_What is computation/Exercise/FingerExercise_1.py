#-------------------- Finger exercise 2:-------------------------
def isOdd(number):
    return number % 2 != 0

def main ():
    x = 33;
    y = 61;
    z = 41;
    # Case 1: All odds
    if isOdd(x):
        if isOdd(y):
                if (x > y):
                    if isOdd(z):
                        if (x > z):
                            print ("X have the largest odd number " , x);
                        elif (y > z):
                            print ("Y have the largest odd number" , y);
                        else:
                            print ("Z have the largest odd number" , z);

        # Case 2: x and y are odds
            # elif (x > y):
            #     print ("X have the largest odd number" , x);
            # else:
            #     print ("Y have the largest odd number" , y);
        # Case 3: x and z are odds
        elif isOdd(z):
            if (x > z):
                print ("X have the largest odd number" , x);
            else:
                print ("Z have the largest odd number" , z);
        
        # Case 4: y and z are odds
    elif isOdd(y):
        if isOdd(z):
            if (y > z): 
                print ("Y have the largest odd number" , y);
            else:
                print ("Z have the largest odd number" , z);
        else:
            print("Y have the largest odd number", y);
    # Case 5: One of em is odd
    elif isOdd(z):
        print("Z have the largest odd number" , z);
    # Case 6: None of em are odds
    else:
        print("None of the variables contain the odd number.")





main();

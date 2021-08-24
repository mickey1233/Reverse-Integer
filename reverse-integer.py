def reverse(x):
    z = ''
    y = list(map(str, str(x)))
    if x >= 0:
        for i in range(int(len(y)/2)):
            head = y[i]
            tail = y[-i-1]
            y[i] = tail
            y[-i-1] = head
        for i in y:
            z = z + str(i)
        

    if x < 0:
        
        for i in range(int((len(y)-1)/2)):
            
            head = y[i+1]
            tail = y[-i-1]
            y[i+1] = tail
            y[-i-1] = head
        for i in y:
            z = z + str(i)
        
        
    
    if int(z) >= -(2^31) and int(z) <= (2^32)-1:
        print(int(z))
    else:
        print(0)

def main():
    reverse(12345)
    reverse(-123)
    reverse(1534236469)
    reverse(120)
    reverse(1)
    reverse(0)
    z = 3147483652
    if int(z) >= -(2**31) and int(z) <= (2**32)-1:
        print(int(z))
    else:
        print(0)
   


if __name__ == '__main__':
    main()
 

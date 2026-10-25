def is_prime(num):
    list = [2,3,5,7]
    for divider in list:
        if(num in list):
            return True;
        if(num % divider ==0 ):
            print(divider % num)
            return False
    return True;
    
    
print(is_prime(2))    
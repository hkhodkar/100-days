def is_leap_year(year):
    divisible_to_four = year % 4;
    divisible_to_hundred = year % 100;
    divisible_to_four_hundred = year % 400;
    if divisible_to_four == 0 and divisible_to_hundred != 0 and  divisible_to_four_hundred == 0:
        return True
    else:
        return False
    
print(is_leap_year(2020))

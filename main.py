nric = input('Enter an NRIC number: ')

# Type your code below
sum = 0
digit_weight = [2, 7, 6, 5, 4, 3, 2]
prefixes = "STFG"
check_digit_ST = "JZIHGFEDCBA"
check_digit_FG = "XWUTRQPNMLK"
valid = False
if len(nric) == 9 and nric[0] in prefixes and nric[8].isalpha and nric[1:8].isdecimal:
    prefix, suffix, digits = nric[0], nric[8], nric[1:8]
    sum = int(digits[0])*digit_weight[0] + int(digits[1])*digit_weight[1] + int(digits[2])*digit_weight[2] + int(digits[3])*digit_weight[3] + int(digits[4])*digit_weight[4] + int(digits[5])*digit_weight[5] + int(digits[6])*digit_weight[6]
    if prefix in ['T', 'G']:
        sum += 4
    if prefix in ['S', 'T']:
        if suffix == check_digit_ST[sum % 11]:
            valid = True
    if prefix in ['F', 'G']:
        if suffix == check_digit_FG[sum % 11]:
            valid = True
if valid:
    print("NRIC is valid.")
else:
    print("NRIC is invalid.")
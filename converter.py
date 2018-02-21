
print "Give an integer from 1 to 1000000"
flag="False"
while flag=="False":
    num = input()
    if num >= 1 and num <= 1000000:
        flag = "True"
    else:
        print "Give an integer from 1 to 1000000"

if num > 0 and num <= 999:
    def val(n):
        if n == 1:
            rom = 'I'
            return rom
        if n == 4:
            rom = 'IV'
            return rom
        if n == 5:
            rom = 'V'
            return rom
        if n == 9:
            rom = 'IX'
            return rom
        if n == 10:
            rom = 'X'
            return rom
        if n == 40:
            rom = 'XL'
            return rom
        if n == 50:
            rom = 'L'
            return rom
        if n == 90:
            rom = 'XC'
            return rom
        if n == 100:
            rom = 'C'
            return rom
        if n == 400:
            rom = 'CD'
            return rom
        if n == 500:
            rom = 'D'
            return rom
        if n == 900:
            rom = 'CM'
            return rom

    def lastdigit(num02):
        num02 = num % 10
        num03 = num % 5
        if 9 > num02 > 5:
            return str('V' + 'I'*num03)
        elif num02 < 4:
            return str('I'*num03)
        else:
            return str(val(num02))

    k3 = lastdigit(num)

    def tensdigit(num12):
        num12 = num % 100 - num % 10
        num13 = num % 50
        if 90 > num12 > 50:
            return str('L' + 'X'*(num13/10))
        elif num12 < 40:
            return str('X'*(num13/10))
        else:
            return str(val(num12))

    k2 = tensdigit(num)

    def hundigit(num112):
        num112 = (num % 1000 - num % 100)
        num113 = num % 500
        if 900 > num112 > 500:
            return str('D' + 'C'*(num113/100))
        elif num112 < 400:
            return str('C'*(num113/100))
        else:
            return str(val(num112))

    k1 = hundigit(num)
    print "This number in latin is: "
    print '%s%s%s' %(k1,k2,k3)

elif num >= 1000 and num <= 1000000:
    from collections import OrderedDict
    def write_roman(num):

        roman = OrderedDict()
        roman[1000000] = "M_"
        roman[900000] = "C_M_"
        roman[500000] = "D_"
        roman[400000] = "C_D_"
        roman[100000] = "C_"
        roman[90000] = "X_C_"
        roman[50000] = "L_"
        roman[40000] = "X_L_"
        roman[10000] = "X_"
        roman[9000] = "I_X_"
        roman[5000] = "V_"
        roman[4000] = "I_V_"
        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"

        def roman_num(num):
            for r in roman.keys():
                x , y = divmod(num, r)
                yield roman[r] * x
                num -= (r * x)
                if num > 0:
                    roman_num(num)
                else:
                    break

        return "".join([a for a in roman_num(num)])

    print "This number in latin is: "
    print write_roman(num)

import random

letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

x = random.choice(letters)
lst = []
def list_append(x):
    for i in range(100):
        for j in range(100):
            lst.append(x)
            x = random.choice(letters)
    return(lst)

y = list_append(x)

flag2="False"
while flag2=="False":
    flag="False"
    print "Give a word with capital characters: "
    print "If you want to stop write: break "
    tmp = raw_input()
    if tmp == "break":
        flag2="True"

#anazita an iparxei lexi orizontia
    for i in range(len(tmp),10000):
        if len(tmp)==1:
            x = lst[i-len(tmp)]
            str2 = ''.join(x)
        if len(tmp)==2:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]
            str2 = ''.join(x)
        if len(tmp)==3:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]
            str2 = ''.join(x)
        if len(tmp)==4:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]
            str2 = ''.join(x)
        if len(tmp)==5:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]
            str2 = ''.join(x)
        if len(tmp)==6:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]+lst[i-len(tmp)+5]
            str2 = ''.join(x)
        if len(tmp)==7:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]+lst[i-len(tmp)+5]+lst[i-len(tmp)+6]
            str2 = ''.join(x)
        if len(tmp)==8:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]+lst[i-len(tmp)+5]+lst[i-len(tmp)+6]+lst[i-len(tmp)+7]
            str2 = ''.join(x)
        if len(tmp)==9:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]+lst[i-len(tmp)+5]+lst[i-len(tmp)+6]+lst[i-len(tmp)+7]+lst[i-len(tmp)+8]
            str2 = ''.join(x)
        if len(tmp)==10:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]+lst[i-len(tmp)+5]+lst[i-len(tmp)+6]+lst[i-len(tmp)+7]+lst[i-len(tmp)+8]+lst[i-len(tmp)+9]
            str2 = ''.join(x)
        if len(tmp)==11:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]+lst[i-len(tmp)+5]+lst[i-len(tmp)+6]+lst[i-len(tmp)+7]+lst[i-len(tmp)+8]+lst[i-len(tmp)+9]+lst[i-len(tmp)+10]
            str2 = ''.join(x)
        if len(tmp)==12:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]+lst[i-len(tmp)+5]+lst[i-len(tmp)+6]+lst[i-len(tmp)+7]+lst[i-len(tmp)+8]+lst[i-len(tmp)+9]+lst[i-len(tmp)+10]+lst[i-len(tmp)+11]
            str2 = ''.join(x)
        if len(tmp)==13:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]+lst[i-len(tmp)+5]+lst[i-len(tmp)+6]+lst[i-len(tmp)+7]+lst[i-len(tmp)+8]+lst[i-len(tmp)+9]+lst[i-len(tmp)+10]+lst[i-len(tmp)+11]+lst[i-len(tmp)+12]
            str2 = ''.join(x)
        if len(tmp)==14:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]+lst[i-len(tmp)+5]+lst[i-len(tmp)+6]+lst[i-len(tmp)+7]+lst[i-len(tmp)+8]+lst[i-len(tmp)+9]+lst[i-len(tmp)+10]+lst[i-len(tmp)+11]+lst[i-len(tmp)+12]+lst[i-len(tmp)+13]
            str2 = ''.join(x)
        if len(tmp)==15:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+1]+lst[i-len(tmp)+2]+lst[i-len(tmp)+3]+lst[i-len(tmp)+4]+lst[i-len(tmp)+5]+lst[i-len(tmp)+6]+lst[i-len(tmp)+7]+lst[i-len(tmp)+8]+lst[i-len(tmp)+9]+lst[i-len(tmp)+10]+lst[i-len(tmp)+11]+lst[i-len(tmp)+12]+lst[i-len(tmp)+13]+lst[i-len(tmp)+14]
            str2 = ''.join(x)


#anazita an iparxei lexi katheta
    for i in range(len(tmp),9900):
        if len(tmp)==1:
            x = lst[i-len(tmp)]
            str2 = ''.join(x)
        if len(tmp)==2:
            x = lst[i-len(tmp)]+lst[i-len(tmp)+100]
            str2 = ''.join(x)
        if len(tmp)==3:
            if i<9800:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]
                str2 = ''.join(x)
        if len(tmp)==4:
            if i<9700:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]
                str2 = ''.join(x)
        if len(tmp)==5:
            if i<9600:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]
                str2 = ''.join(x)
        if len(tmp)==6:
            if i<9500:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]+lst[i-len(tmp)+500]
                str2 = ''.join(x)
        if len(tmp)==7:
            if i<9400:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]+lst[i-len(tmp)+500]+lst[i-len(tmp)+600]
                str2 = ''.join(x)
        if len(tmp)==8:
            if i<9300:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]+lst[i-len(tmp)+500]+lst[i-len(tmp)+600]+lst[i-len(tmp)+700]
                str2 = ''.join(x)
        if len(tmp)==9:
            if i<9200:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]+lst[i-len(tmp)+500]+lst[i-len(tmp)+600]+lst[i-len(tmp)+700]+lst[i-len(tmp)+800]
                str2 = ''.join(x)
        if len(tmp)==10:
            if i<9100:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]+lst[i-len(tmp)+500]+lst[i-len(tmp)+600]+lst[i-len(tmp)+700]+lst[i-len(tmp)+800]+lst[i-len(tmp)+900]
                str2 = ''.join(x)
        if len(tmp)==11:
            if i<9000:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]+lst[i-len(tmp)+500]+lst[i-len(tmp)+600]+lst[i-len(tmp)+700]+lst[i-len(tmp)+800]+lst[i-len(tmp)+900]+lst[i-len(tmp)+1000]
                str2 = ''.join(x)
        if len(tmp)==12:
            if i<8900:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]+lst[i-len(tmp)+500]+lst[i-len(tmp)+600]+lst[i-len(tmp)+700]+lst[i-len(tmp)+800]+lst[i-len(tmp)+900]+lst[i-len(tmp)+1000]+lst[i-len(tmp)+1100]
                str2 = ''.join(x)
        if len(tmp)==13:
            if i<8800:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]+lst[i-len(tmp)+500]+lst[i-len(tmp)+600]+lst[i-len(tmp)+700]+lst[i-len(tmp)+800]+lst[i-len(tmp)+900]+lst[i-len(tmp)+1000]+lst[i-len(tmp)+1100]+lst[i-len(tmp)+1200]
                str2 = ''.join(x)
        if len(tmp)==14:
            if i<8700:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]+lst[i-len(tmp)+500]+lst[i-len(tmp)+600]+lst[i-len(tmp)+700]+lst[i-len(tmp)+800]+lst[i-len(tmp)+900]+lst[i-len(tmp)+1000]+lst[i-len(tmp)+1100]+lst[i-len(tmp)+1200]+lst[i-len(tmp)+1300]
                str2 = ''.join(x)
        if len(tmp)==15:
            if i<8600:
                x = lst[i-len(tmp)]+lst[i-len(tmp)+100]+lst[i-len(tmp)+200]+lst[i-len(tmp)+300]+lst[i-len(tmp)+400]+lst[i-len(tmp)+500]+lst[i-len(tmp)+600]+lst[i-len(tmp)+700]+lst[i-len(tmp)+800]+lst[i-len(tmp)+900]+lst[i-len(tmp)+1000]+lst[i-len(tmp)+1100]+lst[i-len(tmp)+1200]+lst[i-len(tmp)+1300]+lst[i-len(tmp)+1400]
                str2 = ''.join(x)



        if str2 == tmp:
            flag="True"
    if tmp!="break":
        if flag=="True":
            print "There are this word:", tmp , "\n\n\n"
        else:
            print "There are NOT this word!! \n\n\n"

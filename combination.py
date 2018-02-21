import random

numbers = []
for i in range(30):
    numbers.append(random.randrange(-30,30))

flag="False"
for i in numbers:
    for j in numbers:
        for k in numbers:
            if (i+j+k) == 0:
                print "The combination is:"
                print i,j,k
                print "The sum of combination is:"
                print i+j+k
                print 10* "_"
                flag="True"

if flag == "False":
    print "There is not such combination"

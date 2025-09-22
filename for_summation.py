#for Summation code here
final_num = 0
num = int(input("number"))
num2 = num
while num2 > 0:
    num = num + (num2 -1)
    num2 = num2 -1
print(num)
num = int(input("number"))
for x in range(1,num+1,1):
    final_num += x
print(final_num)

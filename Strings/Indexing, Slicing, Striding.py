digits = [0,1,2,3,4,5,6,7,8,9]
name = 'Israel Abraham'

print(name[:6])
print(digits[5::-2])


for i in range(len(digits)):
    print(digits[0:i])


windows_size = 7
for i in range(len(digits)-(windows_size-1)):
    print(digits[i:i+windows_size]) #dynamic slicing scheme

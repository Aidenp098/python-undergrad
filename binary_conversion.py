# Problem 13
def BinToDec(binary_in):
    decimal_out = 0
    for position in range(0, len(binary_in)):
        decimal_out = decimal_out + binary_in[len(binary_in)-position-1] * (2**position)
    return decimal_out

binary_in = [1,1,1,0]
print(BinToDec(binary_in))


# Problem 14
def ParityParty(d):
    bin_list = []

    if(d%2==0):
        bin_list.append(0)
        
        num = d // 2
        bin_list.append(num)
    else:
        bin_list.append(1)
        
        num = (d-1) // 2
        bin_list.append(num)
    
    return bin_list
        

print(ParityParty(0))
print(ParityParty(10))
print(ParityParty(33))



# Problem 15
def DecToBin(d):
    bin_list = []
    flag = True
    
    if(d == 0):
        bin_list.append(0)
        return bin_list
    else:
        while(flag):
            if(d == 0):
                break
            elif(d%2==0):
                bin_list.append(0)
                d = d // 2
            else:
                bin_list.append(1)
                d = (d-1) // 2
        
        return bin_list[::-1]
    
print(DecToBin(0))
print(DecToBin(10))
print(DecToBin(241))
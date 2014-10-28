def isPrime(num):
    for i in range(2,num//2):
        if(num%i==0):
            return False
    return True

def main():
    mappy = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    }

    total = ""
    for i in range(1,1001):
        temp = str(i)
        if(len(temp)==4):
            total+="onethousand"
            break
        elif(len(temp)==3):
            total+=mappy[int(temp[0])]+"hundred"
            if(temp[1]!="1" and temp[1]!="0"):
                total+="and"
                total+=mappy[int(temp[1]+"0")]
                total+="" if temp[2]=="0" else mappy[int(temp[2])]
            elif(temp[2]!="0" or temp[1]!="0"):
                total+="and"
                total+=mappy[int(temp[1]+temp[2])]
        elif(len(temp)==2):
            if(temp[0]!="1"):
                total+="" if temp[0]=="0" else mappy[int(temp[0]+"0")]
                total+="" if temp[1]=="0" else mappy[int(temp[1])]
            else:
                total+=mappy[int(temp[0]+temp[1])]
        else:
            total+=mappy[int(temp[0])]
    print(len(total))

main()

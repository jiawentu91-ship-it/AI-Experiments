def codelength(ls):
    count = 0
    count1 = 0
    ls.append('0') 
    ls1 = []   
    for i in range(len(ls)-1):
        count1 = count1 + 1
        if ls[i+1] == ls[i]:                                                    
            count=count+1
        if count<=1 and ls[i+1] != ls[i]:
            ls1.extend(ls[i-count:i+1])
            count=0
        if count>1 and ls[i+1] != ls[i]:
            count1 = count1-count-1
            count=0
    print(f"长度为{count1},有效部分为{ls1}")

presses = [1,2,2,3,4,4,4,5,6]
codelength(presses)



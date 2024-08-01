def code(a):
    list=[ ]
    
    
    for i in range(1, 21) :
        for j in range (i+1, 21) :
            if a % (i + j) == 0 :        
                list.append(f"{i}{j}")

    result=' '.join(list)
    return result
for a in range(3, 21) :
    print(f"{a} - {code(a)}")
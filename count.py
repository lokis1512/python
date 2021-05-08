def count_occurance(n,div):
    counter = 0
    for i in range(1,n+1):
        if i%div==0: 
            counter +=1
    print(counter)            
count_occurance(100,5)

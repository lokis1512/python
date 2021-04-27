def count_occurance(n):
    counter = 0
    for i in range(1,n+1):
        if i%3==0: 
            counter +=1
    print(counter)            
count_occurance(100)

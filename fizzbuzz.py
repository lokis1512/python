def num():
    for i in range(1,16):
        if (i%3==0 and i%15==0):
            print(i,"fizzbuzz")
        elif i%3==0:
            print(i,"fizz")
        elif i%5==0:
    	    print(i,"buzz")
        else:
        	print(i)
        
num()

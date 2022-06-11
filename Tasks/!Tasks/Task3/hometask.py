while True:

    string_len = input("Enter the number of symbols in the string. It cannot be less than 36: ")    

    if not string_len.isdigit():
        print("The value is not a number or is not integer")
        continue

    string_len = int(string_len)

    if string_len < 35:
        print("incorrect value. The number cannot be less than 35")
        continue
    
    break
     
with open("text.txt", 'r') as f:
    line = f.readlines()
    with open("text_new.txt", 'w') as f:             
        result = ""
        count = 0         
        for i in line:
            for l in i.split():                 
                end_count = count + len(l)
                if count != 0:
                    end_count +=1
                if end_count >string_len:                                                 
                    result += "\n"                    
                    count = 0
                if count !=0:
                    result += " "
                    count += 1
                result += l
                count += len(l) 
        res1 = result.split("\n")                
        for j in res1:
            prob = j.count(" ")            
            if len(j) < string_len and prob !=0:              
                cel = (string_len-len(j))//prob
                ost = (string_len-len(j))%prob
                if cel > 0:
                    j = j.replace(" ",(" ")+(" ")*cel)                    
                if ost > 0:	
                    j = j.replace((" ")+(" ")*cel,(" ")+(" ")*cel+(" "),ost)                    
            j = j +"\n"                           
            f.writelines(j)        
print("The result is in a new file 'text_new.txt'")
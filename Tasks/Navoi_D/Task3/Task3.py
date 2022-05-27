with open("test.txt", 'r') as f:
     with open("test-Copy", 'w') as copy: 
        lim = int(input("Input maximum symbols in string:\n"))    
        if lim > 35 and lim < 50:        
            Current_Spaces1 = 0
            w = 0 
            single_list_words = []
            List_text = f.read().split()

            for d in List_text:
                if w + len(d) <= lim:
                 single_list_words.append(d)
                 w += len(d) + 1 
                else:
                    length = len(single_list_words)
                    count_places = length - 1
                     #distribution spaces 
                    Calculate_spaces = [0 for i in range(count_places)] 
                    i = 0
                    # the rest of spaces
                    Need_spaces = (lim - len(''.join(single_list_words))) 
                    
                    while Need_spaces != 0:
                        Calculate_spaces[i] += 1
                        Need_spaces -= 1
                        i += 1
                        if i == (count_places):
                            i = 0
                    # input spaces in list
                    spaces = [i*' ' for i in Calculate_spaces] 
                     # join string wthout rest spaces
                    k = '{}'.join(single_list_words)          
                      # fill the string with rest spaces
                    result_str = k.format(*spaces)           
                    copy.write(result_str + '\n')
                    single_list_words = [d] 
                    w = len(d)    
            
            if (len(single_list_words)): 
                copy.write(' '.join(single_list_words))   
        else: print("The number of symbols should be no more 50 and no less 35. Try again!")  
    
       
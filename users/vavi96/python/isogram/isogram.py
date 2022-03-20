def is_isogram(string):
    for i in range(len(string)):
      for j in range(len(string)):
       j=i+1 
       if string[i]==string[j] and string[i]!='-' and string[i]!=' '
        break
    return 'not isogram'  

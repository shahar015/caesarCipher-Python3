def caesarCipher(s, k):
    arr= list(s)
    for i in range (len(arr)):
        char = ord(arr[i])

        if(arr[i].isupper()):
            char+=k
            if(char>ord('Z')):
                char=ord('A')-1+((k-(ord('Z')-ord(arr[i])))%26)
                if((k-(ord('Z')-ord(arr[i])))%26==0):
                    char=ord('Z')
              
            if(char<ord('A')):
                char=ord('Z')+1-((k-(ord('Z')-ord(arr[i])))%26)
                if((k-(ord('Z')-ord(arr[i])))%26==0):
                    char=ord('A')
          
        if (arr[i].islower()):
            char+=k
            if(char>ord('z')):
                char=ord('a')-1+((k-(ord('z')-ord(arr[i])))%26)
                if((k-(ord('z')-ord(arr[i])))%26==0):
                    char=ord('z')
              
            if(char<ord('a')):
              char=ord('z')+1-((k-(ord('z')-ord(arr[i])))%26)
              if((k-(ord('z')-ord(arr[i])))%26==0):
                char=ord('a')
                
        arr[i]=chr(char); 
    
    print ("".join(arr))
    return "".join(arr)    
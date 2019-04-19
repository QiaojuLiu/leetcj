#decodeString leetCode394

def decodeString(input_value):
    if '[' not in input_value:
        return input_value
    elif '[' in input_value:
        inverse_value=input_value[::-1]
        loc1=len(input_value)-inverse_value.find('[')-1
        loc2=input_value.find(']')
        temp=int(input_value[loc1-1])*input_value[loc1+1:loc2]
        input_value=input_value[:loc1-1]+temp+input_value[loc2+1:]
    return decodeString(input_value)
        
    

    

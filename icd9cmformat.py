def icd9cmformat(code):
    if code[0].upper() == 'E':
        try:
            if len(code) == 5 and code[4] == '':
                pass
            else:
                return code[:3]+"."+code[3:10]
        except:
            return code
    if code[0].upper() == 'V':
        return code[:2]+"."+code[2:10]
    if len(code) == 4: 
        return str(code[:3]+'.'+code[3:20])
    if len(code) == 5: 
        return str(code[:3]+'.'+code[3:20])
    else:
        return code

    

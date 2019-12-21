

def icd9cmformat(code):
    code = code.strip()
    if '.' in code:
        return code
    elif code[0].upper() == 'E':
            if len(code) == 5:
                return code[:4]+"."+code[4:5]
            else:
                return code+'.'
    elif code[0].upper() == 'V':
        return code[:3]+"."+code[3:5]
    elif len(code) == 3:
        return code+'.'
    elif len(code) == 4 or len(code) == 5: 
        return str(code[:3]+'.'+code[3:5])
    else:
        return "Not recognized"
    
    
# Testing codes and their values

testecode = "E0008"
correctecode = "E000.8" 

testecode2 = "E8810"
correctecode2 = "E881.0"

testvcode = "V7612"
correctvcode = "V76.12" 


test4code = "7701"
correct4code = "770.1" 

test5code = "76072"
correct5code = "760.72" 

testinvalidcode = "12345X"
correctinvalidcode = "Not recognized" 

testperiod = "456.78"
correctperiod = "456.78"

testspace = " 456.78 "
correctspace = "456.78"

# Create dict of codes to test
# The test codes are the keys, the correct ones are the values
testingcodes = {}

testingcodes[testecode] = correctecode
testingcodes[testvcode] = correctvcode
testingcodes[test4code] = correct4code
testingcodes[test5code] = correct5code
testingcodes[testecode2] = correctecode2
testingcodes[testinvalidcode] = correctinvalidcode
testingcodes[testperiod] = correctperiod
testingcodes[testspace] = correctspace


## Running the tests
for key, value in testingcodes.items():
    print(icd9cmformat(key))
    if value == icd9cmformat(key):
        print("Pass")
    else:
        print("Fail")

## Another way to run all the tests at once
## Create a new dict of the keys from testingcodes and the results of the icd9cmformat function
applied_lambda = dict(map(lambda item: (item[0], icd9cmformat(item[1])), testingcodes.items()))

## test to see if the output of the function mapped onto the dictionary is identical to the dict of tests->correct answers
for i in range(0,1):
    if applied_lambda == testingcodes:
        print("All tests have passed")
    else:
        print("Some tests failed")

       
        
    

#returns the real part and the imaginary part as a whole
#it's a complex number as a list

def createComplex (real = 0, imaginary = 0):
    return [real,imaginary]

#gets the real part of the complex number

def getReal (complexl):
    return complexl[0]

#gets the imaginary part of the complex number

def getImaginary (complexl):
    return complexl[1]

#sets or modifies the real part of the complex number

def setReal(complexl,realPart):
    complexl[0]=realPart

#sets or modifies the imaginary part of the complex number
    
def setImaginary(complexl,imaginaryPart):
    complexl[1]=imaginaryPart

#prints a single complex number
                
def printOne(complexl):
    if getReal(complexl) == 0:
        print (str(getImaginary(complexl)) + 'i')
    elif getImaginary(complexl) == 0:
        print (str(getReal(complexl)))
    elif getImaginary(complexl) == 1:
        print (str(getReal(complexl)) + '+' + 'i')
    elif complexl[1]>0:
        print (str(getReal(complexl)) + '+' + str(getImaginary(complexl)) + 'i')
    else:
        print (str(getReal(complexl)) + str(getImaginary(complexl)) + 'i')

#prints all the complex numbers in the list
        
def printThelist(listc):
    for it in range(0,len(listc)):
        printOne(listc[it])

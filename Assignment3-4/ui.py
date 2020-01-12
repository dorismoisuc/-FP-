from model import *
from copy import * 
from undo import *

#reads the real part and the imaginary part of the complex number

def readComplex():
    realPart = int(input(" ⁂ real part:"))
    complexPart = int(input(" ⁂ complex part:"))
    return createComplex(realPart,complexPart)


#creates the list of the complex numbers

def createComplexList(listc):
    inputString = ''
    print(" ⋆ Insert a real part and a complex part:")
    print(" ⋆ Type 'done' to finish inserting")
    while inputString != 'done':
        inputString = input("** ")
        if inputString != 'done':
            try:
                    listc.append(readComplex())
            except ValueError:
                print(" ✁ Invalid input. Retry")
    


#inserts a complex number at a certain position
        
def insertNumber(listc):
    position = int(input(" ⋆ Enter the position "))
    if position > len(listc):
        raise Exception("The position is not in the list. Try again")
    else:
        position = position + 1
        realPart = int(input(" ⁂ real part:"))
        imaginaryPart = int(input(" ⁂ complex part:"))
        complexInsert =  createComplex(realPart,imaginaryPart)
        listc.insert(position,complexInsert)

#removes a complex number from a certain single position
    
def removeSingle(listc):
    position=int(input(" ⋆ The position you want to remove is: "))
    if position > len(listc):
        raise Exception("The position is not in the list. Try again")
    else:
        del listc[position]

#removes more than 1 complex number from given positions
    
def removeMore(listc):
    startPosition = int(input(" ⋆ The start position for removal is: "))
    endPosition = int(input(" ⋆ The end position for removal is: "))
    if int(endPosition) > len(listc):
        raise Exception(" ⋆ The end position doesn't exist in this list. Try again")
    else:
        endPosition = endPosition + 1
        del listc[startPosition:endPosition]

#replaces a complex number

def replace(listc):
    realOld = int(input(" ⋆ The real part of the complex number you want to replace is:"))
    imaginaryOld = int(input(" ⋆ The imaginary part of the complex number you want to replace is: "))
    realNew = int(input(" ⋆ The real part of the replacement is: "))
    imaginaryNew = int(input(" ⋆ The imaginary part of the replacement is: "))
    for it in range (0,len(listc)):
        #print ("the real part is ",getReal(listc[it]))
        #print ("the imaginary part is ",getImaginary(listc[it]))
        #print ("realOld ",realOld)
        #print ("imagOld ", imaginaryOld)
        #print ("realNew ",realNew)
        #print ("imaginaryNew ", imaginaryNew)
        if getReal(listc[it]) == realOld and getImaginary(listc[it]) == imaginaryOld:
            setReal(listc[it],realNew)
            setImaginary(listc[it],imaginaryNew)
            
    
#lists the complex numbers with no imaginary part
#from a start position to an end position
    
def listReal(listc):
    startPoz = int(input(" ⋆ List real numbers from: "))
    endPoz = int(input("To: "))
    if int(endPoz) > len(listc):
        raise Exception(" ⋆ The end position doesn't exist in this list. Try again")
    else:
        endPoz = endPoz + 1
        for it in range(startPoz,endPoz):
        #print ("the imaginary part is ",getImaginary(listc[it]))
        #print ("the real part is ",getReal(listc[it]))
            if (getImaginary(listc[it]) == 0):
                print (getReal(listc[it]))

#gets the modulus of the complex number
            
def getModulus(listc):
    return (getReal(listc)**2 + getImaginary(listc)**2)**0.5

#prints the list of complex numbers which have the modulus equal to an input modulus

def listModuloEq(listc):
    eqModulo = int(input(" ⋆ List complex numbers which have the mod equal to:"))
    for it in range(0,len(listc)):
        if getModulus(listc[it]) == eqModulo:
            print (str(getReal(listc[it])) + '+' + str(getImaginary(listc[it])) + 'i')

#prints the list of complex numbers which have the modulus more little than an input modulus
            
def listModuloLittle(listc):
    eqModulo = int(input(" ⋆ List complex numbers which have the mod more little than:"))
    for it in range(0,len(listc)):
        if getModulus(listc[it]) < eqModulo:
            print (str(getReal(listc[it])) + '+' + str(getImaginary(listc[it])) + 'i')

#prints the list of complex numbers which have the modulus bigger than an input modulus
            
def listModuloBigger(listc):
    eqModulo = int(input(" ⋆ List complex numbers which have the modulo bigger than:"))
    for it in range(0,len(listc)):
        if getModulus(listc[it]) > eqModulo:
            print (str(getReal(listc[it])) + '+' + str(getImaginary(listc[it])) + 'i')

def suma(listc):
    startPos = int(input("The start pos of the sum is: "))
    endPos = int(input("The end pos: "))
    sum = 0
    if endPos > len(listc):
        raise Exception("The end pos is not in the list")
    else:
        endPos = endPos + 1
        for it in range(startPos,endPos):
            sum = sum + getReal(listc[it]) + getImaginary(listc[it])
            
        print ("The sum is: ",sum)

def product(listc):
    startPos = int(input("The start pos of the product is: "))
    endPos = int(input("The end pos: "))
    prod = 1
    if endPos > len(listc):
        raise Exception("The end pos is not in the list")
    else:
        endPos = endPos + 1
        for it in range(startPos,endPos):
            prod = prod * getReal(listc[it]) * getImaginary(listc[it])
            
        print ("The product is: ",prod)

def filterReal(listc):
    if len(listc) ==0:
        raise Exception("The list is empty")
    for it in range(len(listc)-1, -1, -1):
        if getImaginary(listc[it]) !=0:
            del listc[it]

def filterModl(listc):
    if len(listc) ==0:
        raise Exception("The list is empty")
    theVal = int(input("The value the modulus is < than: "))
    for it in range(len(listc)-1,-1,-1):
        if getModulus(listc[it]) > theVal:
            del listc[it]

def filterMode(listc):
    if len(listc) ==0:
        raise Exception("The list is empty")
    theVal = int(input("The value the modulus is equal to: "))
    for it in range(len(listc)-1,-1,-1):
        if getModulus(listc[it]) != theVal:
            del listc[it]

def filterModg(listc):
    if len(listc) ==0:
        raise Exception("The list is empty")
    theVal = int(input("The value the modulus is > than: "))
    for it in range(len(listc)-1,-1,-1):
        if getModulus(listc[it]) < theVal:
            del listc[it]
        
def undoOp(listH):
    listH.pop()
    
    
def run():
    listc = [[1,2],[3,4],[5,6],[0,1],[1,0],[2,3],[4,5],[5,0],[1,1],[2,3],[5,6]]
    listH=[]
    copyL=[]
    commands = {
        "list": printThelist,
        "add": createComplexList,
        "insert": insertNumber,
        "removeOne": removeSingle,
        "removeMany": removeMore,
        "replace": replace,
        "listReal":listReal,
        "listEqualMod":listModuloEq,
        "listLittleMod":listModuloLittle,
        "listBiggerMod":listModuloBigger,
        "sum":suma,
        "product":product,
        "filterReal":filterReal,
        "filterModL":filterModl,
        "filterModE":filterMode,
        "filterModG":filterModg,
        "undo":undoOp
    }
    while True:
        cmd = input("*")
        if cmd == "exit":
            return
        if cmd in commands:
            try:
                commands[cmd](listc)
            except Exception as ex:
                print(str(ex))
        else:
            print ("non-existent command!")

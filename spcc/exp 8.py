print("\nADVAIT CHANDORKAR ; TEB-224\n")
from sys import exit
motOpCode = ["MOV", "ADD", "SUB", "MUL", "DIV", "AND", "OR",
             "LOAD", "STORE", "DCR", "INC", "JMP", "JNZ", "HALT"]
keywords = ["MACRO", "CONST", "DOUBLE", "INT", "FLOAT", "SHORT", "LONG", "STRUCT", "IF", "ELSE", "FOR", "SWITCH",
            "CASE", "CHAR", "RETURN", "PRINTF", "SCANF", "AX", "BX", "CX", "DX", "AH", "BH", "CH", "DH", "AL", "BL", "CL", "DL"]

firstMacroDefinition = []
secondMacroDefinition = []
sourceCode = []
macroNames = []
firstOutputSourceCode = []
outputSourceCode = []
values = []
tc = 0
mc = 0
nmc = 0

sc = int(input(
    "Enter the no of instructions for input source code with first level of macro call: "))
for i in range(sc):
    temp = input("Enter instruction {} : ".format(i+1)).upper()
    sourceCode.append(temp)

fmc = int(input("Enter the no of instructions for first level of macro definition: "))
for i in range(fmc):
    temp = input("Enter instruction {} : ".format(i+1)).upper()
    firstMacroDefinition.append(temp)

if firstMacroDefinition[0] == "MACRO" and firstMacroDefinition[-1] == "MEND" and (firstMacroDefinition[1] not in keywords) and (firstMacroDefinition[1] not in motOpCode):
    macroNames.append(firstMacroDefinition[1])
else:
    print("Invalid Macro Definition.")
    exit(0)

smc = int(input("Enter the no of instructions second level macro definition : "))
for i in range(smc):
    temp = input("Enter instruction {} : ".format(i+1)).upper()
    secondMacroDefinition.append(temp)

if secondMacroDefinition[0] == "MACRO" and secondMacroDefinition[-1] == "MEND":
    temp = secondMacroDefinition[1]
    macroName, argName = temp.split()
    if macroName not in keywords and macroName not in motOpCode:
        macroNames.append(macroName)
else:
    print("Invalid Macro Definition.")
    exit(0)

for i in range(sc):
    if sourceCode[i] in macroNames[0]:
        mc += 1
        for k in range(2, fmc-1):
            temp = firstMacroDefinition[k]
            firstOutputSourceCode.append(temp)
    else:
        temp = sourceCode[i]
        firstOutputSourceCode.append(temp)

print("First level expanded code is : ")
for i in range(len(firstOutputSourceCode)):
    print(firstOutputSourceCode[i])

for i in range(len(firstOutputSourceCode)):
    if macroNames[1] in firstOutputSourceCode[i]:
        nmc += 1
        temp = str(firstOutputSourceCode[i])
        macroName, argValue = temp.split()
        if argValue not in values:
            values.append(argValue)
        for j in range(2, smc-1):
            if argName in secondMacroDefinition[j]:
                temp = secondMacroDefinition[j]
                opCode, value = temp.split()
                temp = temp.replace(argName, argValue)
            outputSourceCode.append(temp)
    else:
        temp = firstOutputSourceCode[i]
        outputSourceCode.append(temp)

print("Expanded code is : ")
for i in range(len(outputSourceCode)):
    print(outputSourceCode[i])
    tc += 1

print("Number of instructions ininput source code (excluding macro call) is : {} ".format(sc-1))
print("Number of Macro calls at first level : {}".format(mc))
print("Number of instructions & other macro calls defined in the first level Macro call : {}, {} ".format(fmc-3-nmc, nmc))
print("Total number of instructions in the final expanded source code : {}".format(tc))
print("\nADVAIT CHANDORKAR ; TEB-224\n")
code = ['MOV R','RAHUL 30,40,50','DCR R','AND R','RAHUL 33,44,55','MUL 88','HALT']
macro = ['MACRO','RAHUL &ARG1,&ARG2,&ARG3','ADD &ARG1','SUB &ARG2','OR &ARG3','MEND']
macrol = []
codel = []
argl = []
macrocount = 0
for x in macro:
 macrol.append(x.removesuffix(' \n').upper())
macroname = macrol[macrol.index('MACRO')+1]
macrol.remove(macroname)
macrol.remove('MACRO')
macrol.remove('MEND')
macroname = macroname.split()[0]
def callMacro(arg, macrol):
 temp = []
 for i in macrol:
    a = i.split()
    a[1] = arg 
    temp.append(' '.join(a))
 print(temp)
 return tuple(temp)
for x in code:
 codel.append(x.removesuffix(' \n'))
codelen = len(codel)
for i in range(len(codel)):
 a = codel[i].split()
 if a[0] == macroname:
    codel[i : i+len(macrol)-2] = callMacro(a[1],macrol)
    argl.append(a[1])
    macrocount += 1
print("\nEvaluated Program: ")
for i in codel:
 print(i)
print("\n\nStatistical Output")
print("Number of instructions in input source code (excluding Macro calls) = {}".format(codelen - macrocount))
print("Number of Macro calls = {}".format(macrocount))
print("Number of instructions defined in the Macro call = {}".format(len(macrol)))
for i,data in enumerate(argl):
 print("Actual argument during Macro call {} = {}".format(i+1,data))
print("Total number of instructions in the expanded source code = {}".format(len(codel)))
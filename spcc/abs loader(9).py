mnemonics_arr = ["MOV R", "ADD R", "SUB R", "MUL R", "DIV R", "AND R", "OR R", "ADD", "SUB", "MUL", "DIV", "AND", "OR", "LOAD", "STORE", "DCRR", "INCR", "JMP", "JNZ", "HALT"]
size_arr = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 1, 1, 3, 3, 1] 
opcode_arr = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
source_code = []
alp_instruct = []
obj_code = []
absolute_addr_arr = []
absolute_addr = 1000
obj_index=0
print('Enter source code: ')
cmd = input()
source_code.append(cmd)

while source_code[-1] != 'HALT':
    cmd = input()
    source_code.append(cmd)

for code in source_code:
    mnemonic = 0
    code_arr = code.split(' ')
    if (code_arr[0] == 'ADD' or code_arr[0] == 'SUB' or code_arr[0] == 'MUL' or code_arr[0] == 'DIV' or code_arr[0] == 'AND' or code_arr[0] == 'OR') and code_arr[1] != 'R':
        for mnemonic in range(len(mnemonics_arr)):
            if mnemonics_arr[mnemonic] == code_arr[0]:
                obj_code.append(opcode_arr[mnemonic])
                absolute_addr +=1
                absolute_addr_arr.append(absolute_addr)
                alp_instruct.append(code)

                absolute_addr+=1
                obj_code.append(code_arr[1])
                absolute_addr_arr.append(absolute_addr)
                alp_instruct.append('       ')

    elif (code_arr[0] == 'STORE' or code_arr[0] == 'LOAD' or code_arr[0] == 'JMP' or code_arr[0] == 'JNZ'):
        addr1 = ''
        addr2 = ''
        for k in range(0, len(code_arr[1])):
            if(k == 0 or k == 1):
                addr1 = addr1 + code_arr[1][k]
            if(k == 2 or k == 3):
                addr2 = addr2 + code_arr[1][k]
        for mnemonic in range(len(mnemonics_arr)):
            if mnemonics_arr[mnemonic] == code_arr[0]:
                obj_code.append(opcode_arr[mnemonic])
                absolute_addr+=1
                absolute_addr_arr.append(absolute_addr)
                alp_instruct.append(code)

                absolute_addr+=1
                obj_code.append(addr1)
                absolute_addr_arr.append(absolute_addr)
                alp_instruct.append('       ')

                absolute_addr+=1
                obj_code.append(addr2)
                absolute_addr_arr.append(absolute_addr)
                alp_instruct.append('       ')

    else:
        for mnemonic in range(len(mnemonics_arr)):
            if mnemonics_arr[mnemonic] == code:
                obj_code.append(opcode_arr[mnemonic])
                absolute_addr+=1
                alp_instruct.append(code)
                absolute_addr_arr.append(absolute_addr)


print("Absolute Address                         Object Code                             ALP Instruction ")
for table in range(len(obj_code)):
    print(absolute_addr_arr[table], "                                        ", obj_code[table],"                                      ",alp_instruct[table])








'''    [ADD 20
MOV R
OR 55
MUL R
STORE 2000
HALT]              press enter'''

    

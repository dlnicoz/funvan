

mnemonics = ["MOVR", "ADDR", "SUBR", "MULR", "DIVR", "ANDR", "ORR", "ADD", "SUB", "MUL", "DIV", "AND", "OR", "LOAD", "STORE", "DCRR", "INCR", "JMP", "JNZ", "HALT"]
size = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 1, 1, 3, 3, 1] 
opcode = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
instruction = []
relative_addr = 0
machine_code = []
relative_addr_arr = []
flag = 0

while flag == 0:
    instruct = input("Enter the instruction or HALT to end the program: ")
    instruction.append(instruct)
    for i in range(0, len(mnemonics)):
        if(instruct == mnemonics[i]):
            relative_addr_arr.append(relative_addr)
            relative_addr += size[i]
            if(instruct == 'ADD' or instruct == 'SUB' or instruct == 'MUL' or instruct == 'DIV' or instruct == 'AND' or instruct == 'OR'):
                data = input("Enter data for " + instruct + "(4byte): ")
                opcode_gen = opcode[i] + ',' + data
                machine_code.append(opcode_gen)
            elif(instruct == 'STORE' or instruct == 'LOAD' or instruct == 'JMP' or instruct == 'JNZ'):
                address = input("Enter address for " + instruct + "(8byte): ")
                addr1 = ''
                addr2 = ''
                for k in range(0, len(address)):
                    if(k == 0 or k == 1):
                        addr1 = addr1 + address[k]
                    if(k == 2 or k == 3):
                        addr2 = addr2 + address[k]
                opcode_addr_gen = opcode[i] + ',' + addr1 + ',' + addr2
                machine_code.append(opcode_addr_gen)        
            else:
                machine_code.append(opcode[i])
    if instruct == 'HALT':
        flag = 1
            
print("Relative Address                         Instruction                             Machine Code")
for i in range(len(instruction)):
    print(relative_addr_arr[i], "                                        ", instruction[i],"                                      ",machine_code[i])

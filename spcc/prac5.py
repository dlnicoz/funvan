macro_def = []
source_code = []
extended_source_code = []

print("Enter Macro Command: ")
macro_cmd = input()
macro_def.append(macro_cmd)

while macro_def[-1] != 'MEND':
    macro_cmd = input()
    macro_def.append(macro_cmd)
macro_name, param = macro_def[1].split()

print("Enter Source Code: ")
command = input("")
source_code.append(command)

while source_code[-1] != 'HALT':
    command = input()
    source_code.append(command)

for ext_cmd in range(len(source_code)):
    if source_code[ext_cmd].startswith(macro_name):
        macro_arg = source_code[ext_cmd].split()[1]
        macro_cmd = 0
        for mac_cmd in range(len(macro_def)):
            if macro_def[mac_cmd] == 'MACRO' or macro_def[mac_cmd] == 'MEND' or macro_def[mac_cmd].startswith(macro_name):
                pass
            else:
                expanded_cmd = macro_def[mac_cmd].replace(param, macro_arg)
                extended_source_code.append(expanded_cmd)
    else:
        extended_source_code.append(source_code[ext_cmd])

print('**********Extended Source Code**************')
for code in extended_source_code:
    print(code)
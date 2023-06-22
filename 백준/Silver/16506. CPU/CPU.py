N =  int(input())
opcode_dict = {
    "ADD": "0000",
    "SUB": "0001",
    "MOV": "0010",
    "AND": "0011",
    "OR": "0100",
    "NOT": "0101",
    "MULT": "0110",
    "LSFTL": "0111",
    "LSFTR": "1000",
    "ASFTR": "1001",
    "RL": "1010",
    "RR": "1011"
}

def opTomachine(opcode):
    if opcode in opcode_dict:
        return(opcode_dict[opcode])
   
ans_list = []     

for i in range(N):
    machine_code = ''
    opcode, rD, rA, last  =  input().split()
    Cflag = False
    
    if opcode[-1] == "C":
        machined_opcode = opTomachine(opcode[0:-1])
        Cflag = True
    else:
        machined_opcode = opTomachine(opcode)
    
    if machined_opcode == ("0010" or "0101"):
        rA = "000"

    machine_code += machined_opcode
    
    if opcode[-1] == "C":
        machine_code += '1'
    else:
        machine_code += '0'
   
    #bit 5 change
    machine_code += '0'
    
    #rD change
    machine_code += format(int(rD), 'b').zfill(3)
    
    #rAchange
    machine_code += format(int(rA), 'b').zfill(3)
    
    if Cflag == True:
        machine_code += format(int(last), 'b').zfill(4)
    else:
        machine_code += format(int(last), 'b').zfill(3)
        machine_code += '0'
        
    ans_list.append(machine_code)
    
for ans in ans_list:
    print(ans)
    
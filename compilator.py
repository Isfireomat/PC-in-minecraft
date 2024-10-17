from memoryMainList import memoryMainList,memoryProgramList
from comands import comands,comands_type,numbers,alphabet,binary_comands
from conf import size_list_byte,byte_lenght

def check(comand_line:list):

    if not (comand_line[0] in comands.keys()):
        raise TypeError("Comand is no exist")
    
    for i in zip(comands_type[comand_line[0]],comand_line[1:]):
        match i[0]:
            case "ind":
                if len(str(bin(int(i[1]))[2:]))>size_list_byte.bit_length()-1:
                    raise IndexError("Index is more then index bits")
            case "inf":
                if not (i[1] in numbers.keys() or 
                        i[1] in alphabet.keys()):
                    raise ValueError("Inf is not exists")

def translate(comand_line:list)->list:
    comand=comands[comand_line[0]]
    match len(comands_type[comand_line[0]]):
        case 1:
            pred_index=str(bin(int(comand_line[1]))[2:])
            information=(byte_lenght-len(pred_index))*"0"+pred_index
            print(comand_line,information)
            index=(size_list_byte.bit_length()-1)*"0"
        case 2:
            information={**numbers,**alphabet}[comand_line[1]]
            pred_index=str(bin(int(comand_line[2]))[2:])
            index=(size_list_byte.bit_length()-1-len(pred_index))*"0"+pred_index
    return comand,information,index
    
def compilate(program:str,memory:memoryProgramList)->None:
    program:list=[i.split() for i in program.strip().split('\n')]
    
    while memory.position_str_byte!="0"*(size_list_byte.bit_length()-1):
        memory.move_byte()
        
    for i,v in enumerate(program):
        if len(v)<3: program[i].extend(['0']*(3-len(v)))
        check(program[i])
        
        memory.memory_comands,memory.memory,memory.memory_index=translate(program[i])
        memory.move_byte()

def run(memory: memoryProgramList,second_memory:memoryMainList):
    position="0"*(size_list_byte.bit_length()-1)
    while memory.position_str_byte!=position:
        memory.move_byte()
    
    while int(memory.memory_comands):
        # print(memory.memory_comands,memory.memory,memory.memory_index)
        binary_comands[memory.memory_comands](second_memory,memory.memory,memory.memory_index)
        memory.move_byte()
    
    

if __name__=="__main__":
    memory=memoryProgramList()
    second_memory=memoryMainList()
    program="""
        mov в 13
        mov р 10
        mov п 0
        mov и 20
        mov е 14
        mov т 15
        mov 0 16
        prc 0
        prc 10
        prc 20
        prc 13
        prc 14
        prc 15
        prc 16
        pri 16
        pri 13
        pri 14
        """
    compilate(program,memory)
    print(memory)
    run(memory,second_memory)
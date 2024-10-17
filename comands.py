# Словарь команд с их значениями
from memoryMainList import memoryMainList,memoryProgramList

comands = {
    "stp": "00000000",  # остановиться  
    "mov": "00000001",  # поместить биты в индекс (mov 03 0) 
    "jmp": "00000010",  # перейти на определённый индекс (jmp 28)
    "prc": "00000011",  # вывести как букву (prs 0)
    "pri": "00000100"   # вывести как число от 0 до 9 (pri 0)
}

# Словарь типов команд
comands_type = {
    "stp": ['non'],   
    "mov": ['inf', 'ind'], 
    "jmp": ['ind'],
    "prc": ['ind'],
    "pri": ['ind']
}

# Словарь чисел с двоичными значениями
numbers = {
    "0": "00000000",
    "1": "00000001",
    "2": "00000010",
    "3": "00000011",
    "4": "00000100",
    "5": "00000101",
    "6": "00000110",
    "7": "00000111",
    "8": "00001000",
    "9": "00001001",
}

# Словарь русского алфавита с двоичными значениями
alphabet = {
    'а': "00000001",
    'б': "00000010",
    'в': "00000011",
    'г': "00000100",
    'д': "00000101",
    'е': "00000110",
    'ё': "00000111",
    'ж': "00001000",
    'з': "00001001",
    'и': "00001010",
    'й': "00001011",
    'к': "00001100",
    'л': "00001101",
    'м': "00001110",
    'н': "00001111",
    'о': "00010000",
    'п': "00010001",
    'р': "00010010",
    'с': "00010011",
    'т': "00010100",
    'у': "00010101",
    'ф': "00010110",
    'х': "00010111",
    'ц': "00011000",
    'ч': "00011001",
    'ш': "00011010",
    'щ': "00011011",
    'ы': "00011100",
    'э': "00011101",
    'ю': "00011110",
    'я': "00011111",
    ' ': "00000000"
}

def move_to_index(memory:memoryMainList,index:str):
    while memory.position_str_byte!=index:
        memory.move_byte()

        
def mov(main_memory:memoryProgramList,memory:memoryMainList,information:str,index:str):
    move_to_index(memory,index)
    memory.memory=information

def prc(main_memory:memoryProgramList,memory:memoryMainList,information:str,index:str):
    move_to_index(memory,information[-len(index):])
    print(next((k for k,v in alphabet.items() if v==memory.memory),None))

def pri(main_memory:memoryProgramList,memory:memoryMainList,information:str,index:str):
    move_to_index(memory,information[-len(index):])
    print(next((k for k,v in numbers.items() if v==memory.memory),None))

def jmp(main_memory:memoryProgramList,memory:memoryMainList,information:str,index:str):
    while main_memory.position_str_byte!=information[-len(index):]:
        main_memory.move_byte()
    
binary_comands={
    "00000000":"stop",
    "00000001":mov,
    "00000010":jmp,
    "00000011":prc,
    "00000100":pri
}

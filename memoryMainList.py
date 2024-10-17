from conf import size_list_byte,byte_lenght

class memoryMainList:
    __memory:list
    position_str_byte:str
    __position_number:int
    
    def __init__(self):
        self.__memory=["0"*byte_lenght]*size_list_byte
        self.position_str_byte="0"*(size_list_byte.bit_length()-1) 
    
        self.__position_number=0
    
    def __str__(self):
        print("=bits===|=int===")
        for i,v in enumerate(self.__memory):
            print(f"{v}:{i}")
        return "==============="
    
    @property
    def memory(self)->str:
        return self.__memory[self.__position_number]
    
    @memory.setter
    def memory(self,information:str)->None:
        if len(information)!=byte_lenght: return 
        self.__memory[self.__position_number]=information
    
    def move_byte(self)->str:
        tmp_position:list=list(self.position_str_byte[::-1])

        for i in range(len(tmp_position)):
            if tmp_position[i]=="0":
                tmp_position[i]="1"
                break
            else:
                tmp_position[i]="0"
        
        self.position_str_byte="".join(tmp_position)[::-1]
        self.__position_number=self.__position_number+1 if int(self.position_str_byte) else 0
        
        return self.position_str_byte
    
class memoryProgramList(memoryMainList):
    commands_memory:list
    def __init__(self):
        super().__init__()
        self.__memory_comands=["0"*byte_lenght]*size_list_byte
        self.__memory_index=["0"*(size_list_byte.bit_length()-1)]*size_list_byte
    
    @property
    def memory_index(self)->str:
        return self.__memory_index[self._memoryMainList__position_number]
    
    @property
    def memory_comands(self)->str:
        return self.__memory_comands[self._memoryMainList__position_number]
    
    @memory_index.setter
    def memory_index(self,other):
        self.__memory_index[self._memoryMainList__position_number]=other
    
    @memory_comands.setter
    def memory_comands(self,other):
        self.__memory_comands[self._memoryMainList__position_number]=other
        
    def __str__(self)->str:
        print("=========bits==========|=int====")
        for i,v in enumerate(zip(self.__memory_comands,self._memoryMainList__memory,self.__memory_index)):
            print(f"{v[0]}|{v[1]}|{v[2]}:{i}")
        return "==============================="
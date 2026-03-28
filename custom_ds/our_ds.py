class my_array():
    def __init__(self):
        self.data=[None]*1
        self.size=0
        self.capacity=1
    def append(self,x):
        if(self.size==self.capacity):
            self.resize()
        self.data[self.size]=x
        self.size+=1  
        return self.data
    def resize(self):
        self.capacity=self.capacity *2 
        new_data=[None]*self.capacity 
        for i in range((self.size)):
            new_data[i]=self.data[i]
        self.data=new_data        
    def get_index(self,x):
        # idx=0
        for i in range(self.size):
            if(self.data[i]==x):
                return i
        return -1
    
    def pop(self,idx):
        if(idx<0 or idx> self.size-1):
            return None
        popped_el=self.data[idx]
        for i in range (idx,(self.size)-1):  
            self.data[i]=self.data[i+1]
        self.data[self.size-1]=None    
        self.size-=1
        return popped_el       
       


        # return idx        


          
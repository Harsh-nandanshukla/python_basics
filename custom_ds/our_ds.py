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
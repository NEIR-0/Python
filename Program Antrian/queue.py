class Queue:
    def __init__(self):
        self.queue = []

    def eunqueue(self):
        # self.queue.append(item)
        self.queue.append(input("Massukkan nilai : "))

    def dequeue(self):
        if len(self.queue) < 1:
            print("\n-----------------\n")
            print("Antrian Kosong")
            print("\n-----------------")
            return None
        print("-----------------\n")
        print("Element paling depan " +'" '+ self.queue[0] +' "'+ " telah dihapus !!!")    
        print("\n-----------------")
        return self.queue.pop(0)

    def size(self):
        print("Banyak element pada queue : ",len(self.queue))   

    def ItsEmpty(self):
        if len(self.queue) < 1:
            print("Queue Its Empty")

        else:    
            print("Queue Not Empty")

    def peek(self):
        if len(self.queue) > 1:
            print("Element terakhir pada Queue : ",self.queue[-1])
        elif len(self.queue) == 1:
            print("Element terakhir pada Queue : ",self.queue[0])
        else:
            print("Antrian kosong")

    def display(self):
        print("Queue : ",self.queue)


class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 0
        for i in range(0,depth+1):
            tree_size=tree_size+2**i
        self.Tree = [None] * tree_size # массив ключей
	
    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        if key!=None and self.Tree[0]!=None:
            i=0
            while i<=len(self.Tree):
                node=self.Tree[i]
                if key>node:
                    i=2*i+2
                    if i>len(self.Tree):
                        return None
                    elif self.Tree[i]==None:
                        return -i
                elif key<node:
                    i=2*i+1
                    if i>len(self.Tree):
                        return None
                    elif self.Tree[i]==None:
                        return -i
                else:
                    return i                  
        else:
            return None # не найден
	
    def AddKey(self, key):
        # добавляем ключ в массив
        i=0
        if self.Tree[i]==None:
            self.Tree[i]=key
            return i
        while i<=len(self.Tree):
            if key < self.Tree[i]:
                i=i*2+1
                if i>len(self.Tree):
                    return -1
            elif key>self.Tree[i]:
                i=i*2+2
                if i>len(self.Tree):
                    return -1
            else:
                return i
            if self.Tree[i]==None:
                self.Tree[i]=key
                return i
            elif self.Tree[i]!=None:
                pass 
        return -1
        # индекс добавленного/существующего ключа или -1 если не удалось
"""
A=aBST(3)
print(A.AddKey(24))
print(A.AddKey(25))
print(A.AddKey(26))
print(A.AddKey(34))
print(A.AddKey(11))

print(A.FindKeyIndex(245))
#print(A.AddKey(14))
print(A.AddKey(7))
print(A.AddKey(9))
print(A.Tree)
print(A.FindKeyIndex(7))
print(A.FindKeyIndex(3))
print(A.FindKeyIndex(13))
"""

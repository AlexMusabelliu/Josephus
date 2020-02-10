class josephus:
  #inefficient code, decided to screw around with classes, made the code longer and less effective.  
    def fill(self):
        num = input("Number of People: ")
        j = 0
        while j == 0:
            try:
                int(num)
                j = 1
            except:
                num = input("Try again: ")
        
        else:
            for x in range(1, int(num) + 1):
                n.append(x)
        
        self.solve()   
            
    def solve(self):
        global n
        while len(n) != 1:
            for per in n:
                k = n.index(per) + 1
                if n.index(per) == len(n)-1:
                    k = 0
                n.pop(k)
                
        print(n)
    
    
n = []

josephus().fill()
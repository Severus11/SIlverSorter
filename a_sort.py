from queue import PriorityQueue
class state(object):
    def __init__(self, value, parent, start=0, goal=0, solver=0):
        self.children=[]
        self.parent= parent
        self.value= value
        self.dist=0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start= parent.start
            self.goal= parent.goal
            self.solver=parent.solver
        else:
            self.path= [value]
            self.start= start
            self.goal= goal
            self.solver= solver
    
    def GetDist(self):
        pass
    def createChild(self):
        pass

class state_string(state):
    def __init__(self, value, parent, start=0, goal=0):
        super(state_string,self).__init__(value, parent, start, goal)
        self.dist= self.GetDist()

    def GetDist(self):
        if self.value== self.goal:
            return 0
        dist=0
        for i in range(len(self.goal)):
            letter= self.goal[i]
            dist= dist + abs(i- self.value.index(letter))
        return  dist
    def createChild(self):
        if not self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val= val[:i] +val[i+1] + val[i]+ val[i+2:]
                child = state_string(val,self)
                self.children.append(child)
class A_solve:
    def __init__(self, start, goal):
        self.path=[]
        self.visitedQueue=[]
        self.priorityQueue= PriorityQueue()
        self.start= start
        self.goal = goal 
    def solve(self):
        startState= state_string(self.start, 0, self.start, self.goal)
        count=0
        self.priorityQueue.put((0,count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            closestChild= self.priorityQueue.get()[2]
            closestChild.createChild()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count = count+1
                    if not child.dist:
                        self.path =child.path 
                        break
                    self.priorityQueue.put((child.dist, count, child))
        if not self.path:
            print("goal of "+ self.goal +"not posssible")
        return self.path 

if __name__== "__main__":
    start1= input()
    goal1 = input()           
    a= A_solve(start1, goal1)
    a.solve()
    for i in range(len(a.path)):
        print ("%d)"%i + a.path[i])
    



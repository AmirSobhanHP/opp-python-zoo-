class cow:
    name = ""
    age = int()
    color = ""
    weight = int()
    def __init__(self,name,age,color,weight):
        self.name = name
        if age > 0:
            self.age = age
        else:
            raise ValueError
        self.color = color
        if weight > 0:
            self.weight = weight
        else:
            raise ValueError
    def eating(self,nameOfFood):
        return f"{self.name} eating {nameOfFood}"
    def cowinfo(self):
        return f"your cow name is {self.name} & his age is {self.age} & he is colored {self.color} and he is {self.weight} kg."
    def morningTime():
        return "hello user! good morning... " 
    def nightTime():
        return "good night user ! "
    def animalsound():
        return "maaaaaaaaaaaaa... "
# cow_1 = cow(cowName,cowAge,cowColor,cowWeight)

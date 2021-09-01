class Sheep:
    name = ""
    age = int()
    color = ""
    weight = float()
    def __init__(self,name,age,color,weight):
        self.name = name
        if age > 0:
            self.age = age
        else:
            raise ValueError
        self.color = color
        if weight > 0.0:
            self.weight = weight
        else:
            raise ValueError
    def eating(self,nameOfFood):
        return f"{self.name} eating {nameOfFood}"
    def sheepinfo(self):
        return f"your sheep name is {self.name} & his age is {self.age} & he is colored {self.color} and he is {self.weight} kg."
    def morningTime():
        return "hello user! good morning... " 
    def nightTime():
        return "good night user ! "
    def animalsound():
        print("baaaaaaaaaaaaaaaa... ")
# sheep_1 = sheep("sheepName",sheepAge,"sheepColor",sheepWeight)

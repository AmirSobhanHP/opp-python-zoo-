class sheep:
    def __init__(self,name,age,color,weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    def eating(self,nameOfFood):
        return f"{self.name} eating {nameOfFood}"
    def sheepinfo(self):
        return f"your sheep name is {self.name} & his age is {self.age} & he is colored {self.color} and he is {self.weight} kg."
    def morningTime():
        print("hello user! good morning... ") 
    def nightTime():
        print("good night user ! ")
# sheep_1 = sheep("sheepName",sheepAge,"sheepColor",sheepWeight)
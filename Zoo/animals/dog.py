class dog:
    def __init__(self,name,age,color,weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    def eating(self,nameOfFood):
        return f"{self.name} eating {nameOfFood}"
    def doginfo(self):
        return f"your dog name is {self.name} & his age is {self.age} & he is colored {self.color} and he is {self.weight} kg."
    def morningTime():
        return "hello user! good morning... " 
    def nightTime():
        return "good night user ! "
    def animalsound():
        return "hop! hop... "
# dog_1 = dog("dogName",dogAge,"dogColor",dogWeight)
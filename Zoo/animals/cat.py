class cat:
    def __init__(self,name,age,color,weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    def eating(self,nameOfFood):
        return f"{self.name} eating {nameOfFood}"
    def catinfo(self):
        return f"your cat name is {self.name} & his age is {self.age} & he is colored {self.color} and he is {self.weight} kg."
    def morningTime():
        print("hello user! good morning... ") 
    def nightTime():
        print("good night user ! ")
    def animalsound():
        return "miaoooooo... "
# cat_1 = cat("catName",catAge,"catColor",catWeight)
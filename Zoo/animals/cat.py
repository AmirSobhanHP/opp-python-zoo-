class cat:
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
         if age > 0:
            self.weight = age
        else:
            raise ValueError
    def eating(self,nameOfFood):
        return f"{self.name} eating {nameOfFood}"
    def catinfo(self):
        return f"your cat name is {self.name} & his age is {self.age} & he is colored {self.color} and he is {self.weight} kg."
    def morningTime():
        return "hello user! good morning... " 
    def nightTime():
        return "good night user ! "
    def animalsound():
        return "miaoooooo... "
# cat_1 = cat("catName",catAge,"catColor",catWeight)

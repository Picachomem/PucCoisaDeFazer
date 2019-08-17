
##  BEGIN MAIN  ##


class User:

    def __init__(self, userName, memberAmount, foodArray, foodAmount):
        self.userName = userName
        self.memberAmount = memberAmount
        self.foodArray = foodArray
        self.foodAmount = foodAmount

#    frequency

##  TESTES

obj1 = User("Pedro", 4, ["leite", "feijao"], [1, 2])

print(obj1.userName, obj1.memberAmount, obj1.foodArray, obj1.foodAmount)
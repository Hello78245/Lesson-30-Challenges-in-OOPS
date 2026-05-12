import random
class FruitQuiz:
    def __init__(self):
        self.fruits={'apple':'red',
                    'banana':'yellow',
                    'orange':'orange',
                    'lime':'green'}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            print("What is the color of {}?".format(fruit))
            user_answer=input()
            if(user_answer.lower()==color):
                print("Correct Answer")
            else:
                print("wrong answer")
            option=int(input("enter 0, if you wish to play again, press 1:"))
            if(option):
                break
print("welcome to fruit quiz")
fq=FruitQuiz()
fq.quiz()
from random import randint

def level():
    # user is reprompted until one of integers from 1 to 5 is chosen
    while True:
        try:
           lev = int(input("Choose a level from 1 to 5:"))
           if lev in [1,2,3,4,5]:
            break
           else:
              print("Please choose a valid level")
        except ValueError:
            continue

    return lev

def operator():
   # user is reprompted until one of the mathematical operations is chosen
   while True:
    char = input("Choose a mathematical operator(+,-,*,/):")
    if char in ['+','-','/','*']:
        break
    else:
       print("Please choose a valid operator")
       continue
   return char

def generator(lev):
   while True:
        try:
           if lev in [1,2,3,4,5]:
            break
        except ValueError:
            continue
    # if the user chooses 1 , a 1 digit number is generated
   if lev == 1:
      num = randint(1,9)
    # if the user chooses the numbers 2-5 , a 2-5 digit number respectively is generated.
   else:
      num = randint(pow(10,lev-1),pow(10,lev)-1)

   return num

def main():
   
   score = 0
   level_choice = level()
   operator_choice = operator()

   match operator_choice :
    # After appropriate operator is chosen , 10 questions are asked based on the level and the operator chosen
      case '+':
        for _ in range(10):
            x = generator(level_choice)
            y = generator(level_choice)
            try:
               result = x + y
               answer = int(input(f"{x} + {y}:"))
               if answer == result:
                score += 1
               else:
                  print("Wrong answer!")
                  print(f"The correct answer is {result}")
            except ValueError:
               print("Wrong answer!")
               print(f"The correct answer is {result}")
        # After answering the 10 questions the score is displayed
        print(f"Score:{score}")

      case '-':
        for _ in range(10):
            x = generator(level_choice)
            y = generator(level_choice)
            try:
               result = x - y
               answer = int(input(f"{x} - {y}:"))
               if answer == result:
                score += 1
               else:
                  print("Wrong answer!")
                  print(f"The correct answer is {result}")
            except ValueError:
               print("Wrong answer!")
               print(f"The correct answer is {result}")

        print(f"Score:{score}")
      
      case '*':
        for _ in range(10):
            x = generator(level_choice)
            y = generator(level_choice)
            try:
               result = x * y
               answer = int(input(f"{x} * {y}:"))
               if answer == result:
                score += 1
               else:
                  print("Wrong answer!")
                  print(f"The correct answer is {result}")
            except ValueError:
               print("Wrong answer!")
               print(f"The correct answer is {result}")

        print(f"Score:{score}")
    
      case '/':
        # Instruction is given to the user incase division is chosen as an operator
        print("Make sure your answer is rounded to the nearest hundredth place!")
        for _ in range(10):
            x = generator(level_choice)
            y = generator(level_choice)

            try:
               result = round(x / y,2)
               answer = float(input(f"{x} / {y}:"))
               if answer == result:
                score += 1
               else:
                  print("Wrong answer!")
                  print(f"The correct answer is {result}")
            except ValueError:
               print("Wrong answer!")
               print(f"The correct answer is {result}")

        print(f"Score:{score}")
   
if __name__ == "__main__":
    main()



        

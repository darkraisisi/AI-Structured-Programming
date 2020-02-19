import colors
import algorithms as algo
import time

codeLength = 4
maxTries = 8
amountOfColors = len(colors.all_colors)
algo.generateSecret()

def checkInputOptions(_input: str, options: dict, callback) -> str:
    if _input in options:
        options[_input]()
    else:
        print(options, _input)
        print(f"I cant't understand this input: {_input}")
        callback()

def selectGameMode():
   mode = input('Please select the gamemode you want to play.\n1: AI vs AI, see the result of a guessing algorithm.\n2: You vs Ai, You input all the guesses and and asses the responses.\n')
   # \n3: AI vs You, You input a secret and respond to the guesses being made by the AI.
   checkInputOptions(mode,{'1':AIvsAI,'AI vs AI':AIvsAI,'2':personVsAi,'You vs AI':personVsAi},selectGameMode)
def selectGameOptions():
   checkInputOptions(input("Do want to continue with normal game options?\n8 max tries?\n6 different colors?(wip)\nCode length of 4?(wip)\ny/n?"),{'n':gameOptions,'no':gameOptions},selectGameOptions)

def gameOptions():
   checkInputOptions(input("Which option do you want to change?\n1: Max tries?\n2: Amount of different colors?(wip)\n3: Code length(wip)?\n"),{'1':setOptionAmount},gameOptions)

def setOptionAmount():
   print('test')

def AIvsAI():
   wins = 0
   loses = 0
   amountOfGames = input("How many games do you want to play?\n")
   game = 0
   totalTries = 0
   startTime = time.time()
   print("Start Time: {startTime}")
   while game < int(amountOfGames):
      # print(f'game:{game}')
      hasWon = False
      algo.generateSecret()
      algo.repopulateAllCombinations()

      for turn in range(0,maxTries):
         totalTries += 1

         # evaluation = algo.simpleAlgorithm(turn,colors.SECRET)
         evaluation = algo.consistentWorstCaseAlgorithm(turn,colors.SECRET)

         if(evaluation['black'] == 4):
            hasWon = True
            break

      game += 1

      if(hasWon):
         wins += 1
      else:
         loses += 1
      
   elapsedTime = time.time() - startTime
   print(f'To complete {game} games it took:{elapsedTime}s')
   print(f'Player 1 Won:{wins} times and Lost:{loses} times')
   print(f'TotalTries:{totalTries}/ Amount of games played:{game}')
   print(f'Amount of guesses ratio:{totalTries / game}')

def personVsAi():
   wins = 0
   loses = 0
   amountOfGames = input("Howmany games do you want to play?\n")
   game = 0
   print(f'Secret: {colors.SECRET}')
   while game < int(amountOfGames):
      print(f'New Round, round {game}')
      hasWon = False
      for turn in range(0,maxTries):
         print(f'Turn:{turn+1}')
         guesse = inputToGuesse()
         evaluation = algo.evaluateColors(guesse,colors.SECRET)
         print(evaluation)
         if(evaluation['black'] == 4):
            print('-----\nYou won\n-----')
            hasWon = True
            break
      game += 1

      if(hasWon):
         wins += 1
      else:
         loses += 1
      

   print(f'You Won:{wins} times and Lost:{loses} times')

def inputToGuesse()->list:
   newGuesse = []
   print(f'\nPlease input {codeLength} colors:')
   print("1: Red, 2: Yellow, 3: Blue, 4: Green, 5: Orange, 6: Purple")
   while len(newGuesse) < 4:
      color = inputToColor(input('Please input one of these colors.\n'))
      if color:
         newGuesse.append(color)
   return newGuesse

def inputToColor(i)->str:
   try:
      i = int(i)
      if(i <= amountOfColors):
         print('1',colors.all_colors[i-1])
         return colors.all_colors[i-1]
      else:
         print('number was to high')
   except ValueError:
      for color in colors.all_colors:
         if lower(i[0]) == lower(color[0]):
            print('1',color)
            return color

if __name__ == "__main__":
   # selectGameOptions()
   selectGameMode()
   # inputToGuesse()
   # pins = algo.evaluateColors(['Green','Green','Red','Yellow'],colors.SECRET)
   # print(pins)
   # print(len(algo.allPossibleCombinations))
   # print('done')
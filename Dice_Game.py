# improved Dice game

import os
import random
import time
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Dice Art
diceArt = {
     1 :("┌───────┐",
         "│       │",
         "│   ●   │",
         "│       │",
         "└───────┘"),
     2 :("┌───────┐",
         "│ ●     │",
         "│       │",
         "│     ● │",
         "└───────┘"),
     3 :("┌───────┐",
         "│     ● │",
         "│   ●   │",
         "│ ●     │",
         "└───────┘"),
     4 :("┌───────┐",
         "│ ●   ● │",
         "│       │",
         "│ ●   ● │",
         "└───────┘"),
     5 :("┌───────┐",
         "│ ●   ● │",
         "│   ●   │",
         "│ ●   ● │",
         "└───────┘"),
     6 :("┌───────┐",
         "│ ●   ● │",
         "│ ●   ● │",
         "│ ●   ● │",
         "└───────┘"),
     0 :("┌───────┐",
         "│       │",
         "│       │",
         "│       │",
         "└───────┘")}

# functions
def info():
     clear()
     print(" ┌───────────────────────────────┐")
     print(" │ How to play:                  │")
     print(" │  - Choose a number where you  │")
     print(" │    want then place your bet   │")
     print(" │  - You win if your chosen #   │")
     print(" │    appears on any of the of   │")
     print(" │    the rolled dice            │")
     print(" │  - If your chosen number      │")
     print(" │    appears 2x, you winnings   │")
     print(" │    will be 2x of you bet. If  │")
     print(" │    3x, it will be 3x.         │")
     print(" │                               │")
     print(" │ Command:                      │")
     print(" │ [q] quit      [s] settings    │")
     print(" │ [i] show this info.           │")
     print(" │                               │")
     print(" └───────────────────────────────┘")
     print()
     print()
     print("  Press [enter] to return. . .    ")
     input()

def roll():
     rolled = [random.randint(1,6) for _ in range(3)]
     return rolled

def payout(rolled, b1, b2, b3, b4, b5, b6):
     returnCredit = 0
     win = 0
     lose = 0
     if b1 != 0 and 1 in rolled: win += b1 * rolled.count(1); returnCredit += b1
     if b2 != 0 and 2 in rolled: win += b2 * rolled.count(2); returnCredit += b2
     if b3 != 0 and 3 in rolled: win += b3 * rolled.count(3); returnCredit += b3
     if b4 != 0 and 4 in rolled: win += b4 * rolled.count(4); returnCredit += b4
     if b5 != 0 and 5 in rolled: win += b5 * rolled.count(5); returnCredit += b5
     if b6 != 0 and 6 in rolled: win += b6 * rolled.count(6); returnCredit += b6
     if b1 != 0 and 1 not in rolled: lose += b1
     if b2 != 0 and 2 not in rolled: lose += b2
     if b3 != 0 and 3 not in rolled: lose += b3
     if b4 != 0 and 4 not in rolled: lose += b4
     if b5 != 0 and 5 not in rolled: lose += b5
     if b6 != 0 and 6 not in rolled: lose += b6
     return win, lose, returnCredit

def checkInt(n):
     try:
          int(n)
          return True
     except ValueError:
          return False

def main():
     statsNum = 50
     statsNumMsg = f"last {statsNum} games"
     rolled = [0,0,0]
     b1, b2, b3, b4, b5, b6 = 0, 0, 0, 0, 0, 0
     stats= []
     s1, s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0, 0
     winLos = []
     wl1, wl2, wl3, wl4, wl5, wl6, wl7, wl8 = "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "
     betWinLos = []
     bwl1, bwl2, bwl3, bwl4, bwl5, bwl6, bwl7, bwl8 = 0, 0, 0, 0, 0, 0, 0, 0
     results= []
     h1, h2, h3, h4, h5, h6, h7, h8 = "[ ,  ,  ]", "[ ,  ,  ]", "[ ,  ,  ]", "[ ,  ,  ]", "[ ,  ,  ]", "[ ,  ,  ]", "[ ,  ,  ]", "[ ,  ,  ]"
     currency = "P"
     credit = 1000
     bet = 0
     min = 25
     max = min*200
     msg = ""
     rollingAnimation = False
     while True:
          clear()
          while rollingAnimation:
               for _ in range(5):
                    animationMsg = "Rolling. . ."
                    animationRolled = roll()
                    clear()
                    print(" ┌───────────────────────────────┬───────────────────────────────┐")
                    for line in range(5):
                              print(" │", end="")
                              for die in animationRolled:
                                   print(f" {diceArt.get(die)[line]}", end="")
                              print(" │", end="")
                              print(f"    Dice result probability    │" if line == 0 else "", end="")
                              print(f"{statsNumMsg:^31}│" if line == 1 else "", end="")
                              print(f" [1]  --.-- %    [4]  --.-- %  │" if line == 2 else "", end="")
                              print(f" [2]  --.-- %    [5]  --.-- %  │" if line == 3 else "", end="")
                              print(f" [3]  --.-- %    [6]  --.-- %  │" if line == 4 else "", end="")  
                              print()
                    print(" ├───────────────────────────────┼───────────────────────────────┤")
                    print(" │        PLACE YOUR BETS        │ #    result:  stats     bet   │")
                    print(f" │ [1]  {currency} {b1:6}   [4]  {currency} {b4:6} │ 1 - [ ,  ,  ]  ---   {currency} ------ │")
                    print(f" │ [2]  {currency} {b2:6}   [5]  {currency} {b5:6} │ 2 - {h2}  {wl2}   {currency} {bwl2:6} │")
                    print(f" │ [3]  {currency} {b3:6}   [6]  {currency} {b6:6} │ 3 - {h3}  {wl3}   {currency} {bwl3:6} │")
                    print(f" ├───────────────┬───────────────┤ 4 - {h4}  {wl4}   {currency} {bwl4:6} │")
                    print(f" │ bal: {currency} {credit:6} │ min: {currency} {min:6} │ 5 - {h5}  {wl5}   {currency} {bwl5:6} │")
                    print(f" │ bet: {currency} {bet:6} │ max: {currency} {max:6} │ 6 - {h6}  {wl6}   {currency} {bwl6:6} │")
                    print(f" ├───────────────┴───────────────┤ 7 - {h7}  {wl7}   {currency} {bwl7:6} │")
                    print(f" │ > {animationMsg:^25} < │ 8 - {h8}  {wl8}   {currency} {bwl8:6} │")
                    print(" └───────────────────────────────┴───────────────────────────────┘")
                    print("                                                      [i] - help  ")
                    time.sleep(0.3)
               rollingAnimation = False
          clear()
          print(" ┌───────────────────────────────┬───────────────────────────────┐")
          for line in range(5):
                    print(" │", end="")
                    for die in rolled:
                         print(f" {diceArt.get(die)[line]}", end="")
                    print(" │", end="")
                    print(f"    Dice result probability    │" if line == 0 else "", end="")
                    print(f"{statsNumMsg:^31}│" if line == 1 else "", end="")
                    print(f" [1] {s1:6.2f} %    [4] {s4:6.2f} %  │" if line == 2 else "", end="")
                    print(f" [2] {s2:6.2f} %    [5] {s5:6.2f} %  │" if line == 3 else "", end="")
                    print(f" [3] {s3:6.2f} %    [6] {s6:6.2f} %  │" if line == 4 else "", end="")  
                    print()
          print(" ├───────────────────────────────┼───────────────────────────────┤")
          print(" │        PLACE YOUR BETS        │ #    result:  stats     bet   │")
          print(f" │ [1]  {currency} {b1:6}   [4]  {currency} {b4:6} │ 1 - {h1}  {wl1}   {currency} {bwl1:6} │")
          print(f" │ [2]  {currency} {b2:6}   [5]  {currency} {b5:6} │ 2 - {h2}  {wl2}   {currency} {bwl2:6} │")
          print(f" │ [3]  {currency} {b3:6}   [6]  {currency} {b6:6} │ 3 - {h3}  {wl3}   {currency} {bwl3:6} │")
          print(f" ├───────────────┬───────────────┤ 4 - {h4}  {wl4}   {currency} {bwl4:6} │")
          print(f" │ bal: {currency} {credit:6} │ min: {currency} {min:6} │ 5 - {h5}  {wl5}   {currency} {bwl5:6} │")
          print(f" │ bet: {currency} {bet:6} │ max: {currency} {max:6} │ 6 - {h6}  {wl6}   {currency} {bwl6:6} │")
          print(f" ├───────────────┴───────────────┤ 7 - {h7}  {wl7}   {currency} {bwl7:6} │")
          print(f" │ > {msg:^25} < │ 8 - {h8}  {wl8}   {currency} {bwl8:6} │")
          print(" └───────────────────────────────┴───────────────────────────────┘")
          print("                                                      [i] - help  ")
          print("                                                  [enter] - roll  ")
          i = input("  >: ").lower()
          if i == "s":
               setting_isRunning = True
               while setting_isRunning:
                    clear()
                    print(" ┌───────────────────────────────┐")
                    print(" │ Settings:                     │")
                    print(" │                               │")
                    print(" │  [1] Change currency          │")
                    print(" │  [2] Change min and max bet   │")
                    print(" │  [3] Probability # of game    │")
                    print(" │  [4] Add credit               │")
                    print(" │  [5] return to game           │")
                    print(" │                               │")
                    print(" │                               │")
                    print(f" │           {currency}  : currency       │")
                    print(f" │      {min:6}  : min            │")
                    print(f" │      {max:6}  : max (min*200)  │")
                    print(f" │        {statsNum:4}  : # of game      │")
                    print(f" │      {credit:6}  : add credit     │")
                    print(" │                               │")
                    print(" └───────────────────────────────┘")
                    print()
                    s = input("  >: ").lower()
                    if s == "1":
                         xCur = input(f"  Enter single currency symbol: ")
                         if len(xCur) != 1:
                              print()
                              print("  INVALID:")
                              print("  Enter single Characrter only")
                              print()
                              print("  [enter] to continue . . . ")
                              input()
                              continue
                         currency = xCur
                         continue
                    if s == "2":
                         xMin = input(f"  Enter Min bet(1-4999): {currency} ")
                         if checkInt(xMin):
                              xMin = int(xMin)
                              if xMin > 0 and xMin <= 4999:
                                   min = xMin; max = xMin*200
                                   continue
                         print()
                         print("  INVALID:")
                         print("  Enter valid min bet")
                         print()
                         print("  [enter] to continue . . . ")
                         input()
                         continue
                    if s == "3":
                         xSN = input("  Enter # of Game for Stats(1-999): ")
                         if checkInt(xSN):
                              xSN = int(xSN)
                              if xSN > 0 and xSN <= 999:
                                   statsNum = xSN
                                   statsNumMsg = f"last {statsNum} games"
                                   continue
                         else:
                              print()
                              print("  INVALID:")
                              print("  Enter # of Game for Stats")
                              print()
                              print("  [enter] to continue . . . ")
                              input()
                              continue
                    if s == "4":
                         if credit >11:
                              print()
                              print("  INVALID:")
                              print("  Add only when you credit is")
                              print(f"  below {currency} 10")
                              print()
                              print("  [enter] to continue . . . ")
                              input()
                              continue
                         xCre = input("  Enter credit add(1-20000):")
                         if checkInt(xCre):
                              xCre = int(xCre)
                              if xCre > 0 and xCre <= 20000:
                                   credit += xCre
                                   continue
                         else:
                              print()
                              print("  INVALID:")
                              print("  Enter valid add credit amount")
                              print()
                              print("  [enter] to continue . . . ")
                              input()
                              continue
                    if s == "5":
                         setting_isRunning = False
               continue
          if i == "i":
               info()
               msg = ""
               continue
          if i == "q":
               clear()
               exit()
          if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6":
               amount = input(f" Enter your bet for #{i}: {currency} ")
               if not checkInt(amount):
                    msg = "INVALID: bet value"
                    continue
               amount = int(amount)
               if amount == 0:
                    if i == "1": credit += b1; bet -= b1; b1 = 0
                    if i == "2": credit += b2; bet -= b2; b2 = 0
                    if i == "3": credit += b3; bet -= b3; b3 = 0
                    if i == "4": credit += b4; bet -= b4; b4 = 0
                    if i == "5": credit += b5; bet -= b5; b5 = 0
                    if i == "6": credit += b6; bet -= b6; b6 = 0
               elif amount > max or amount < min:
                    msg = "INVALID: bet out of range"
                    continue
               elif amount > credit:
                    msg = "INVALID: insufficient bal"
                    continue
               elif amount <= max and amount >= min:
                    credit -= amount
                    bet += amount
                    if i == "1": credit += b1; bet -= b1; b1 = amount; msg = f"{currency}{amount} was placed at #1"
                    if i == "2": credit += b2; bet -= b2; b2 = amount; msg = f"{currency}{amount} was placed at #2"
                    if i == "3": credit += b3; bet -= b3; b3 = amount; msg = f"{currency}{amount} was placed at #3"
                    if i == "4": credit += b4; bet -= b4; b4 = amount; msg = f"{currency}{amount} was placed at #4"
                    if i == "5": credit += b5; bet -= b5; b5 = amount; msg = f"{currency}{amount} was placed at #5"
                    if i == "6": credit += b6; bet -= b6; b6 = amount; msg = f"{currency}{amount} was placed at #6"
                    continue
          if i == "":
               if bet > 0:
                    rollingAnimation = True
                    rolled = roll()
                    winnings = payout(rolled, b1, b2, b3, b4, b5, b6)[0]
                    lose = payout(rolled, b1, b2, b3, b4, b5, b6)[1]
                    returned = payout(rolled, b1, b2, b3, b4, b5, b6)[2]
                    credit += winnings + returned
                    b1, b2, b3, b4, b5, b6 = 0, 0, 0, 0, 0, 0
                    bet = 0
                    if winnings > 0: msg = f"You won {currency}{winnings}!"
                    if winnings == 0: msg = ""
                    results.append(rolled)
                    if len(results) >= 9: results.pop(0)
                    for x in rolled:
                         stats.append(x)
                         while len(stats) > statsNum:
                              stats.pop(0)
                    if winnings > lose: winLos.append("WIN"); betWinLos.append(winnings - lose); msg = f"You won {currency}{winnings}!"
                    if winnings < lose: winLos.append("LOS"); betWinLos.append(winnings - lose); msg = f"You Lose {currency}{lose}!"
                    if len(winLos) >= 9 or len(betWinLos) >= 9: winLos.pop(0); betWinLos.pop(0)
                    s1 = (stats.count(1) / len(stats)) * 100
                    s2 = (stats.count(2) / len(stats)) * 100
                    s3 = (stats.count(3) / len(stats)) * 100
                    s4 = (stats.count(4) / len(stats)) * 100
                    s5 = (stats.count(5) / len(stats)) * 100
                    s6 = (stats.count(6) / len(stats)) * 100
                    if len(results) >= 1: h1 = results[-1]
                    if len(results) >= 2: h2 = results[-2]
                    if len(results) >= 3: h3 = results[-3]
                    if len(results) >= 4: h4 = results[-4]
                    if len(results) >= 5: h5 = results[-5]
                    if len(results) >= 6: h6 = results[-6]
                    if len(results) >= 7: h7 = results[-7]
                    if len(results) == 8: h8 = results[-8]
                    if len(winLos) >= 1: wl1 = winLos[-1]
                    if len(winLos) >= 2: wl2 = winLos[-2]
                    if len(winLos) >= 3: wl3 = winLos[-3]
                    if len(winLos) >= 4: wl4 = winLos[-4]
                    if len(winLos) >= 5: wl5 = winLos[-5]
                    if len(winLos) >= 6: wl6 = winLos[-6]
                    if len(winLos) >= 7: wl7 = winLos[-7]
                    if len(winLos) == 8: wl8 = winLos[-8]
                    if len(betWinLos) >= 1: bwl1 = betWinLos[-1]
                    if len(betWinLos) >= 2: bwl2 = betWinLos[-2]
                    if len(betWinLos) >= 3: bwl3 = betWinLos[-3]
                    if len(betWinLos) >= 4: bwl4 = betWinLos[-4]
                    if len(betWinLos) >= 5: bwl5 = betWinLos[-5]
                    if len(betWinLos) >= 6: bwl6 = betWinLos[-6]
                    if len(betWinLos) >= 7: bwl7 = betWinLos[-7]
                    if len(betWinLos) == 8: bwl8 = betWinLos[-8]
                    continue
               else:
                    msg = "INVALID: no bet yet"
          if i == "x":
               rolled = roll()
               continue
          continue
if __name__ == "__main__":
     main()
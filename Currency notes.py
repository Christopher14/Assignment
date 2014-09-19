#Christopher pullen
#19.09.2014
#currency notes
#progamm will allow you to enter a number and will tell you how mant 20, 10, 5, 2, 1 notes/coins you will need.

money = int(input("Please enter the amount of money you would like to be placed into coins/notes"))

twenty_notes = money // 20
twenty_remainder = money % 20
ten_notes = twenty_remainder // 10
ten_remainder = twenty_remainder % 10
five_notes = ten_remainder // 5
five_remainder = ten_remainder % 5
two_coins = five_remainder // 2
two_remainder = five_remainder % 2
one_coins = two_remainder // 1

print (" Your total notes and coins are {0} £20 notes, {1} £10 notes, {2} £5 notes, {3} £2 coins and {4} £1 coins" .format (twenty_notes, ten_notes, five_notes, two_coins, one_coins))

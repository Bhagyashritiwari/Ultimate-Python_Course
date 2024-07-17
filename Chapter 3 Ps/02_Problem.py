# Write a program to fill in a letter template given below with name and date.

letter = ''' Dear Name,
You are selected!
<|Date|>
'''      
print(letter.replace("Name", "Bani").replace("<|Date|>", "30 July 2024")) ## use replace method


#program to display the hendred's tens and units in a number
integer=int(input("Pick a number from 100 - 999: "))
hundreds = integer//100 #whole number division
integer_two = integer%100 # givesw the remainder
tens = integer_two//10 #divides the remainder by ten
units = integer_two%10 #gives the remainder of the remainder
print(hundreds, "hundreds", tens, "tens", units, "units")





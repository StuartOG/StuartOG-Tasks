#program to display the hendred's tens and units in a number
integer=int(input("Pick a number from 100 - 999: "))
hundreds = integer//100
integer_two = integer%100
tens = integer_two//10
units = integer_two%10
print(hundreds, "hundreds", tens, "tens", units, "units")





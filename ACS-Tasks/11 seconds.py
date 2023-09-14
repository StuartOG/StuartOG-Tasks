input = (input("Enter a time")) #input a time for the user
times = input.split(":") #separates the hours minutes and seconds

if len(times) != 3:
    print("Please use the x:x:x format instead") # makes the user use the x:x:x format to input the time
else:
    hours = int(times[0]) * 60 * 60 # converts hours into seconds
    minutes = int(times[1]) * 60 # converts minutes into seconds
    seconds = int(times[2])

    total = hours + seconds + minutes # adds all the numbers together
    print(total) # prints the total number of seconds

input = (input("Enter a time"))
times = input.split(":")

if len(times) != 3:
    print("Please use the x:x:x format instead")
else:
    hours = int(times[0]) * 60 * 60
    minutes = int(times[1]) * 60
    seconds = int(times[2])

    total = hours + seconds + minutes
    print(total)

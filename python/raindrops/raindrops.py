def convert(number):

    # returns raindrop "sounds" of either "Pling", "Plang", and/or "Plong"
    # if the number is divisible by 3, 5, and 7, respectively.
    # returns the number if the number is not divisible by either 3, 5, or 7

    divisor = {3: "Pling", 5: "Plang", 7: "Plong"}
    times = 0
    raindrop_sound = ""

    for digit in divisor.keys():
        if number % digit == 0:
            raindrop_sound = raindrop_sound + divisor[digit]
            times += 1

    return f"{raindrop_sound}" if times != 0 else f"{number}"

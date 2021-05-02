sounds = {3: "Pling", 5: "Plang", 7: "Plong"}


def convert(number):

    # returns raindrop "sounds" of either "Pling", "Plang", and/or "Plong"
    # if the {argument} is a number divisible by 3, 5, and 7, respectively.
    # returns the {argument} if it is a number but is not divisible by either 3, 5, or 7
    # returns "The passed argument was not a number" if the {argument} is a string type

    if type(number) != str:
        drop_sound = [value for key, value in sounds.items() if number % key == 0]
        wife = "".join(drop_sound) if drop_sound else str(number)
        return wife
    else:
        return "The passed argument was not a number."

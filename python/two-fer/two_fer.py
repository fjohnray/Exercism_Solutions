
# def two_fer(name=None):
#     if name is None:
#         return "One for you, one for me."
#     else:
#         return "One for " + name + ", one for me."
# ^ first solution but finds unpythonic, I guess?

def two_fer(name="you"):
    # returns "One for {argument}, one for me."
    # returns "One for you, one for me." if no {argument} was passed
    return f"One for {name}, one for me."

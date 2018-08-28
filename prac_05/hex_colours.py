COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "beige": "#f5f5dc",
           "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2", "brown": "#a52a2a", "burlywood": "#deb887",
           "CadetBlue": "#5f9ea0", "chartreuse1": "#7fff00"}

user_input = input("Enter a colour: ")
while user_input != "":
    print("The code for \"{}\" is {}".format(user_input,
                                             COLOURS.get(user_input)))
    user_input = input("Enter a colour: ")
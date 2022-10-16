def band_name():
    '''
    This function will take the city of where the user grew up and
    name of their pet then combine them to output a band name
    '''

    print("Hey there! Let\'s make you a band name.")
    
    hometown = input("What city or hometown you grew up in? \n")
    pet_name = input("What\'s the name of your pet? \n ")

    band = hometown + ' ' + pet_name

    print(f"Your band name is {name_of_band}")

band_name()

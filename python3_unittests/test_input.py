def test():
    choice = input("Would you like to see your current password and username? \n(Type see input or new input): ")
    if choice == "see input":
        namefile1 = open("namefile.txt", "r")
        a = namefile1.read()
        namefile1.close()
        print(a)
    elif choice == "new input":
        a = input("What is your password? ")
        b = input("\nwhat is your username? ")
        namefile = open("namefile.txt", "w")
        namefile.write("\n" + "Your Username is: " + b + "\n" + "\nYour Password is: " + a)
        namefile.close()

        def thinger():
            relo = input("\nWould you like to see whats inside your text file? Y/N ")
            if relo == "Y":
                namefile1 = open("namefile.txt", "r")
                a = namefile1.read()
                namefile1.close()
                print(a)
            elif relo == "N":
                print("Okay goodbye")
            elif relo != "N" or relo != "Y":
                print("\n")
                print(relo + " " + "is a invalid input")
                thinger()
        thinger()
    elif choice != "see input" or choice != "new input":
        print("\nThat is a invalid input <{}>".format(choice))
        test()


test()

"""Short and sweet demo program."""

import random

__author__ = "Jesse Wei <jessew13@email.unc.edu>"

# Please don't modify this list :)
# ok i won't
SECRET: list[str] = ['  ', '█', '█', '█', '█', '█', '█', '╗', ' ', '█', '█', '╗', '█', '█', '█', '█', '█', '█', '█', '█', '╗', ' ', '█', '█', '╗', ' ', '█', '█', '╗', ' ', '█', '█', '█', '█', '█', '█', '╗', ' ', '\n', ' ', '█', '█', '╔', '═', '═', '═', '═', '╝', ' ', '█', '█', '║', '╚', '═', '═', '█', '█', '╔', '═', '═', '╝', '█', '█', '█', '║', '█', '█', '█', '║', '█', '█', '╔', '═', '█', '█', '█', '█', '╗', '\n', ' ', '█', '█', '║', ' ', ' ', '█', '█', '█', '╗', '█', '█', '║', ' ', ' ', ' ', '█', '█', '║', ' ', ' ', ' ', '╚', '█', '█', '║', '╚', '█', '█', '║', '█', '█', '║', '█', '█', '╔', '█', '█', '║', '\n', ' ', '█', '█', '║', ' ', ' ', ' ', '█', '█', '║', '█', '█', '║', ' ', ' ', ' ', '█', '█', '║', ' ', ' ', ' ', ' ', '█', '█', '║', ' ', '█', '█', '║', '█', '█', '█', '█', '╔', '╝', '█', '█', '║', '\n', ' ', '╚', '█', '█', '█', '█', '█', '█', '╔', '╝', '█', '█', '║', ' ', ' ', ' ', '█', '█', '║', ' ', ' ', ' ', ' ', '█', '█', '║', ' ', '█', '█', '║', '╚', '█', '█', '█', '█', '█', '█', '╔', '╝', '\n', '  ', '╚', '═', '═', '═', '═', '═', '╝', ' ', '╚', '═', '╝', ' ', ' ', ' ', '╚', '═', '╝', ' ', ' ', ' ', ' ', '╚', '═', '╝', ' ', '╚', '═', '╝', ' ', '╚', '═', '═', '═', '═', '═', '╝', ' ', '\n']

def main() -> None:
    print("Hello git110ers!")  
    # HELLO THIS IS A CHANGE
    file = open("demo.txt", "w")
    for char in SECRET:
        file.write(char)
    file.close()
    print("After running this file, open up demo.txt in File Explorer/Finder for a nice surprise :)")
    print("You can also accomplish this by typing cat demo.txt (macOS and Linux) or more demo.txt (Windows)")
    
    # Add whatever else you want under this line!
    print("HELP ME")
    # A simple print statement, something interesting, or anything else.
    # If you want your pull request to be accepted, don't put anything you wouldn't want others to see.

    # what if i just add a comment
    
    # ok fine I'll add a print statement in a loop
    num_times: int = int(input("Type a number, any number! "))
    for i in range(num_times):
        print("Hello world " + str(i))


# if __name__ == "__main__" is lame
# actually functions are lame I prefer to keep all my code at the global level

if __name__ == "__main__":
    main()

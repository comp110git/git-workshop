"""Short and sweet demo program!"""

__author__ = "githubtester110 <githubtester110@gmail.com>"  # Fill in your name here - always good practice to have an __author__ variable.

# Please don't modify this list :)
# ok i won't
SECRET: list[str] = ['  ', '█', '█', '█', '█', '█', '█', '╗', ' ', '█', '█', '╗', '█', '█', '█', '█', '█', '█', '█', '█', '╗', ' ', '█', '█', '╗', ' ', '█', '█', '╗', ' ', '█', '█', '█', '█', '█', '█', '╗', ' ', '\n', ' ', '█', '█', '╔', '═', '═', '═', '═', '╝', ' ', '█', '█', '║', '╚', '═', '═', '█', '█', '╔', '═', '═', '╝', '█', '█', '█', '║', '█', '█', '█', '║', '█', '█', '╔', '═', '█', '█', '█', '█', '╗', '\n', ' ', '█', '█', '║', ' ', ' ', '█', '█', '█', '╗', '█', '█', '║', ' ', ' ', ' ', '█', '█', '║', ' ', ' ', ' ', '╚', '█', '█', '║', '╚', '█', '█', '║', '█', '█', '║', '█', '█', '╔', '█', '█', '║', '\n', ' ', '█', '█', '║', ' ', ' ', ' ', '█', '█', '║', '█', '█', '║', ' ', ' ', ' ', '█', '█', '║', ' ', ' ', ' ', ' ', '█', '█', '║', ' ', '█', '█', '║', '█', '█', '█', '█', '╔', '╝', '█', '█', '║', '\n', ' ', '╚', '█', '█', '█', '█', '█', '█', '╔', '╝', '█', '█', '║', ' ', ' ', ' ', '█', '█', '║', ' ', ' ', ' ', ' ', '█', '█', '║', ' ', '█', '█', '║', '╚', '█', '█', '█', '█', '█', '█', '╔', '╝', '\n', '  ', '╚', '═', '═', '═', '═', '═', '╝', ' ', '╚', '═', '╝', ' ', ' ', ' ', '╚', '═', '╝', ' ', ' ', ' ', ' ', '╚', '═', '╝', ' ', '╚', '═', '╝', ' ', '╚', '═', '═', '═', '═', '═', '╝', ' ', '\n']

def main() -> None:
    print("Hello 110ers!")  
    file = open("demo.txt", "w")
    for char in SECRET:
        file.write(char)
    file.close()
    print("After running this file, open up demo.txt in File Explorer/Finder for a nice surprise :)")
    print("You can also accomplish this by typing cat demo.txt")
    
    # Add whatever else you want under this line!
    # A simple print statement, something interesting, or anything else.
    # If you want your pull request to be accepted, don't put anything you wouldn't want others to see.

    # how about i just add a comment, gg


if __name__ == "__main__":
    main()

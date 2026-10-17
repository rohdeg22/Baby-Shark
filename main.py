"""----------------------------------------------------------------
Name:       Grace Rohde
Assignment: Lab - Baby Shark
Course:     CS 1430, Section X, Fall 2026
Purpose:    This program is designed to be practice for Python
            functions

Input: None

Output: The sound Baby Shark, with three verses:
        Baby Shark,
        doo-doo-doo-do-do-do-do *3
        Baby Shark!
        Mommy Shark,
        doo-doo-doo-do-do-do-do *3
        Mommy Shark!
        Daddy Shark,
        doo-doo-doo-do-do-do-do *3
        Daddy Shark!
----------------------------------------------------------------"""

##############
# CONSTANTS
##############
REPEAT = 3
#def dodo():
    #print("doo-doo-doo-do-do-do-do")
def shark_verse(shark):
    for i in range(REPEAT):
        print(shark, "Shark,")
        print("doo-doo-doo-do-do-do-do")
    print(shark, "Shark" + "!")

def main ():
    shark_verse("Baby")
    shark_verse("Mommy")
    shark_verse("Daddy")

#def main():
    #print("Baby Shark,")
    #p#rint("doo-doo-doo-do-do-do-do")
    #pr#int("Baby Shark,")
    #print("doo-doo-doo-do-do-do-do")
    #print("Baby Shark,")
    #p#rint("doo-doo-doo-do-do-do-do")
    #pr#int("Baby Shark!")
    #pri#nt("Mommy Shark,")
    #prin#t("doo-doo-doo-do-do-do-do")
    #print###Mommy Shark,")
   # print("doo-doo-doo-do-do-do-do")
    #print("Mommy Shark!")
    #print("Daddy Shark,")
    #print("doo-doo-doo-do-do-do-do")
    #print("Daddy Shark,")
    #print("doo-doo-doo-do-do-do-do")
    #print("Daddy Shark,")
    #print("doo-doo-doo-do-do-do-do")
    #print("Daddy Shark!")


if __name__ == "__main__":
    main()

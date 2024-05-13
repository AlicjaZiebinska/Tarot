init python:
    import random
    
#wybranakarta = {1: renpy.image, 2: karta do wyboru2, 3: karta do wyboru3, 4: karta do wyboru4}
    

    

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ft = Character("Fortune teller")


# The game starts here.

label start:

    scene pokoj
    show wrozbitka at right


    ft "Hi dear! What can I get for you today?"

    ft "Do You want to see what tommorow brings?"

    label choice:
        menu:
            "Yes":
                jump cards
            "No":
                jump shame

    label cards:
        $ pierwsza = 0
        hide wrozbitka with dissolve
        show kartydowyboru at center with dissolve
        "Choose one card."
        menu:
            "first":
                jump firstcard
            "second":
                jump firstcard
            "third":
                jump firstcard

                label firstcard:

                    $ wybranakarta = renpy.random.randint(0,13)
                    $ pierwsza = wybranakarta
                    show expression ("karty/karty%d.png" % wybranakarta) at top
                    
                    ft "Oh well that is interesting. Let's choose next card."

        hide wybranakarta with dissolve
        show kartydowyboru at center with dissolve
#

        menu:
            "first":
                jump secondcard
            "second":
                jump secondcard
            "third":
                jump secondcard

                label secondcard:

                    $ wybranakarta = renpy.random.randint(0,13)
                    $ druga = wybranakarta
                    while druga == pierwsza:
                        $ wybranakarta = renpy.random.randint(0,13)

                    show expression ("karty/karty%d.png" % wybranakarta) at top
                    
                    ft "Hmm it is getting even better!"

        hide wybranakarta with dissolve
        show kartydowyboru at center with dissolve

#

        menu:
            "first":
                jump thirdcard
            "second":
                jump thirdcard
            "third":
                jump thirdcard

                label thirdcard:

                    $ wybranakarta = renpy.random.randint(0,13)
                    $ trzecia = wybranakarta
                    while trzecia == pierwsza or trzecia == druga:
                        $ wybranakarta = renpy.random.randint(0,13)

                    show expression ("karty/karty%d.png" % wybranakarta) at top
                    
                    ft "Okey! That is the third card. Now let's read what they mean."

        hide wybranakarta with dissolve
        show kartydowyboru at center with dissolve


     
    label shame:
        "Ohhh, such a shame. Okay, find out it by yourself."
        jump end  
    label end:
        "It was nice to see you sweetie, good luck!"







    jump choice



    # This ends the game.

    return

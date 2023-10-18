import random
import time


class InvalidInput(Exception):
    pass


def user_hit(monster):
    if monster == "goblin":
        return random.randint(5, 20)
    elif monster == "orc":
        return random.randint(12, 40)
    else:
        return random.randint(25, 100)


def monster_hit(monster):
    if monster == "goblin":
        return random.randint(1, 9)
    elif monster == "orc":
        return random.randint(5, 19)
    else:
        return random.randint(10, 42)


user_health = 100
monster_dict = {"goblin": 30,
                "orc": 80,
                "dragon": 200}
monsters = ["goblin", "orc", "dragon"]
moves = {"h": "Hit", "d": "Doge"}
fight = ["h", "d"]
defeated = {}

print("You are an adventurer, who is lost in woods full of monsters.\n"
      "There are total 3 types of monsters in this forest:"
      "Dragon, Orc and Goblin.\n"
      "Defeat all of them to complete this game. \n\n\n")

time.sleep(1.4)

while True:
    try:
        mons_typ = random.choice(monsters)
        mons_health = monster_dict[mons_typ]
        print("You hear some noises from not so far and decided to check it out.\n"
              "You saw a monster there......\n")
        print(f"Its a {mons_typ} with {mons_health}hp")
        time.sleep(0.5)
        choice = input("Enter your choice fight the monster or quit (f/q):")
        if choice.lower() == "f":
            print()
            print(f"You chose to fight the {mons_typ}")

            while True:
                user_fight_choice = input("hit or dodge or quit or any other key to exit this fight(h/d/q):")
                print()
                mons_choice = random.choice(fight)

                if user_fight_choice in fight:
                    if user_fight_choice.lower() == mons_choice == "h":
                        usr_damage = user_hit(mons_typ)
                        mons_health -= usr_damage
                        mons_damage = monster_hit(mons_typ)

                        if mons_health <= 0:
                            if mons_typ in defeated:
                                defeated[mons_typ] += 1
                            else:
                                defeated[mons_typ] = 1
                            print(defeated)
                            monsters.pop(monsters.index(mons_typ))
                            print(f"You slayed the {mons_typ}.\n"
                                  f"Your health has been restored.")
                            user_health = 100
                            if monsters:
                                play_again = input("Do you want to continue fighting monsters? (y/n): ").lower()
                                if play_again == 'y':
                                    break
                                elif play_again == "n":
                                    if defeated:
                                        print("You defeated:")
                                        for mons in defeated:
                                            print(f"{defeated[mons]} {mons}")
                                    exit()
                                else:
                                    raise InvalidInput
                            else:
                                raise IndexError

                        else:
                            user_health -= mons_damage
                            time.sleep(0.5)
                            print(f"You struck the {mons_typ} dealing the damage of {usr_damage}hp but,\n"
                                  f"{mons_typ} attacked back and you lost {mons_damage}hp")
                            print(f"Monster health:{mons_health}\n"
                                  f"Your health:{user_health}")
                            print()

                            if user_health <= 0:
                                print("You died!!!!!!!!\n"
                                      f"The {mons_typ} was too strong for you to handle.")
                                exit()

                    elif user_fight_choice == "d":
                        time.sleep(0.5)
                        print("You chose to doge")

                    elif mons_choice == "d":
                        time.sleep(0.5)
                        print(f"{mons_typ} chose to doge")

                elif user_fight_choice == "q":
                    if defeated:
                        print("You defeated:")
                        for mons in defeated:
                            print(f"{defeated[mons]} {mons}")
                            exit()
                    else:
                        print("\nWhat a loser!!!!!")
                        exit()

                else:
                    break

        elif choice.lower() == "q":
            if defeated:
                print("You defeated:")
                for mons in defeated:
                    print(f"{defeated[mons]} {mons}")
                    exit()
            else:
                print("\nWhat a loser!!!!!")
                exit()

        else:
            raise InvalidInput

    except InvalidInput:
        print("\nPlease enter a valid input")

    except IndexError:
        print("\nCongratulations!!! you have successfully defeated all the monsters")
        exit()

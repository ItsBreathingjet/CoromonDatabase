# Add you code here
#Introduction
print(f"Welcome to the Glossary of Coromon, the semi-expansive dictionary for you to learn a little more about these mysterious creatures that live among us.\nThere is a lot to learn about these mysterious creatures and where is a better place to begin then the basic statisics of these Coromon to help you on your future journey! \nWould you like to continue to?")
import sys
import csv
import random
def main():
    while True:
        decision=input("Please type either 'Y' to continue or 'N' to end:")
        if decision.upper() =="N":
            print("Thank you for visiting the Glossary, come again soon!")
            sys.exit()
        elif decision.upper()== "Y":
            print("Welcome to the Glossary of Coromon!")
            #Continue with the program
            coromondata=[]
            with open("CoromonDataset.csv", "r") as datafile:
                reader=csv.reader(datafile)
                header=next(reader)

                for row in reader:
                    coromon=dict(zip(header, row))
                    for key in ["Health Points", "Attack", "Special Attack", "Defense", "Special Defense", "Speed", "Stamina Points"]:
                        coromon[key]=int(coromon[key])
                    coromondata.append(coromon)
            coromon_total=len(coromondata)

            print(f"There are currently a total of {coromon_total} Coromon that exist.\n")

            #Printing a random Coromon and their stats
            random_mon=random.choice(coromondata)
            print(f"Here is a random Coromon:\n{random_mon}\n")

            #Printing the different types of Coromon
            types=set(coromon["Type"] for coromon in coromondata)
            print(f"\nDifferent Types of Coromon: \n{types}\n")

            #Average values for common types and its corresponding Coromons
            typeaverage={}
            for coromon_types in types:
                type_data=[coromon for coromon in coromondata if coromon["Type"]== coromon_types]
                if type_data:
                    average_value= {
                        key: round(sum(coromon[key] for coromon in type_data) / len(type_data))
                        for key in ["Health Points", "Attack", "Special Attack", "Defense", "Special Defense", "Speed", "Stamina Points"]
                    }
                    typeaverage[coromon_types]=average_value
            print(f"Average for Coromon Types:\n")
            for coromon_types, averages in typeaverage.items():
                print(f"{coromon_types}: {averages}\n")

            #Printing the Coromon type with the highest average health points
            def health_points(coromon_types):
                return typeaverage[coromon_types]["Health Points"]
            max_health= max(typeaverage, key=health_points)
            print(f"The Coromon Type with the highest average health points is:\n{max_health}")

            #Printing the Coromon type with the lowest average health points
            def health_points(coromon_types):
                return typeaverage[coromon_types]["Health Points"]
            min_health= min(typeaverage, key=health_points)
            print(f"The Coromon Type with the lowest average health points is:\n{min_health}")

            #Printing the coromon type with the highest average attack points
            def attack_points(coromon_types):
                return typeaverage[coromon_types]["Attack"]
            max_attack= max(typeaverage, key=attack_points)
            print(f"The Coromon Type with the highest average attack points is:\n{max_attack}")

            #Printing the coromon type with the lowest average attack points
            def attack_points(coromon_types):
                return typeaverage[coromon_types]["Attack"]
            min_attack= min(typeaverage, key=attack_points)
            print(f"The Coromon Type with the lowest average attack points is:\n{min_attack}")

            #Printing the coromon type with the highest average special attack points
            def specattack_points(coromon_types):
                return typeaverage[coromon_types]["Special Attack"]
            max_specattack= max(typeaverage, key=specattack_points)
            print(f"The Coromon Type with the highest average attack points is:\n{max_specattack}")

            #Printing the coromon type with the lowest average special attack points
            def specattack_points(coromon_types):
                return typeaverage[coromon_types]["Special Attack"]
            min_specattack= min(typeaverage, key=specattack_points)
            print(f"The Coromon Type with the lowest average attack points is:\n{min_specattack}")

            #Printing the coromon type with the highest average defense points
            def defense_points(coromon_types):
                return typeaverage[coromon_types]["Defense"]
            max_defense= max(typeaverage, key=defense_points)
            print(f"The Coromon Type with the highest average defense points is:\n{max_defense}")

            #Printing the coromon type with the lowest average defense points
            def defense_points(coromon_types):
                return typeaverage[coromon_types]["Defense"]
            min_defense= min(typeaverage, key=defense_points)
            print(f"The Coromon Type with the lowest average defense points is:\n{min_defense}")

            #Printing the coromon type with the highest average special defense points
            def specdefense_points(coromon_types):
                return typeaverage[coromon_types]["Special Defense"]
            max_specdefense= max(typeaverage, key=specdefense_points)
            print(f"The Coromon Type with the highest average special defense points is:\n{max_specdefense}")

            #Printing the coromon type with the lowest average special defense points
            def specdefense_points(coromon_types):
                return typeaverage[coromon_types]["Special Defense"]
            min_specdefense= min(typeaverage, key=specdefense_points)
            print(f"The Coromon Type with the lowest average special defense points is:\n{min_specdefense}")

            #Printing the coromon type with the highest average speed stat
            def speed_points(coromon_types):
                return typeaverage[coromon_types]["Speed"]
            max_speed= max(typeaverage, key=speed_points)
            print(f"The Coromon Type with the highest average speed is:\n{max_speed}")

            #Printing the coromon type with the lowest average speed stat
            def speed_points(coromon_types):
                return typeaverage[coromon_types]["Speed"]
            min_speed= min(typeaverage, key=speed_points)
            print(f"The Coromon Type with the lowest average speed is:\n{min_speed}")

        else:
            print("Invalid input! Please enter either Y or N")
if __name__ == "__main__":
    main()
    
    
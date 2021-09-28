#!/usr/bin/python3

# create a for loop that will display farm information

# farm data set
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


farm_name = farms.get(name)


# create a list of strings
for x in farm_name:
    print("\nThe farm is named" + x, end="")

print("\n" + "The loop has ended")


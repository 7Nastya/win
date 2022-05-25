def print_scrope(students, *balls):
    print(f"Student: {students}", f"Balls today:")
    for x in balls:
        print(x)
print_scrope("Sasha", 4, 5)
def printPetNames(owner, **pets):
   print(f"Owner Name: {owner}")
   for pet,name in pets.items():
      print(f"{pet}: {name}")
printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")

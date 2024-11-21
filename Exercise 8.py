# 8. Simple Search

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_term = "Sam"

if search_term in names:
    print(f"{search_term} found in list.")
else:
    print(f"{search_term} not found in list.")

# user input
search_term = input("Enter the name to search: ")
if search_term in names:
    print(f"{search_term} found in list.")
else:
    print(f"{search_term} not found in list.")

names = open("names.txt", "r").read()
new_file = open("new_names.txt", "w")
new_names = names.title()
new_file.write(new_names)
new_file.close
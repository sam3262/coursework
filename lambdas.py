# list of names
names_list=['Frank Harrelson', 'Bob Sharles', 'Bob Tranklin', 'Bob Grody', 'Hank Charles', 'Bob Rarrelson', 
'Mack Slobson', 'John Jonones', 'Rob Wranklin', 'Tom Simpsonian', 'Rob Rearrelson', 'John Moodys', 
'Frank Shones', 'John Harrelson','Frank Quhorles', 'Tom Pharles', 'Frank Fwanklin', 'Frank Charleston', 
'John Arles', 'John Georanklin', 'Frank Dobsonsoson', 'Diane Johnston', 'Dob Scone', 'Michael Scarn', 
'Goldie Hawn', 'Billie Holliday', 'Woody Harrelson', 'Arthur Rubinstein', 'Thomas Edison', 'Robert Goulet']

#lambda used to sort by last name
names_list.sort(key=lambda name:name.split()[-1].lower())

#printing the sorted ordered names
print(names_list)
#hey = word.split(), last_five = hey[1][0:5]

final_list = []
new_list = names_list.sort(key=lambda name:name.split()[-1].lower())

#for loop for the list
for word in names_list: 
    #spits the names to help take the last name
    last_name = word.split()
    #gets the first two letters of the first name
    first_two = word[0:2]
    #gets first five letters from the last name
    last_five = last_name[1][0:5]
    #puts these selected letters into a new list
    final_list.append(last_five+first_two)
      
#prints the username list
print(f"\n{final_list}")

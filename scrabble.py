
#dictionary of letters and how many points they equate to
point_letters = { 1 : ("a","e","i","o","u","l","n","r","s","t"), 2 : ("d", "g"), \
3 : ("b","c","m","p"), 4 : ("f","h","v","y","w"), 5 : "k", 8 : ("j", "x"), 10 : ("q", "z")}

#starting user scrabble points off at 0 
user_points = 0

#input from the user
word = input("What is your scrabble word? : ")

#store user input as a list to traverse through point letters
word_list = list(word)

#iteration loop to go through all the letters/list of letters
for word in word_list: 

    for key,value in point_letters.items(): 
        for v in value: #finding the each letter within the dictionary of values
            
            if word[0] == v : #finding the key that the letter belongs to
                user_points+=key #adding the point from the letter to the users total points
                
#telling the user how many points they earned from their word
print(f"\nCongratuations, you earned {user_points} points for your word!\n")
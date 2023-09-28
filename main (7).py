sentence=input("Enter a sentence: ")
letter=input("Enter a letter to search: ")

counter=0

for i in range(len(sentence)):
    if sentence[i]==letter:
        counter=counter+1
print("The number of "+ str(letter) + " in the sentence is: "+ str(counter))

again=input("Search for another? ")
while "y" in again.lower():
    for i in range(len(sentence)):
        if sentence[i]==letter:
            counter=counter+1
print("The number of "+ str(letter) + " in the sentence is: "+ str(counter))
again=input("Search for another? ")
# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
#   - my_last_name
#       -set this equal to your last name
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
#   - current_year
#       -set this equal to 2020
firstName = 'Kaden'
lastName = 'McEntire'
birthYear = 2000
currentYear = 2023


# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
#       - last name
#       - first letter of your first name (use the +index)
#       - second letter of your last name (use the -index)
#       - first two letter of your first name (use the +index)
#       - second two letter of your last name (use the -index)
print (firstName)
print (lastName)
print (firstName[0])
print (lastName[-2])
print (firstName[0:2])
print (lastName[-8:-6])



#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
#       -first name six times
print (firstName + " " + lastName)
for i in range (6) :
    print (firstName, end =" ")
print ()


# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
print (firstName, lastName, "was born in", birthYear)
print (firstName, lastName, "was born in", birthYear, ".", firstName, "enjoyed celebrating", currentYear)



# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
#       - tab last name current year
print (firstName + "'s birth year is " + birthYear + "\t" + lastName + " " + currentYear)

# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
#       - length of last name
#       - first name and last name all in upper case
# program to append data to existing file and then display the entire file
f = open('twister.txt', 'a')
f.write('''
How much Fish could Bobby fish fry if bobby fish could fry fish''')
f.close()


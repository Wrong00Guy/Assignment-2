testFi1e = open( 'C:\\Users\\Student\\Desktop\\test.txt','r')
testContent =testFi1e.read()

word_list = testContent. split()
char_dict = { } 
for char in word list:
    if char in char_dict:
     char_dict[char]=char_dict[char]+1
    else :
       char_dict[char] = 1

sorted_dict = sorted(char_dict.items(),key = lamnda item: item[1], reverse = True)

first10pairs =  list(sorted_dict)[:10]
print(first10pairs)
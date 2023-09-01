num = input("Enter a multi digit number: ")
zeros = ones = twos = three = four = five = six = seven = eight = nine = 0
for i in num:
    if i == '0':
        zeros = zeros + 1
    if i == '1':
        ones = ones + 1
    if i == '2':
        twos = twos + 1
    if i == '3':
        three = three + 1
    if i == '4':
        four = four + 1
    if i == '5':
        five = five + 1
    if i == '6':
        six = six + 1
    if i == '7':
        seven = seven + 1
    if i == '8':
        eight = eight + 1
    if i == '9':
        nine = nine + 1


print("Zero's = ", zeros)
print("One's = ", ones)
print("Two's = ", twos)
print("Three's = ", three)
print( "Four s =", four)
print("Five's = ", five)
print("Six's = ", six)
print("Seven's = ", seven)
print("Eight's = ", eight)
print("Nine's = ", nine)
# 1 membuat string

'''

singgle qoute
double qoute

'''
data = 'string dengan single qoute'
print(data)

data = "string dengan double qoute"
print(data)

print("Hello world")
print('Hello World')
print("'hello world'")


# 2 menggunakan tanda \  
print('Hello wor\'ld')

# backlash
print("C:\\user\\lenovo")

# tab
print("hello \t\t\t world")

# backspace 
print("Hello \b world")


# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed
print("baris pertama.\rbaris kedua.") # CR -> carriage return
print("baris pertama.\r\nbaris kedua.") # CRLF -> Line Feed carriage return 

# 3. string literal atau raw

# hati hati
print('\new normal') # akan sala pathnya

# menggunakan raw string
print(r'\newnormal')

# multiline 
print("""
Nama : Andikarna
Jurusan : Informatika
""")




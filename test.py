file = open('file2.txt')
# get all lines of document
content = file.readlines()
n = len(content)
sentence = ""
# return line that don't start with '#'
for i in range(0,n):
    line = content[i].strip()
    if line and line[0].isalnum():
        sentence += line + ' '

print(sentence.strip())



file.close
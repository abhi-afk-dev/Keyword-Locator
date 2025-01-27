word=input('Enter the word you want to search for: ')


with open('test.txt','r') as file:
    count=0
    for line in file:
        count+=1
with open('test.txt','r') as file:
    line=0;    
    for i in range(1,count+1):
        reading=file.readline()
        line+=1
        if word in reading:
            search=True
            break;
        else:
            search = False
    if search == False:
        print(f'{word} is not present in the file')        
    if search == True:   
        print(f'{word} is present in line: ',line)
        


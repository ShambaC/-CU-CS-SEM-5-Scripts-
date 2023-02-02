import sys

def grep(word,file_name):
    file=open(file_name,"r")
    list1=[]

    for line in file:
        data=line.split()
        list1.extend(data)
    print(list1)
    
    c=0
    for i in range(len(list1)):
        if(list1[i]==word or (list1[i].rstrip('.')==word)):
            c+=1
    print("frequency of word ",word," is: ",c)



def most_repeated_grep(file_name):
    file=open(file_name,"r")
    words=[]

    for line in file:
        data=line.split()
        words.extend(data)

    for i in range(len(words)):
        words[i]=words[i].rstrip('.')
    print(words)

    frequency={}
    max=0
    maxword=''
    for x in words:
        c=0
        for y in words:
            if(x==y):
                c=c+1
        if(c>max):
            max=c
            maxword=x
        frequency[x]=c
   
    print("Frequency of all words:")
    print(frequency)
    print("Most repeated word:")
    print(maxword,":",max)

grep(sys.argv[1],sys.argv[2])
most_repeated_grep(sys.argv[2])
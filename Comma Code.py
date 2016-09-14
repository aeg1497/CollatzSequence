#From ch 4 of Automate the boring stuff with python book
#Seperate list by commas and add and and after the last word. 

#function
def comma(ls):
    formatted = '' #formatted list
    ls_len = len(ls) #get length of string
    temp = ''
    #for loop to iterate list
    for i in range(ls_len):
        if i == ls_len - 1:
            temp = ls[i]
            formatted = formatted + 'and ' + temp
        else:
            temp = ls[i]
            formatted = formatted + temp + ', '

    print(formatted)


spam = ['apples', 'bananas', 'tofu', 'cats']
comma(spam)

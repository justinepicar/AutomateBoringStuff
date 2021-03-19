#Comma Code
#Write a function that takes a list value as an argument and returns a string with
# all the items separated by a comma and a space, with and inserted before the last item.
# For example, passing the previous spam list to the function would return
# 'apples, bananas, tofu, and cats'. But your function should be able to work with any
# list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

def commaCode(stringList):
    sentence=''
    if len(stringList)==0:
        return str('This list is empty.')
    for i in stringList:
        sentence+=str(i)
        if stringList.index(i)==len(stringList)-2: #if value is 2nd to last, add 'and'
            if len(stringList)== 2: #if there are only two items on the list
                sentence+=' and '
            else: #if there are more than 2 items on the list
                sentence+=', and '#since index is defined as value in list
        elif stringList.index(i)==len(stringList)-1: #if it is the last value on the list
            sentence+='.'
        else:
            sentence+=', '
    return sentence

list1=['apples']
list2=['apples','bananas']
list3=['apples','bananas','tofu']
list4=['apples','bananas','tofu','cats']
list5=[]

print(commaCode(list1))
print(commaCode(list2))
print(commaCode(list3))
print(commaCode(list4))
print(commaCode(list5))

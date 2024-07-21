books_list = []
print("when your books list finish,type 'finish' ")
x = str()
while x != "finish":
    x = str(input("please enter your book name:"))
    books_list.append(x)
if x=="finish":
    print(books_list)
    x = str(len(books_list))
    print("you have " + x + " books" )

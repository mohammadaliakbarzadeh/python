b = int(input("Enter Number 1 :"))
c = int(input("Enter Number 2 :"))
d = int(input("Enter Number 3 :"))
e = int(input("Enter Number 4 :"))

def binary(a):

    numbers = [128,64,32,16,8,4,2,1]
    answer_a = list()
    a_1 = int()
    for i in numbers:
        a_1 = a - i
        if a_1 >= 0 :
            answer_a.insert(8,1)
            a = a_1
        elif a_1 < 0:
            answer_a.insert(8,0)
            a_1 = a
    return(" ".join(str(e) for e in answer_a))

print(binary(b)+"."+binary(c)+"."+binary(d)+"."+binary(e))

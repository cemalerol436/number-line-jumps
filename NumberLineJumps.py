
def kangaroo(x1, v1, x2, v2):

    if v2>=v1:
        return "NO"

    else:
        i=0
        while i<10001 :

            x1 += v1
            x2 += v2

            if x1==x2 :
                return "YES"
            elif x1>x2:
                return "NO"
            i += 1


x1 = int(input("1:"))

v1 = int(input("2:"))

x2 = int(input("3:"))

v2 = int(input("4:"))

result = kangaroo(x1, v1, x2, v2)

print(result)

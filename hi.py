new_list = [4,7,890,88,76]
sum = 0

for i in new_list:
    sum = sum + i
    print(sum)

print(sum)

t = [(2,3),(3,4)]

for (j,k) in t:
    print(j)
    print(k)



lis_comp = [x**2 for x in range(0,11) if x%2 == 0]


print(lis_comp)


word = 'subash'

for i,j in enumerate(word):
    print(i,j)


def check_even_list(ne_list):
    for number in ne_list:
        if number % 2 == 0:
            return True
        else:
            pass

print(check_even_list([7,8,9,6]))




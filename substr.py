name = 'subash'


# for i in range(1, len(name) + 1):
#     print(name[:i])




for i in range(len(name)):
    print(i)
    for j in range(i + 1, len(name) + 1):
        print(j)
        print(name[i:j])



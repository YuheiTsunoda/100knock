def n_gram(target,n):

    result=[]

    for i in range(0, len(target)-n+1):
        result.append(target[i:i+n])

    return result

target1 = "paraparaparadise"
target2 = "paragraph"

set_x = set(n_gram(target1,2))
set_y = set(n_gram(target2,2))

# 和集合
set_or = set_x | set_y
print("和集合"+ str(set_or))

set_and = set_x & set_y
print("積集合"+ str(set_and))

set_sub = set_x - set_y
print("差集合"+ str(set_sub))

# 'se'が含まれるか？
print('seがXに含まれる:' + str('se' in set_x))
print('seがYに含まれる:' + str('se' in set_y))

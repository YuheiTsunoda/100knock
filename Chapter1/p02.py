from functools import reduce

target1 = "パトカー"
target2 = "タクシー"
result = "".join(reduce(lambda x, y: x+y, zip(target1, target2)))

result2= ""
for(a,b) in zip(target1,target2):
    result2 += a+b

print(result)
print(result2)

def permutation(list, res):
   if list == 1:
      return res
   else:
      return [ 
         y + x
         for y in permutation(1, res)
         for x in permutation(list - 1, res)
      ]
list1 = ["a","b","c"]
print(list1 - 1)
print(permutation(1, ["a","b","c"]))
print(permutation(2, ["a","b","c"]))

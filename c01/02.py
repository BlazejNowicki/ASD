numbers = [8, 19, 11, 4, 21, 22, 7, 22]

def min_max(l):
  if l[0] >= l[1]:
    min_l = l[1]
    max_l = l[0]
  else:
    min_l = l[0]
    max_l = l[1]
 #TODO poprawić dla nieparzystych
  for x in range(2, len(l), 2):
    if l[x] >= l[x+1]:
      if min_l > l[x+1]:
        min_l = l[x+1]
      if max_l < l[x]:
        max_l = l[x]
    else:
      if min_l > l[x]:
        min_l = l[x]
      if max_l < l[x+1]:
        max_l = l[x+1]
  return min_l, max_l


min_l, max_l = min_max(numbers)
print(f'Minimum: {min_l}, maximum: {max_l}')
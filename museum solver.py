import itertools
# === LOADING DATA ===
workers = []

f = open("workers.txt", "r")
for x in f:
  if x[0] == '#':
    continue
  x = x.split(" ")
  
  person = {
      "name": x[0],
      0: int(x[1]),
      1: int(x[2]),
      2: int(x[3])
    }
  workers.append(person)

rooms = []
f = open("rooms.txt", "r")
for x in f:
  if x[0] == '#':
    continue
  x = x.split(" ")
  
  location = {
      "name": x[0],
      0: int(x[1])-int(x[4]),
      1: int(x[2])-int(x[5]),
      2: int(x[3])-int(x[6])
    }
  rooms.append(location)

#print(workers)
#print(rooms)

# === ALGORITHM ===

num_needed = len(rooms) * 3

best_score = 0
best_orient = None
best_score_offby = 0
for n, i in enumerate(itertools.permutations(workers, num_needed)):
  score = 0
  score_offby = 0
  for r, room in enumerate(rooms):
    first_item = r*3
    
    v1 = i[first_item][0] + i[first_item+1][0] + i[first_item+2][0]
    if  v1 > room[0]:
      score += 1 
    else:
      score_offby += (room[0] - v1)
      
    v2 = i[first_item][1] + i[first_item+1][1] + i[first_item+2][1]
    if  v2 > room[1]:
      score += 1
    else:
      score_offby += room[1] - v2
    
    v3 = i[first_item][2] + i[first_item+1][2] + i[first_item+2][2]
    if  v3 > room[2]:
      score += 1
    else:
      score_offby += room[2] - v3
      
  if score > best_score:
    best_score = score
    best_orient = i
    best_score_offby = score_offby
    if best_score == num_needed*3:
      break 
  elif score == best_score and score_offby < best_score_offby:
    best_score = score
    best_orient = i
    best_score_offby = score_offby
  
  #if n % 10000 == 0:
    #print(n)

for r, room in enumerate(rooms):
  print("===" + room['name'] + "===")
  start = r*3
  print(best_orient[start+0]["name"])
  print(best_orient[start+1]["name"])
  print(best_orient[start+2]["name"])

input()

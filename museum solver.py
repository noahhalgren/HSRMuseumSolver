import itertools

# === LOADING DATA ===

workers = []
with open("workers.txt", "r") as f:
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
with open("rooms.txt", "r") as f:
    for x in f:
        if x[0] == '#':
            continue
        x = x.split(" ")
        location = {
            "name": x[0],
            0: int(x[1]) - int(x[4]),
            1: int(x[2]) - int(x[5]),
            2: int(x[3]) - int(x[6])
        }
        rooms.append(location)

# === ALGORITHM ===

num_needed = len(rooms) * 3
best_score = 0
best_orient = None
best_score_offby = 0

for combination in itertools.combinations(workers, num_needed):
    score = 0
    score_offby = 0
    for r, room in enumerate(rooms):
        start = r * 3
        total_values = [0, 0, 0]
        for worker in combination[start:start+3]:
            for i in range(3):
                total_values[i] += worker[i]
        for i in range(3):
            if total_values[i] > room[i]:
                score += 1
            else:
                score_offby += room[i] - total_values[i]
    if score > best_score:
        best_score = score
        best_orient = combination
        best_score_offby = score_offby
        if best_score == num_needed * 3:
            break
    elif score == best_score and score_offby < best_score_offby:
        best_score = score
        best_orient = combination
        best_score_offby = score_offby

for r, room in enumerate(rooms):
    print("===" + room['name'] + "===")
    start = r * 3
    print(best_orient[start]["name"])
    print(best_orient[start + 1]["name"])
    print(best_orient[start + 2]["name"])

input()

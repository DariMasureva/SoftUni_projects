queue = int(input())
lift = list(map(int, input().split()))
max_people = len(lift) * 4

for idx, wagon in enumerate(lift):
    spots_to_be_filled = 4 - wagon

    if queue > 0 and spots_to_be_filled > 0:

        if queue > spots_to_be_filled:
            lift[idx] = 4
            queue -= spots_to_be_filled
        else:
            lift[idx] += queue
            queue = 0
            break

    elif queue == 0:
        break

if queue == 0 and sum(lift) < max_people:
    print("The lift has empty spots!")

if sum(lift) == max_people and queue > 0:
    print(f"There isn't enough space! {queue} people in a queue!")

lift = list(map(str, lift))
print(" ".join(lift))

sequence = input().split()
segments = round(len(sequence)/2) - 1
left_time = 0
right_time = 0

for segment_idx in range(segments):
    time = int(sequence[segment_idx])

    if time == 0:
        left_time *= 0.8
    else:
        left_time += time

for segment_idx in range(-1, segments * (-1) - 1, -1):
    time = int(sequence[segment_idx])

    if time == 0:
        right_time *= 0.8
    else:
        right_time += time

if right_time < left_time:
    winner = right_time
    name = "right"
else:
    winner = left_time
    name = "left"

print(f"The winner is {name} with total time: {winner:.1f}")

h = float(input())
w = float(input())

w_cm = w * 100
w_after_loss = w_cm - 100
h_cm = h * 100
num_w_seats = w_after_loss // 70
num_h_seats = h_cm // 120
total_seats = num_h_seats * num_w_seats - 3

print(total_seats)

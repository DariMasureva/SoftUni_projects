hall = int(input())

statuettes = 0.7 * hall
catering = 0.85 * statuettes
sound = 0.5 * catering

total = "{:.2f}".format(statuettes + catering + sound + hall)

print(total)


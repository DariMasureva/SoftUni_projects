def tribonacci_seq(print_count: int):
    initial_seq = [1, 1, 2]

    if print_count < len(initial_seq):
        return initial_seq[:print_count]

    for _ in range(print_count - 3):
        length = len(initial_seq)
        next_num = sum(initial_seq[length - 3:length])
        initial_seq.append(next_num)

    return initial_seq


number_count = int(input())
final_sequence = tribonacci_seq(number_count)
final_sequence = [str(number) for number in final_sequence]

print(" ".join(final_sequence))

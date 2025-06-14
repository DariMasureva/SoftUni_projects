def swap(first_el: str, sec_el: str, parent_list):
    first_idx = parent_list.index(first_el)
    sec_idx = parent_list.index(sec_el)
    potential_first_ex = f"{first_el}-Exercise"
    potential_sec_ex = f"{sec_el}-Exercise"

    parent_list[first_idx], parent_list[sec_idx] = parent_list[sec_idx], parent_list[first_idx]

    if potential_first_ex in initial_schedule:
        initial_schedule.remove(potential_first_ex)
        initial_schedule.insert(sec_idx + 1, potential_first_ex)

    if potential_sec_ex in initial_schedule:
        initial_schedule.remove(potential_sec_ex)
        initial_schedule.insert(first_idx + 1, potential_sec_ex)


def manage_exercise(title, parent_list):
    ex_title = f"{title}-Exercise"

    if title not in parent_list:
        parent_list.append(title)

    title_idx = parent_list.index(title)
    parent_list.insert(title_idx + 1, ex_title)


initial_schedule = input().split(", ")
command = input()

while command != "course start":
    command = command.split(":")
    function = command[0]
    cur_lesson = command[1]

    if function == "Add":
        if cur_lesson not in initial_schedule:
            initial_schedule.append(cur_lesson)

    elif function == "Insert":
        idx = int(command[2])
        if cur_lesson not in initial_schedule:
            initial_schedule.insert(idx, cur_lesson)

    elif function == "Remove":
        if cur_lesson in initial_schedule:
            initial_schedule.remove(cur_lesson)

    elif function == "Swap":
        cur_lesson_swap = command[2]

        if cur_lesson in initial_schedule and cur_lesson_swap in initial_schedule:
            swap(cur_lesson, cur_lesson_swap, initial_schedule)

    elif function == "Exercise":
        exercise = f"{cur_lesson}-Exercise"

        if exercise not in initial_schedule:
            manage_exercise(cur_lesson, initial_schedule)

    command = input()

final_schedule = [(idx, lesson) for idx, lesson in enumerate(initial_schedule, 1)]

for number, lesson in final_schedule:
    print(f"{number}.{lesson}")

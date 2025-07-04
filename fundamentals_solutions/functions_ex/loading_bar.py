def loading_bar(percent_loaded: int):
    percent_sign_count = int(percent_loaded / 10)
    dots_count = 10 - percent_sign_count

    if percent_loaded == 100:
        message = "Complete!"
    else:
        message = "Still loading..."

    load_bar = "[" + "%" * percent_sign_count + "." * dots_count + "]"
    perc_visualisation = f"{percent_loaded}%"

    return load_bar, message, perc_visualisation


percent = int(input())
cur_load_bar, cur_message, cur_perc_visualisation = loading_bar(percent)
print(cur_perc_visualisation, end=" ")

if percent == 100:
    print(f"{cur_message}\n{cur_load_bar}")
else:
    print(f"{cur_load_bar}\n{cur_message}")

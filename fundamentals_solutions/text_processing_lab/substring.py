substr = input()
main_str = input()

while substr in main_str:
    main_str = main_str.replace(substr, "")
print(main_str)

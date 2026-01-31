# TODO-1: Ask the user for input
print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

bidders = {}
process = True

while process:
    key = input("What is your name?:  ")
    value = int(input("What is your bid?: $  "))
    bidders[key] = value
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n  ").lower()
    print('\n' * 100)
    if other_bidders == "yes":
        process = True
    elif other_bidders == "no":
        process = False
        if not process != False:
            highest_bid = max(bidders.values())
            highest_key = max(bidders, key=bidders.get)
            print(f"The highest bid was done by {highest_key} which was $ {highest_bid} .")
    else:
        print('Choose a valid option')





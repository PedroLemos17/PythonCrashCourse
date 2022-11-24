# Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.

flag = True
print("Enter q when you want to quit\n")
while(flag):
    reason=input("Why do you like programming?\n")
    if reason == 'q':
        flag=False
    else:
        with open("reasons.txt", 'a') as file:
            file.write(f"{reason}\n")
# Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.

short_messages=["hello my baby", "hello my honey", "hello my ragtime pal"]
sent_messages=[]

def show_messages(list):
    for value in list:
        print(f"{value.title()}\n")

def send_message(origin, destiny):
    while origin:
        current_value=origin.pop()
        print(f"{current_value.title()}\n")
        destiny.append(current_value)
        
send_message(short_messages[:], sent_messages)
print("Lists:\n")
show_messages(sent_messages)
show_messages(short_messages)
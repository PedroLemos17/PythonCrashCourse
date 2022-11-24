# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

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
        
send_message(short_messages, sent_messages)
print("Lists:\n")
show_messages(sent_messages)
show_messages(short_messages)
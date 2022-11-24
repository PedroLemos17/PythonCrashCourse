# Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

short_messages=["hello my baby", "hello my honey", "hello my ragtime pal"]

def show_messages(list):
    for value in list:
        print(f"{value.title()}\n")

show_messages(short_messages)
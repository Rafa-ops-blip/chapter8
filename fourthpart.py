#8.9 Messages
def show_messages(messages):
  for message in messages:
    print(message)

other_messages = ["Hello!", "How are you?", "Safe trip home", "See you later", "come back here!"]


show_messages(other_messages)


#8.10 Sending messages
def send_messages(messages, sent_messages):
  """print each text messages and move them to sent_messages list"""
  for message in messages:
    print(f"Sending messages: {message}")
    sent_messages.append(message)
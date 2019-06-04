import time, sys, random, re
#hardcoded
responses = {
"what's your name?": [
"my name is EchoBot",
"they call me EchoBot",
"they know me as Echobot"],"hello":["hello","hallo"]
}
def response(message):
  if message in responses:
    return random.choice(responses[message])
  else:
    return "i didn't get that: "+ message


def send_message(message):
  argument = message
  #history += argument
  res = response(argument)
  ant = "Echobot: "+res
  print("Echobot is typing...")
  time.sleep(random.randrange(1,5))
  print(ant)
name = input("Echobot: what's youre name? ")
while True:
    message = input(name+": ")
    send_message(message)



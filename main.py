import time, sys, random, re
#hardcoded list with answer
responses = {
"what's your name?": [
"My name is EchoBot",
"They call me EchoBot",
"They know me as Echobot"],"hello":["Hello","Hallo"],"hi":["Hallo", "Hi"]
}
#swap pronouns function
def swap_pronouns(phrase):
  phrase = phrase
  if ' i' in phrase:
    #print("test")
    phrase = re.sub(' i', ' you', phrase)
    #print(phrase)
  if ' my' in phrase:
    phrase = re.sub(' my', ' your', phrase)
  if ' me' in phrase:
    phrase = re.sub(' me', ' you', phrase)
  return phrase
#list with messages if there is no input typed.
nomessage = ["I cant answer to nothing", "Say something!",  "I lose intrest when I get ignored", "Silence is an answer too but not one where I can do something with", "I didn't text you just to exercise my fingers!, I was expecting a reply back"]
#pattern matching list
pattern_responses = {"do you remember (.*)":["Of course I remember {}","Yes I do remember {}"],"stupid(.*)":["Im not stupid","why do you think Im stupid?"],"smart(.*)":["smarter than you atleast", "based on your question Im smarter than you", "It depends on what you call smart"]
  ,"i feel (.*)":["Why do you feel {}","You feel {}, why?"],"what can (.*)": ["I can do a lot", "What do you want me to do?"], "hallo(.*)": ["Hello", "Hello, what can I do for you?"],"can you(.*)":["Can you?", "I can", "I can make {}"], "how are(.*)":["Im doing good", "Im fine"],"can i(.*)":["Do you want to?", "You can!"],"who(.*)":["I am echobot", "does it matter?", "They call me echobot", "Do you know who {} is?"],"echobot":["That is my name", "Hello"], "what do(.*)":["I did not", "What did I do?"],"im in(.*)":["How is it in{}?","Why are you in{}?"], "hi(.*)":["Hello","Hi"],"hello(.*)":["Hello","Hi"], "what are(.*) ":["Im in this chat","Im doing what I need to do"],"why(.*)":["Why not?","Why are you asking?"],"old(.*)":["Does it matter?", "Im "+str(random.randrange(1,1000))+" years old"],"are you(.*)": ["Im doing fine", "Im doing well"], "bad(.*)":["why are you feeling bad?","why do you feel bad?"],"good":["Im also doing good", "what makes you feel good?"]}
#pattern match function
def check_pattern(message):
  for pattern in pattern_responses:
    match = re.search(pattern, message)
    if match:
      answer = random.choice(pattern_responses[pattern])
      #print(match.group(1))
      answer2 = answer.format(swap_pronouns(match.group(1)))
      return answer2
  return ""
#create a response
def response(message):
  message = message.lower()
  if message in responses:
    return random.choice(responses[message])
  else:
    ret = check_pattern(message)
    if ret != "":
      return ret
    else:
      if message == " " or message == "":
        return random.choice(nomessage)
      else:
        return "Hmm that's intresting"

#send response to chat
def send_message(message):
  argument = message
  #history += argument
  res = response(argument)
  ant = "Echobot: "+res
  print("Echobot is typing...")
  time.sleep(random.randrange(1,5))
  print(ant)
#ask the name of the user
def askname():
  noname = ["typing youre name is not that dificult, try again!", "no name, no chat!", "youre real name!, try again!", "youre name cant be nothing!", "I gave my name now it is youre turn, try again!", "youre name please"]
  name = input("Echobot: what's your name? ")
  if name == "" or name == " ":
    print("echobot: "+random.choice(noname))
    return name
  else:
    print("Echobot: hello",name , "welcome to the chat")
    return name
#call the askname function
name = askname()
#create responses when the chatbot crashed.
crashlist = ["There was an error in my brain", "I think my brain just crashed..."]
#infinite loop
while True:
  #try to ask the name of the user and if there is a name return a message.
  try:
    if name == "" or name == " ":
      name = askname()
    else:
      message = input(name+": ")
      send_message(message)
  #if this fails return a answer from the crashlist
  except:
    print("echobot: "+random.choice(crashlist))
    print("echobot has left the chat")



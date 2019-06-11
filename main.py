import time, sys, random, re
#hardcoded
responses = {
"what's your name?": [
                      "My name is EchoBot",
                      "They call me EchoBot",
                      "They know me as Echobot"],"Hello":["Hello","Hallo"]
}
#swap pronouns
def swap_pronouns(phrase):
    #save the variable
    phrase = phrase
    #check for pronouns
    if 'I' in phrase:
        phrase = re.sub('I', 'you', phrase)
    if 'my' in phrase:
        phrase = re.sub('my', 'your', phrase)
    if 'me' in phrase:
        phrase = re.sub('me', 'you', phrase)
#   return the checked text
    return phrase
#list with sentences how can be used if the input is empty
nomessage = ["I cant answer to nothing", "say something!",  "I lose intrest when I get ignored", "silence is an answer Too but not one where I can do something with", "I didn't text you just to exercise my fingers!, I was expecting a reply back"]
#list for pattern maching
pattern_responses = {"do you remember (.*)":["Of course I remember {}","Yes I do remember {}"],
    "i feel (.*)":["Why do you feel {}","You feel {}, why?"],"what can (.*)": ["I can do a lot", "what do you want me to do?"], "hallo(.*)": ["Hallo", "hallo, what can I do for you?"],"can you(.*)":["can you?", "I can", "I can make {}"], "how are(.*)":["Im doing good", "Im fine"],"can i(.*)":["Do you want to?", "you can!"],"who(.*)":["I am echobot", "does it matter?", "They call me echobot", "Do you know how {} is?"],"echobot":["That is my name", "Hello"]}
#pattern match function
def check_pattern(message):
    #search for patterns
    for pattern in pattern_responses:

        match = re.search(pattern, message)
        if match:
            answer = random.choice(pattern_responses[pattern])
            answer2 = answer.format(match.group(1))
        return answer2
    return ""

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
                return "i didn't get that: "+ message


def send_message(message):
    argument = message
    #history += argument
    res = response(argument)
    ant = "Echobot: "+res
    print("I am typing...")
    time.sleep(random.randrange(1,5))
    print(ant)
def askname():
    noname = ["typing your name is not that difficult, try again!", "no name, no chat!", "your real name!, try again!", "you're name cant be nothing!", "I gave my name now it is your turn, try again!", "you're name please"]
    name = input("Echobot: what's your name? ")
    if name == "" or name == " ":
        print("echobot: "+random.choice(noname))
        return name
    else:
        print("Echobot: hello",name , "welcome to the chat")
        return name
name = askname()
crashlist = ["That was an error in my brain", "I think my brain just crashed..."]
while True:
    try:
        if name == "" or name == " ":
            name = askname()
        else:
            message = input(name+": ")
            send_message(message)
    except:
        print("echobot: "+random.choice(crashlist))



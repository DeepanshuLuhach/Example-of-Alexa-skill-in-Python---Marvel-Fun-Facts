import static as stc
import random
# Lambda has to deal with these 3 intents only, for custom alexa skill
def lambda_handler(event, context) : 
	if event['request']['type'] == 'LaunchRequest' : 
		return on_launch()
	elif event['request']['type'] == 'IntentRequest' : 
		return on_intent(event)
	elif event['request']['type'] == 'SessionEnded' :
		return on_session_ended()

# Greet user on launch, remember the intent is not called yet
def on_launch():
	Messages = [
		"Welcome, how about some interesting marvel facts?",
		"Let's find you some interesting facts about your favourite marvel character",
		"Hi there, how can I help you today?",
		"Welcome, this skill has more than 500 facts, let me pick the speacial one for you.",
		"Hello there, you are a true marvel fan, let me tell you some interesting facts",
		"Hello there, what can I do for you today",
		"Hello, nice to meet you."
	]
	return response(getRandom(Messages), False)

# What to do when an intent is called. 
def on_intent(event) : 
	intent = event['request']['intent']

	intent_name = intent['name']
	if intent_name == 'GetFunFactIntent':
		return GetFunFactIntent(intent)
	elif intent_name == 'AMAZON.CancelIntent' : 
		return on_stop()
	elif intent_name == 'AMAZON.HelpIntent' : 
		return on_help()
	elif intent_name == 'AMAZON.StopIntent' : 
		return on_stop()	
	else:
		print("Incorrect intent, return help")
		return on_help()

# This will give us the fact we need 
def GetFunFactIntent(intent):
	character = getSlotValue(intent, 'Character')
	if character != -1 : 
		character = character.lower()
		character = alterName(character) 
		# alterName() will give us their "made up names", if the user give us their real name
		char_facts = stc.characters
		for k, v in char_facts.iteritems() : 
			if k == character :
				array = v
				return response(getRandom(array))
				# getRandom return a random value from the passed array
		return response("Sorry, I don't know about " + character + ". I know only about spider man, captain marvel, hulk, thor, iron man, captain america, black widow, black panther, falcon, scarlet witch, vision, ant man, doctor strange, loki, venom, deadpool, thanos", False)
	else : 
		facts = stc.facts
		return response(getRandom(facts))

# returns the slot value if the slot slot_name is present in the input json, -1 otherwise
def getSlotValue(intent, slot_name) : 
	if intent.has_key('slots') : 
		if intent['slots'].has_key(slot_name) : 
			if intent['slots'][slot_name].has_key('value') : 
				return intent['slots'][slot_name]['value']

	return -1;
# user may speak alternate name of the character, altername checks them and returns their "made up names"
def alterName(character) : 
	if character == 'peter parker' : 
		return "spider man"
	elif character == 'carol danvers' or character == 'carol' : 
		return "captain marvel"
	elif character == 'bruce banner' or character == 'banner' :
		return "hulk"
	elif character == 'god of thunder' : 
		return "thor"
	elif character == 'tony stark' or character == 'tony': 
		return "iron man"
	elif character == 'steve rogers' or character == 'steve' or character == 'rogers' :
		return "captain america"
	elif character == 'natalia alianovna romanova' or character == 'romanova' or character == 'natasha' or character == 'natalia' : 
		return "black widow"
	elif character == 't\'chala' or character == 'wakanda king' : 
		return "black panther"
	elif character == 'samuel thomas' or character == 'sam' : 
		return "falcon" 
	elif character == 'wanda maximoff' or character == 'wanda' : 
		return "scarlet witch"
	elif character == 'hank pym' or character == 'hank' : 
		return "ant man"
	elif character == 'stephen vincent strange' or character == 'strange' or character == "doctor stephen" : 
		return "doctor strange"
	elif character == 'eddie brock' or character == 'edie brock' or character == 'eddie' :
		return "venom"
	elif character == 'wade wilson' or character == 'wade' : 
		return "deadpool"
	else :
		return character

# tells the user how to use the skill
def on_help() : 
	output = "You can say 'tell me some fun facts', " \
	"or you can ask for your favourite character, for example you can say, 'tell me some facts about doctor strange. " \
	"What can I do for you?"
	return response(output, False)

def on_stop():
	Messages = [
		"See ya",
		"Bye bye",
		"tata",
		"Hope to see you again",
		"Let me know if you want to hear about some more marvel characters",
		"ciao",
		"sayonara"
	]
	return response(getRandom(Messages))



def getRandom(array) : 
	return array[random.randint(0, len(array) - 1)]

# this is the response which the user will get
def response(output, shouldEndSession = True) : 
	print("\n")
	print(output)
	print("\n")
	return {
		'version' : '1.0',
		'response' : {
			'shouldEndSession' : shouldEndSession,
			'outputSpeech' : {
				'type' : 'PlainText',
				'text' : output
			}
		}
	}


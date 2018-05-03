import static as stc
import random
def lambda_handler(event, context) : 
	if event['request']['type'] == 'LaunchRequest' : 
		return on_launch()
	elif event['request']['type'] == 'IntentRequest' : 
		return on_intent(event)
	elif event['request']['type'] == 'SessionEnded' :
		return on_session_ended()

def on_launch():
	return response("Hello, nice to meet you.", False)

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

def GetFunFactIntent(intent):
	facts = stc.facts
	return response(facts[random.randint(0, len(facts) - 1)], True)


def response(output, shouldEndSession) : 
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


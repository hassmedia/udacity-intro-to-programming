import twilio
from twilio.rest import TwilioRestClient

'''
This is a program for sending text messages using 'twilio'.
'''

# check twilio version
print "twilio version: " + twilio.__version__
 
# account sid and auth Token from twilio.com/user/account
account_sid = "account-sid"
auth_token  = "auth-token"
client = TwilioRestClient(account_sid, auth_token)
 
# message content and receiver, these are just random numbers
# for testing. 
message = client.messages.create(body="Hello!",
    to="+35644556667", from_="+46100388850")

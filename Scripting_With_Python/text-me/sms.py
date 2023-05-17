from twilio.rest import Client

account_sid = 'ACbb4029feabb4aea5b977574d51f17c6c'
auth_token = '338aa565b4c2d6dcb8ed48f87d6ed83c'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18449531229',
  body='Auth Token used in python sms.py script',
  to='+19195998704'
)

print(message.sid)
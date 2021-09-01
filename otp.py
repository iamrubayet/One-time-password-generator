import twilio
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random # generate random number
otp = random.randint(1000,9999)
print("Your OTP is - ",otp)
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC37259de9578f64e16a161292e9e1749#'
auth_token = 'e9878ae07027a77b3cb16874bc67418#'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='Your Secure Device OTP is - ' + str(otp) +     'use this otp...',
         from_='+19132701673',
         to='+8801764259025'
     )

print(message.sid)

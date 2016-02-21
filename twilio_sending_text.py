from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACbd1299bb37237f5d434a9fb08121e9cc" 
AUTH_TOKEN = "d09e9acc9e62006f280b8377539566fc" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to="+918792362659", 
    from_="+12018028195", 
    body="Hey Brandy!! What's Up? !!", 
    #media_url="http://farm2.static.flickr.com/1075/1404618563_3ed9a44a3a.jpg", 
)
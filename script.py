from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

account_sid = 'ACab1199d1213963e4669ea072dcb7e8a5' 
auth_token = '316ff6c6207783e2728a5ef3960d1913'

client = Client(account_sid, auth_token)

response = VoiceResponse()
response.say('Toma tus pastillas!', voice='woman', language='es-ES')

def callmsg():    
    call = client.calls.create(
          from_='+12535232944', 
          twiml=response,
          to='+994705899298'   
    )
   
 


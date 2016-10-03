from requests_oauthlib import OAuth1Session
import json

from OSC import OSCClient, OSCMessage
client = OSCClient()
client.connect( ("localhost", 6667) )

from time import sleep

CK = 'i4MgdpomXISoSQsXUK7LQHH5C'                             # Consumer Key
CS = 'f4a3sfBliNPgLRzxSOXYltsbHL1oUjPpCqDGjRyWuujuIriVw7'         # Consumer Secret
AT = '2914968338-9XGVF3oUci0j0o3nxGSK6vgtgoLd91WAawO4Ldu' # Access Token
AS = 'aWRPiUQA7c5z0kZIEKF3Qj6opoypfzZ5ay8jNf7MCO5wz'         # Accesss Token Secert



url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

tweet_id = 0
screen_name = 'lightmanshinajo'
while 1:
    if tweet_id == 0:
        params = {
            'screen_name': screen_name,
            'count' : 1
        }
    else:
        params = {
            'screen_name': screen_name,
            'count' : 20,
            'since_id' : tweet_id
        }


    twitter = OAuth1Session(CK, CS, AT, AS)

    req = twitter.get(url, params = params)
    

    if req.status_code == 200:
    
        timeline = json.loads(req.text)
        
        count = 0
        for tweet in timeline:
            msg = tweet["text"].encode('utf-8')
            client.send( OSCMessage("/tweet", msg) )
            
            if count == 0 :
                tweet_id = tweet["id_str"]
            count = count+1
            
            print(msg)
    else:
        print ("Error: %d" % req.status_code)

    sleep(6);
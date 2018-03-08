#Working with google maps api
import urllib.request
import json
import re

#Get Google maps API key for distance matrix here: https://developers.google.com/maps/documentation/distance-matrix/
#Get token and key for twitter here:   https://apps.twitter.com/


#For twitter
import tweepy 




# Part 1:  Update Twitter Status function

#Please use your  key and token 

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def tweet_update(tweet):
    #TWITTER KEY AND TOKEN
  cfg = { 
    "consumer_key"        : "Value",
    "consumer_secret"     : "Value",
    "access_token"        : "Value",
    "access_token_secret" : "Value" 
    }

  api = get_api(cfg)
  status = api.update_status(status=tweet) 


  
  
  
  
#Part 2: Google Maps api 


def get_distance():
    endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    
    #USE YOUR GOOGLE MAPS API DISTANCE MATRIX KEY  
    api_key = 'Value'
    
    #Origin and destination
    origin = input('Source Address: ').replace(' ','')
    destination = input('Destination Address: ').replace(' ','')
    
    #request
    nav_request = 'origins={}&destinations={}&key={}'.format(origin,destination,api_key)
    request = endpoint + nav_request 
    response = urllib.request.urlopen(request).read()
    
    #Read json
    directions  = json.loads(response.decode('utf-8'))
    
    #print(directions)
    
    #Getting distance between the points 
    distance = directions['rows'][0]['elements'][0]['distance']['text']
    
    #Distance in float
    distance_num = float(''.join(re.findall("\d+\.\d+", distance)))
    
    #Taking maximum distance as 100 to check same city
    if int(distance_num) > 100:
        return 'Make sure source and destination are in the same city'
    else:
        tweet = distance + ' is the driving distance between ' + origin + ' and ' + destination + '.'
        tweet_update(tweet)
        return tweet
    

        
if __name__ == "__main__":
    get_distance()
    
    
    
    


  
  
import twitter
import tweepy
from tweepy import OAuthHandler
consumer_key = "hEDGEdp4p2Tp8U6h5vpOGOpm9"
consumer_secret = "4C8P1YeOtsjebf6dYyTnRCWae3GWWoF9n6VLnQOKTEorlK3KbT"
access_token = "846992744690208768-QQKUada7IjhguoQyjrARQ99nCkHVMop"
access_token_secret = "5zfmqKV2eLPO2SU0XoW3DKtOUqwmvpPB1r7KoQ48OQnq8"
authorization = twitter.OAuth(access_token, access_token_secret, consumer_key, consumer_secret)
t = twitter.Twitter(auth=authorization)

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, proxy="socks5://127.0.0.1:1080")
print("api")

for status in tweepy.Cursor(api.home_timeline).items(2):
    print (status.text)

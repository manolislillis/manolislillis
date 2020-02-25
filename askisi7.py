import tweepy 
  
consumer_key = "" 
consumer_secret = ""
access_key = ""
access_secret = ""
  
 
def get_tweets(username,count):  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
    auth.set_access_token(access_key, access_secret)  
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name=username,count=2) 
    tweets_for_csv = [tweet.text for tweet in tweets] 
    for j in tweets_for_csv:
        for i in range (len(j.split())):
            count=count+1

    return count
   
if __name__ == '__main__': 
   
    User1=str(input(" Δώσε πρώτο όνομα: "))
    User2=str(input(" Δώσε δεύτερο όνομα: "))
    count1=0
    count2=0
    count1=get_tweets(User1,count1)
    count2=get_tweets(User2,count2)
    if (count1>count2):
        print("ο χρήστης:",User1,"έχει περισσότερες λέξεις στα τελευταία 50 tweet από τον χρήστη:",User2)

    if (count1<count2):
        print("ο χρήστης:",User2,"έχει περισσότερες λέξεις στα τελευταία 50 tweet από τον χρήστη:",User1)

    if (count1==count2):
        print("Οι χρήστες",User1,"και",User2,"έχουν ακριβώς τον ίδιο αριθμό λέξεων στα τελευταία 50 tweets")

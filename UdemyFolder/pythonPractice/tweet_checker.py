#Ask user to enter a tweet
tweet = input("Enter your tweet:")
#check length of tweet
tweet_length = len(tweet)
#if tweet is over 140 characters subtract overage
over_length = len(tweet) - 140
#if tweet is less than or equal to 140 chars, return this message
if tweet_length <= 140:
    print(f"That {tweet_length} char tweet will work!")
    #if tweet is over 140 chars return this message
else:
    print(f"Your {tweet_length} char tweet is {over_length} chars too long")

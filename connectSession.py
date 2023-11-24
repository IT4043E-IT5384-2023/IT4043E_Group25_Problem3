from tweety import Twitter


app = Twitter("session")
with open("account.key", "r") as f:
    username, password, key = f.read().split()
app.sign_in(username, password, extra=key)

tweets = app.search(keyword='bitcoin')
for tweet in tweets:
    print(tweet)

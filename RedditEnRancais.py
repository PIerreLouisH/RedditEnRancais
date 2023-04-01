import praw
import os

# Define user agent string with GitHub URL
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
user_agent = 'MyBot/1.0 (https://github.com/PIerreLouisH/RedditEnRancais)'

# Create a Reddit instance and authenticate with your credentials
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# Choose the subreddits we want to monitor and the corresponding French translations
subreddit_names = ['france', 'rance']
subreddit_to_french = {
'movies': 'FilmsFR',
'iwantout':'expatriation',
'food': 'BonneBouffe',
'dessert': 'BellePatisserie',
'english': 'anglais',
'algeria': 'algerie',
'personalfinance': 'vosfinances',
'addictions': 'addictionsFR',
'sexuality': 'sexualite',
'tinder': 'TinderFrance',
'mentalhealth': 'santementale',
'Needafriend': 'besoindeparler',
'parenting': 'parentingFR',
'bitcoin': 'BitcoinFrance',
'anarchism': 'anarchisme',
'jail': 'taule',
'cars': 'voitures',
'houseplants': 'jardin',
'conspiracy': 'conspiration',
'philosophy': 'philosophie',
'manga': 'mangafr',
'rpg': 'jdr',
'books': 'livres'} 
# This is a hardcoded list of English-to-French translations

# Create a subreddit instance that monitors the chosen subreddits
subreddit = reddit.subreddit('+'.join(subreddit_names))

# Look for comments containing English subreddit names and suggest French alternatives
for comment in subreddit.stream.comments(skip_existing=True):
    # Convert the comment text to lowercase for easier processing
    text = comment.body.lower()
    # Split the text into words and look for words starting with 'r/'
    for word in text.split():
        if word.startswith('r/') and len(word) > 2: # Check if the word has at least 3 characters after 'r/'
            eng_subreddit = word[2:] # Extract the subreddit name from the word
            if eng_subreddit in subreddit_to_french: # Check if the subreddit has a French alternative
                french_subreddit = subreddit_to_french[eng_subreddit] # Get the French alternative from the dictionary
                reply = f"Le subreddit r/{eng_subreddit} a un équivalent français: r/{french_subreddit}." # Construct the reply message
                comment.reply(reply) # Post the reply as a comment

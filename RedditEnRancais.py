import praw

# Define user agent string with GitHub URL
user_agent = 'MyBot/1.0 (https://github.com/PIerreLouisH/RedditEnRancais)'

# Create a Reddit instance and authenticate with your credentials
reddit = praw.Reddit(client_id=secrets['CLIENT_ID'],
                     client_secret=secrets['CLIENT_SECRET'],
                     username=secrets['USERNAME'],
                     password=secrets['PASSWORD'],
                     user_agent=user_agent)

# Choose the subreddits you want to monitor and the corresponding French translations
subreddit_names = ['france', 'rance']
subreddit_to_french = {
'food': 'alimentation', 
'movies': 'films', 
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

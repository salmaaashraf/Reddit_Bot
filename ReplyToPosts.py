import praw
import re
import os


# Create an instance of reddit bot
def CreateInstance():
    reddit = praw.Reddit(
        client_id="-bnHFU9igBLkdA",
        client_secret="dSNRNKoCIfdd-Xv-bRb4NR9wmy_yFQ",
        password="12hadeer/*",
        user_agent="RedditBot",
        username="Hadeer111")
    return reddit


# file to store the ids of posts that are replied to
def Read_ID_Post_From_File():
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        # Read the file into a list and remove any empty values
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))
    return posts_replied_to


def Reply_To_Posts(reddit, posts_replied_to, To_Search_for, Reply_of_bot):
     # sentence to search for (To_Search_for)
    # reply of the bot (Reply_of_bot)
    # get the top  values from the subreddit
    subreddit = reddit.subreddit('pythonforengineers')
    for submission in subreddit.hot(limit=10):
        print(submission.title)
        if submission.id not in posts_replied_to:  # if this post in not replied to before

            # search
            if re.search(To_Search_for, submission.title, re.IGNORECASE):
                # Reply to the post
                submission.reply(Reply_of_bot)
                print("Bot replying to : ", submission.title)

                # Store the current id into our list
                posts_replied_to.append(submission.id)
    return posts_replied_to


# add the ids of posts that are replied to
def Update_File(posts_replied_to):
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")



# function to send a message to a user
def send_message(reddit, username, title, body):
    reddit.redditor(username).message(title, body)




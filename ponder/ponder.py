from app import pick_story_objects, get_context, get_style
from groqq import model_trigger

# Activate Ponder
def activate_ponder():

    story_objects = pick_story_objects()

    context = get_context()

    style = get_style()

    tweet = model_trigger(context, style, story_objects)

    # Post the tweet

    from twitter import post_tweet

    print(f"tweet created: {tweet}")

    print("Now attempting post")

    post_tweet(tweet)

    print("Post successful")




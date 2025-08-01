from .app import pick_story_objects, get_context, get_style
from .groqq import model_trigger

# Activate Ponder
def activate_ponder():
    try:
        print("Starting ponder activation...")
        
        story_objects = pick_story_objects()
        print(f"Selected: {story_objects}")

        context = get_context()
        print("Context loaded successfully")

        style = get_style()
        print("Style loaded successfully")

        tweet = model_trigger(context, style, story_objects)
        print(f"Tweet created: {tweet}")

        # Post the tweet
        from .twitter import post_tweet

        print("Now attempting post...")
        post_tweet(tweet)
        print("Post successful!")

    except Exception as e:
        print(f"Error in activate_ponder: {e}")
        raise
from flask import Flask, request, jsonify
from ponder.app import pick_story_objects, get_context, get_style
from ponder.groqq import model_trigger
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)

def run_ponder_job():
    story_objects = pick_story_objects()
    context = get_context()
    style = get_style()
    tweet = model_trigger(context, style, story_objects)

    from ponder.twitter import post_tweet
    
    print(f"tweet created: {tweet}")
    print("Now attempting post")
    post_tweet(tweet)
    print("Post successful")


@app.route('/activate_ponder', methods=['POST'])
def activate_ponder_endpoint():
    run_ponder_job()
    return jsonify({"status": "Ponder activated and tweet posted."})


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_ponder_job, 'cron', hour=0, minute=0)
    scheduler.start()
    app.run(host="0.0.0.0", port=5000)

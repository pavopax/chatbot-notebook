from flask import Flask, request
import json
import requests

app = Flask(__name__)

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
<<<<<<< HEAD
PAT = 'EAAWeiepMTPoBAJZAUI8lZAFZCNVLi0HdVFgbrFzsJ5ob3HgbIQflP1JQiziBsc9vLVV7MuyPepmygfajT7GYdQxPdLRhcPdYlKmCCuWC2WcPXGL2zKrJXqdhBs35TEpoGYj2upMCtxgvh4vmzhcyRYdnuIHpaFl9XZADNuN1UgZDZD'
=======
PAT = ''
>>>>>>> a7bb670f4afc7d71ceba9218a5efcfa9304261f9

@app.route('/', methods=['GET'])
def handle_verification():
    print "Handling Verification."
    if request.args.get('hub.verify_token', '') == 'my_voice_is_my_password_verify_me':
        print "Verification successful!"
        return request.args.get('hub.challenge', '')
    else:
        print "Verification failed!"
        return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
    print "Handling Messages"
    payload = request.get_data()
    print payload
    for sender, message in messaging_events(payload):
        print "Incoming from %s: %s" % (sender, message)
        send_message(PAT, sender, message)
    return "ok"

<<<<<<< HEAD
@app.route('/page')
def main():
    return render_template('index.html')

=======
>>>>>>> a7bb670f4afc7d71ceba9218a5efcfa9304261f9
def messaging_events(payload):
    """Generate tuples of (sender_id, message_text) from the
    provided payload.
    """
    data = json.loads(payload)
    messaging_events = data["entry"][0]["messaging"]
    for event in messaging_events:
        if "message" in event and "text" in event["message"]:
            yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
        else:
<<<<<<< HEAD
            yield event["sender"]["id"], "Hmm, I can't echo this :("
=======
            yield event["sender"]["id"], "I can't echo this"
>>>>>>> a7bb670f4afc7d71ceba9218a5efcfa9304261f9


def send_message(token, recipient, text):
    """Send the message text to recipient with id recipient.
    """

    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params={"access_token": token},
                      data=json.dumps({
                          "recipient": {"id": recipient},
                          "message": {"text": text.decode('unicode_escape')}
                      }),
                      headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text

if __name__ == '__main__':
    app.run()

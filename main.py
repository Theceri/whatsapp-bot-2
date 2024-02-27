from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # fetch data from callback url
    incoming_message=request.get_json()
    print(incoming_message)
    
    return "this is doable"
from flask import Flask,request,jsonify
app=Flask(__name__)

@app.route('/')
def home():
    return"Server is running Send POST request to /n8n -wwebhook"

@app.route('/n8n -webhook',methods=['POST'])
def n8n_webhook():
    data = request.get_json()
    print("Received from n8n: ",data)
    return jsonify ({"status":"recevied","data":data})

if __name__=='__main__':
    app.run(debug=True,port=5000)
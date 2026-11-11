from flask import Flask ,jsonify
app=Flask (__name__)
users=[
    {"id":1, "name":"Alice","email":"alice@gmail.com"},
    {"id":2, "name":"Bob","email":"bob@gmail.com"},
    {"id":3, "name":"Charile","email":"charile@gmail.com"},
    {"id":4, "name":"Diana","email":"diana@gmail.com"},
    {"id":1, "name":"Eve","email":"eve@gmail.com"}
]
@app.route('/users',methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    user=next((u for u in users if u ['id']==user_id),None)
    if user:
        return jsonify(user)
    return jsonify({"error":"user not found"}),404

if __name__=="__main__":
    app.run(debug=True)
        
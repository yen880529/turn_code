from flask import Flask, render_template, request

app = Flask(__name__)

users = []

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        users.append({"username": username, "email": email})
        return "註冊成功！"
    return '''
    <form method="post">
        使用者名稱: <input type="text" name="username"><br>
        Email: <input type="email" name="email"><br>
        <input type="submit" value="註冊">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

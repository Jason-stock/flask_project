from flask import Flask
app = Flask(__name__) # 建立application物件

# 建立路徑 \ 對應的處理函式
@app.route("/")
def index():  # 用來回應網站首頁連線的函式
    return "Hello flask"  # 回傳網站的內容

@app.route("/data")
def hendleData():  # 用來回應網站首頁連線的函式
    return "My Data"  # 回傳網站的內容

# 建立動態路由: / 建立路徑 /user/name 對應的處理函式
@app.route("/user/<name>")
def getUser(name):
    if name == 'jason':
        return "你好 "+name
    else:
        return "hello "+name

# 啟動伺服器
app.run(debug=True, port=3000)


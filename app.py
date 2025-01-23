from flask import Flask
from flask import request
import json
from flask import redirect
# 建立application物件，可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="static", # 靜態檔案的資料夾名稱
    static_url_path="/" # 靜態檔案對應的網址路徑
) 

# 建立路徑 /getSum 對應的處理函式
# 利用要求字串 (Query String) 提供彈性 /getSum?min=最小數字&max=最大數字
@app.route("/getSum")
def getSum():
    maxNumber = request.args.get("max", 100)
    maxNumber = int(maxNumber)
    minNumber = request.args.get("min", 1)
    minNumber = int(minNumber)
    result = 0
    for i in range(minNumber,maxNumber+1):
        result += i
    return "結果 : "+str(result)


# 建立路徑 \ 對應的處理函式
@app.route("/")
def index():# 用來回應網站首頁連線的函式

    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址" ,request.url)
    # print("瀏覽器和作業系統", request.headers.get("user-agent"))
    # print("語言偏好", request.headers.get("accept-language"))
    # print("引薦網址", request.headers.get("referrer"))

    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")
    else:
        return redirect("/zh/")

@app.route("/en/")
def index_english():
    return json.dumps({
            "status":"ok",
            "text":"Hello flask"
    })

@app.route("/zh/")
def index_chinese():
    return json.dumps({
            "status":"ok",
            "text":"你好 flask"
    }, ensure_ascii=False)

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


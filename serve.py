from flask import Flask,render_template,request,redirect,url_for
import time,random
from models import jfc,quote


app = Flask(__name__)

#主页
@app.route("/",methods=["POST","GET"])
def mian():
    #名言
    nums = quote.number()
    quotes = quote.quotes(nums)

    return render_template("/page/main.html",quotes=quotes)
    

#联系
@app.route("/contact")
def contact():
    return render_template("/page/contact.html")


#反馈
@app.route("/feedback",methods=["POST","GET"])
def feedback():

    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

    if request.method == "POST":
        text = request.form["text"]
        
        with open("data_lib/feedback.txt","a") as f:
            f.write(f"{localtime}\n{text}\n\n")

        return render_template("/page/feedback.html")
    else:
        return render_template("/page/feedback.html")


#关于
@app.route("/about")
def about():
    return render_template("/page/about.html")


#登录
@app.route("/login",methods=['POST','GET'])
def login():
    #名言
    nums = quote.number()
    quotes = quote.quotes(nums)
    #登录
    if request.method == "POST":
        
        user = request.form['user']
        password = request.form['password']
        
        with open(r"E:\work\project\website\data_lib\user.txt","r",) as f:            
            user_s = f.read()

        if user in user_s and password in user_s:
            return render_template("/page/main.html",user=user,quotes=quotes)

        else:
            return render_template("/errors/error.html",massage="账号或密码错误",url="/login")
    else:
        return render_template("/page/login.html")


#解方程组
@app.route("/solution",methods=['POST','GET'])
def solution():
    
    if request.method == "POST":
        fc1 = request.form["fc1"]
        fc2 = request.form["fc2"]
        results = jfc.jfc(fc1,fc2)

        return render_template("/page/solution.html",results = results)
    else:
        return render_template("/page/solution.html")


#文章
@app .route("/article")
def article():
    return render_template("/page/article.html")


#注册
@app.route("/sign_up",methods=["POST","GET"])
def sign_up():

    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(r"E:\work\project\website\data_lib\user.txt",'r') as f:
        a = f.read()

    if request.method == "POST":
        username = request.form["username"]
        pw = request.form['pw']
        pws = request.form['pws']
        if username in a:
            return render_template('/errors/error.html',massage="该用户名已注册",url="/sign_up")
        elif pw != pws:
            return render_template('/errors/error.html',massage="两次输入的密码不一致",url="/sign_up")
        else:
            with open(r"E:\work\project\website\data_lib\user.txt",'a') as f:
                f.write(f"{localtime}\n{username}\n{pw}\n\n")

            return redirect(url_for('login'))
    else:
        return render_template("/page/sign_up.html")



if __name__ == "__main__":
    app.run(debug="True")

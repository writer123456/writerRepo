from flask import Flask,request
app=Flask(__name__)
@app.route('/add',methods=['GET','POST'])
def add():
    num1=int(request.args.get('num1'))
    num2=int(request.args.get('num2'))
    return str(num1+num2)
@app.route('/subtract',methods=['GET','POST'])
def subtract():
    num1=int(requesst.args.get('num1'))
    num2=int(request.args.get('num2'))
    return str(num1-num2)
@app.route('/multiply',methods=['GET','POST'])
def multiply():
    num1=int(request.args.get('num1'))
    num2=int(request.args.get('num2'))
    return str(num1*num2)
@app.route('/divide',methods=['GET','POST'])
def divide():
    num1=int(request.args.get('num1'))
    num2=int(request.args.get('num2'))
    return str(num1/num2)
if __name__ == "__main__":
    app.run(debug=True)

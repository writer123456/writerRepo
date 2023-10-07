from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def HelloWorld():
    student=[{'name':'prashant',
                'age':52},
                {'name':'Prajwal',
                'age':36}
                ]
    for i in range(0,len(student),1):
        if request.args.get('name')==student[i]['name']:
            print(student[i]['name'])
            return student[i]['name']


if __name__ == "__main__":
    app.run(debug=True)
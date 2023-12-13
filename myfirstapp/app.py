from flask import Flask, render_template
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index1.html')
def index1():
    api_url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=17'
    response = requests.get(api_url)   
    data1 = response.json()
    return render_template('index1.html', data=data1)

@app.route('/index2.html')
def index2():
    api_url2 = 'http://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=6'
    response2 = requests.get(api_url2)   
    data2 = response2.json()
    return render_template('index2.html', data=data2)

@app.route('/index3.html')
def index3():
    api_url3 = 'http://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=3'
    response3 = requests.get(api_url3)   
    data3 = response3.json()
    return render_template('index3.html', data=data3)

@app.route('/index4.html')
def index4():
    api_url4 = 'http://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2'
    response4 = requests.get(api_url4)   
    data4 = response4.json()
    return render_template('index4.html', data=data4)

@app.route('/index5.html')
def index5():
    api_url5 = 'http://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=8'
    response5 = requests.get(api_url5)   
    data5 = response5.json()
    return render_template('index5.html', data=data5)

@app.route('/index6.html')
def index6():
    api_url6 = 'http://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=1'
    response6 = requests.get(api_url6)   
    data6 = response6.json()
    return render_template('index6.html', data=data6)


if __name__ == '__main__':
    app.run(debug=True)

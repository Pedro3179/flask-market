from flask import Flask, render_template


app = Flask(__name__)
#print(type(app))

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items=[
        {'id':1, 'name':'RK Royal Kludge R75', 'barcode': '45378905678', 'price': 450},
        {'id':2, 'name':'Masterkeys PRO M', 'barcode': '23568790653', 'price': 467},
        {'id':3, 'name':'exbom BK152-C', 'barcode': '42696531729', 'price': 100},
        {'id':4, 'name':'Mancer Shade MK2', 'barcode': '52123531729', 'price': 120}
        ]
    return render_template('market.html', items=items)
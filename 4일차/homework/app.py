from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods = ['GET'])
def read_order():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders':orders})

@app.route('/order', methods = ['POST'])
def write_order():
    receive_name = request.form['name_give']
    receive_qty = request.form['qty_give']
    receive_address = request.form['address_give']
    receive_phone = request.form['phone_give']

    order = {
    'name' : receive_name,
    'qty' : receive_qty,
    'address' : receive_address,
    'phone' : receive_phone
    }
    db.orders.insert_one(order)

    return jsonify({'result':'success', 'msg':'주문이 완료되었습니다!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
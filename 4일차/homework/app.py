from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/orders', methods=['GET'])
def read_order():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders':orders})

@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    qty_receive = request.form['qty_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
   
    doc = {
        'name': name_receive, 
        'qty': qty_receive,
        'address': address_receive, 
        'phone': phone_receive
    }
    db.orders.insert_one(doc)

    return jsonify({'result': 'success','msg':'주문이 완료되었습니다.'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

   
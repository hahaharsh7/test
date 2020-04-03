from flask import Flask , jsonify , request , render_template
app =Flask(__name__)


#post used to recieve data 
#get used to send data back 
#reverse in browser
stores = [
     {'name':'my store' ,
    'items':[
	{'name':'my item',
	'price':100}]
      }
]

@app.route('/')
def home():
	return render_template('index.html')
# post /store data: {name}
@app.route('/store', methods =['POST'])
def create_store():
	request_data = request.get_json()
	new_store ={
	'name': request_data['name'],
	'items':[]

	}
	stores.append(new_store)
	return jsonify(new_store)
#get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
	for store in stores:
		if store['name']==name:
			return jsonify(store)
		else:
			return jsonify({'message':'store not found'})
	

#get / store
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})

@app.route('/store/<string:name>/item' ,methods=['POST'])
def create_item_in_store(name):
	for store in stores:
		if store['name']==name:
			new_item ={
			'name': request_data['name']
			'price':request_data['price']
			}
			store['items'].append(new_item)
			return jsonify(new_item)
	return jsonify({'message':'store not found'})





@app.route('/store/<string:name>/item')
def get_item_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({'items':store['items']})
		else:
			return jsonify({'message':'no items found'})


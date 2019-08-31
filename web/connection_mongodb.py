import pymongo

'''
	服务器端
	连接并操作数据库
'''

class My_db(object):
	def __init__(self):
		# 连接数据库
		mongo_client = pymongo.MongoClient('localhost', 27017)

		# 获取数据库
		db = mongo_client.my_data

		# 获取集合
		self.collection = db.my_data


	# 从数据库查询获取数据
	def query(self):	
		# 查询第一条数据
		data = self.collection.find_one()   
		
		return data	


	# 修改数据
	def update(self, temperature, humidity):
		data = self.query()   # 查询原有的数据

		# 需要修改的数据
		my_update = {
			'temperature':data["temperature"],
			'humidity':data["humidity"]
		}
		# 打算修改以后的数据
		newvalues = { 
			"$set": {
				'temperature':temperature,
				'humidity':humidity
			} 
		}

		# 开始修改
		self.collection.update_one(my_update, newvalues)
		

if __name__ == '__main__':
	a = My_db()

	d = a.query()
	
	print(d)


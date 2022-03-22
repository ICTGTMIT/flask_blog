from app import app #从app包中导入 app这个实例

#2个路由
@app.route('/')
@app.route('/index') # 无论输入"/"or"/index",都定向到index()
#1个视图函数
def index():
	return "Hello,World,zjs!"#返回一个字符串


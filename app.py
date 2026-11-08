from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def home():
    return "hello world" # 这里换成您自己的业务逻辑
if __name__ == '__main__':
    # 重点：必须要读环境变量的端口，不能写死 9000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
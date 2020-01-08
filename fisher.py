from flask import Flask

from helper import is_isbn_or_key

app = Flask(__name__)
# 这种配置方式要求文件中的常量名称全部大写
app.config.from_object('config')


# @app.route('/hello')
# def hello():
#     # 还有基于类的视图 （即插视图）
#     # return 'Hello World'
#     headers = {
#         'content-type': 'text/plain'
#     }
#     # response = make_response('<html><html/>', 404)
#     # response.headers = headers
#     # return response
#     return '<html></html', 404, headers

# app.add_url_rule('/hello', view_func=hello)


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字或者isbn
    :param page: 分页
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)

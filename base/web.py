# coding=utf-8
import json
import web

urls = (
    '/', 'index'
)

class index:
    def POST(self):
        data = web.data()
        print json.dumps(data)


if __name__ == "__main__":
    web.config.session_parameters['timeout'] = 86400
    app = web.application(urls, globals())
    app.run()
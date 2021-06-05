from wsgiref.simple_server import make_server

HTML = """ <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
  Esta es una prueba regresando HTML   
</body>
</html>
"""

def application(env, start_response):
    headers = [("Content-Type","text/html")]
    start_response("200 OK", headers)
    return [bytes(HTML, 'utf-8')]

server = make_server('localhost',8000, application)
server.serve_forever()

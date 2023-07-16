import os


def run():
    if os.path.exists('/home/kamachi/Development/fumiko/web/app.py'):
        os.remove('/home/kamachi/Development/fumiko/web/app.py')

    app = open('/home/kamachi/Development/fumiko/web/app.py', 'x')

    app.write("""from flask import Flask
    
app = Flask(__name__)\n
    """)

    sites = os.listdir('/home/kamachi/Development/fumiko/web/sites')

    for file in sites:
        if file == 'index.html':
            route = '/'
        else:
            route = f'/{file.removesuffix(".html")}'

        code = f"""
@app.route("{route}")
def {file.removesuffix(".html")}():
\tsite = open("/home/kamachi/Development/fumiko/web/sites/{file}")
\treturn site.read()"""

        app.write(f'{code}\n\n')

    app.write("\napp.run(host='0.0.0.0', port=5000)\n")

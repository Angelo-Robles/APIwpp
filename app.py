from flask import Flask,render_template

app = Flask("Website")

@app.route("/")
def hello():

    from heyoo import WhatsApp
    #TOKEN DE ACCESO DE FACEBOOK
    token='EAAEoBqTRXZC8BO5EcK2qw91CYm90CDxOkkZAZCIsmewYwCzU8sXDV22hgQ0YojLoiZAvFTZBxwz1YBOnZA2iAaTq975uCVqVveMuDn4vumJAimkwlfQSharPapRxSi5JJZCEF7wZAWIqAoZATT5mn6x5QOziZCXZCW8Fb7Cko4yy6uLpXjylYZBWrgDeouBjZBsZBuUButeqZCxWgN1Aztoq2VWfC4ZD'
    #IDENTIFICADOR DE NÚMERO DE TELÉFONO
    idNumeroTeléfono='137997732719392'
    #TELEFONO QUE RECIBE (EL DE NOSOTROS QUE DIMOS DE ALTA)
    telefonoEnvia='51990233650'

    messenger = WhatsApp(token,  phone_number_id=idNumeroTeléfono)
    messenger.send_message('hello_world', telefonoEnvia)

    return "ÉXITO"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port = '5000')
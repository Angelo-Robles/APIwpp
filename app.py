from flask import Flask,render_template

app = Flask("Website")

@app.route("/")
def hello():

    from heyoo import WhatsApp
    #TOKEN DE ACCESO DE FACEBOOK
    token='EAAERNqRPsO4BO1cvVFlKqb9xtcbNvwrFgYeZABgUIXlm4XsQ6dZBjaWxUWB1RwBshxflhBdsNWxpf8pxE97S04UYpcJ80j35ZAxSwltcz0GX7i6yYZCT05EdBoq68Gi2D4nes3qiF2VYZBMZBe13zZBV5oBAI4hKzZCfWjclxBxa89OmHzguTaYuZAjFGhwmNN5ybRn0pqOwjKlBhzPAWbsQZD'
    #IDENTIFICADOR DE NÚMERO DE TELÉFONO
    idNumeroTeléfono='137997732719392'
    #TELEFONO QUE RECIBE (EL DE NOSOTROS QUE DIMOS DE ALTA)
    telefonoEnvia='51990233650'

    messenger = WhatsApp(token,  phone_number_id=idNumeroTeléfono)
    messenger.send_message('hello_world', telefonoEnvia)

    return "ÉXITO"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port = '5000')

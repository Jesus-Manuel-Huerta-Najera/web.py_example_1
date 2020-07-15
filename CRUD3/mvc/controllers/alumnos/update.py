import web

render = web.template.render("mvc/views/alumnos/")

class Update():

    def GET(self):
        try:
            return render.update() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            forms = web.input()
            print(forms)
            return "Revisa la consola"
        except Exception as e:
            return "Error"+ str(e.args)
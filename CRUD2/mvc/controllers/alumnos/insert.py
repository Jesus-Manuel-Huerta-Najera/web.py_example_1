import web

render = web.template.render("mvc/views/alumnos/")

class Insert():

    def GET(self):
        try:
            return render.insert() # renderizando Log.html
        except Exception as e:
            return "Error " + str(e.args)
    def POST(self):
        try:
            form = web.input()
            print(form)
            print(form.Matricula)
            return "Revisa la consola"
        except Exception as e:
            return "Error"+ str(e.args)
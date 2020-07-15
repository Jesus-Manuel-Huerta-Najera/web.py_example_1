import web

render = web.template.render("mvc/views/alumnos/")

class Index():

    def GET(self):
        try:
            return render.index() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)

import web
import mvc.model.personas as personas
render = web.template.render("mvc/views/alumnos/")
model_alumnos = personas.Alumnos()
class List():

    def GET(self):
        try:
            result = model_alumnos.select()
            return render.list(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)
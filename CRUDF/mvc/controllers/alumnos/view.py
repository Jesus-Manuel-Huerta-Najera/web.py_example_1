import web

import mvc.model.personas as personas
render = web.template.render("mvc/views/alumnos/")
model_alumnos = personas.Alumnos()
class View():

    def GET(self,id):
        try:
            result = model_alumnos.view(id)[0]
            return render.view(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)
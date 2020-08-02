import web

import mvc.model.personas as personas
render = web.template.render("mvc/views/alumnos/")
model_alumnos = personas.Alumnos()

class Delete():

    def GET(self,id):
        try:
            result = model_alumnos.view(id)[0]
            print("ok esta bien")
            return render.delete(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)
    def POST(self,id):
        try:
            form = web.input()
            ids = form.id
            model_alumnos.delete(ids)
        except Exception as e:
            return "Error1000"+ str(e.args)
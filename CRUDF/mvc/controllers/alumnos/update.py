import web

import mvc.model.personas as personas
render = web.template.render("mvc/views/alumnos/")
model_alumnos = personas.Alumnos()
class Update():

    def GET(self,id):
        try:
            result = model_alumnos.view(id)[0]
            return render.update(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self,id):
        try:
            form = web.input()
            #print(forms)
            ids = form.id
            matricula = form.Matricula
            nombre = form.Nombre
            Ap = form.Primer_apellido
            Am = form.Segundo_apellido
            date = form.date
            gen = form.Sexo
            estado = form.Estado
            model_alumnos.update(matricula,nombre,Ap,Am,date,gen,estado,ids)
            web.seeother('/Plist')
        except Exception as e:
            return "Error"+ str(e.args)
import web
import mvc.model.personas as personas
render = web.template.render("mvc/views/alumnos/")
model_alumnos = personas.Alumnos()

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
            matricula = form.Matricula
            nombre = form.Nombre
            Ap = form.Primer_apellido
            Am = form.Segundo_apellido
            date = form.date
            gen = form.Sexo
            estado = form.Estado
            model_alumnos.insert(matricula,nombre,Ap,Am,date,gen,estado)
            return render.insert()
            #web.seeother('/personas_list')
        except Exception as e:
            return "Error"+ str(e.args)
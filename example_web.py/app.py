import web

urls = (
    '/', 'mvc.controllers.log.Formulario'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

import web

urls = (
    '/', 'mvc.controllers.alumnos.index.Index',
    '/Pdelete/(.*)', 'mvc.controllers.alumnos.delete.Delete',
    '/Pinsert', 'mvc.controllers.alumnos.insert.Insert',
    '/Plist', 'mvc.controllers.alumnos.list.List',
    '/Pupdate/(.*)', 'mvc.controllers.alumnos.update.Update',
    '/Pview/(.*)', 'mvc.controllers.alumnos.view.View',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()

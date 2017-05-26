import web
import os

CWD = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

render = web.template.render('{!s}/templates/'.format(CWD))

urls = (
  '/', 'index'
)


class index:

    def GET(self):
        fullname = 'John Doe'
        title = 'This template Title'
        items = [
            "First",
            "Second",
            "Third"
        ]
        return render.index(fullname, title, items)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

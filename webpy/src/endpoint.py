import web
import os

from web import form

CWD = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

render = web.template.render('{!s}/templates/'.format(CWD))

urls = (
  '/', 'Index'
)


class Index:

    def GET(self):
        fullname = 'people'
        title = 'This template Title'
        items = [
            "First",
            "Second",
            "Third"
        ]
        login = form.Form(
            form.Textbox('username'),
            form.Password('password'),
            form.Button('Login'),
        )
        my_form = login()
        form_html = my_form.render()
        return render.index(fullname, title, items, form_html)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

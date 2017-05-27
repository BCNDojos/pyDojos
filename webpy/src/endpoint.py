import web
import os

from web import form

CWD = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

render = web.template.render('{!s}/templates/'.format(CWD))

urls = (
  '/', 'Index',
  '/login', 'Login'
)


class Login:

    login_form = form.Form(
        form.Textbox('username', form.notnull),
        form.Password(
            'password',
            form.notnull,
            form.regexp('\d+', 'Digits only'),
            form.Validator(
                'Must be larger or equal than 8',
                lambda x: len(x) >= 8
            )
        )
    )

    def GET(self):
        my_form = self.login_form()
        return render.login(my_form)

    def POST(self):
        my_form = self.login_form()
        if not my_form.validates():
            return render.login(my_form)
        else:
            result = 'my_form.d.username and my_form.["username"].value are ' \
                     'equivalent ways of extracting the validated arguments ' \
                     'from the form.\n\n'
            result += 'Got! username: "{!s}", password: "{!s}"'.format(
                my_form['username'].value, my_form['password'].value
            )
            return result


class Index:

    def GET(self):
        fullname = 'people'
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

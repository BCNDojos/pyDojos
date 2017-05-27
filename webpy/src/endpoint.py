import base64
import re

import web
import os

from web import form

CWD = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

render = web.template.render('{!s}/templates/'.format(CWD))

urls = (
  '/', 'Index',
  '/login', 'Login',
  '/private/', 'Private',
)


class Private:

    def __init__(self):
        self._allowed = [
            ('admin', '12345678'),
            ('test', '87654321')
        ]

    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        if auth is None:
            auth_is_required = True
        else:
            auth = re.sub('^Basic ', '', auth)
            username, password = base64.decodestring(auth).split(':')
            if (username, password) in self._allowed:
                return render.private(username)
            else:
                auth_is_required = True
        if auth_is_required:
            web.header('WWW-Authenticate', 'Basic realm="Auth example"')
            web.ctx.status = '401 Unauthorized'
            return


class Login:

    def __init__(self):
        self._login_form = form.Form(
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
        my_form = self._login_form()
        return render.login(my_form)

    def POST(self):
        my_form = self._login_form()
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

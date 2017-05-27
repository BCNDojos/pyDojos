Getting started with web.py framework
=====================================

![webpy Logo](http://webpy.org/static/webpy.gif)

This session is based on several introduction proves of concept using web.py 
lightweight framework.

There are lots of python web frameworks, although web.py has some features and 
history that make it special:

* Started by [Aaron Swartz](http://www.aaronsw.com/), just a very important 
person.
* [reddit.com](http://reddit.com/) used it as it grew to become one of the top 
1000 sites and served millions of daily page views.
* It is a good way to understand what is happening during a request/response 
HTTP transaction.

Expect this session to be more practice than theory.

More information about web.py in the official website 
[http://webpy.org/](http://webpy.org/).

**web.py is native for python 2.7+ and python 3 is not supported.**

## Session key points ##

1. Installing dependencies.
2. Hello, world!
3. Temporary remote access by ngrok.
4. Templates.
    * Fail with indentation.
    * Update python file and template and check with no server restarting.
    * Template not found due to current working directory.
5. Forms.
    * Printing Form. Escaped and unescaped passed html.
    * Submit Form and get body.
    * Fields validation.
6. Basic Authentication.
    * Http authentication header.
    * Logout by Unauthorized status.
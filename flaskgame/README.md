Playing a bit with Flask
========================

![Flask Logo](http://flask.pocoo.org/static/logo/flask.svg)

Flask is a great lightweight web framework ideal to build fast and reliable web 
services and much more.

This dojo is inspired on 
[CD Ninja Gold repository](https://github.com/felisadeang/CD_ninjagold).

Also taken some parts of this 
[Flask Dojo](https://github.com/ranisalt/flask-dojo).

More information about Flask in the official website 
[http://flask.pocoo.org/](http://flask.pocoo.org/).

## Dojo Steps ##

1. Hello world!
2. Context introduction.
3. Start Fighting.
	```
	curl http://localhost:5000
	curl -XDELETE http://localhost:5000
	curl -XPOST http://localhost:5000/fight
	```
4. Do Punch.
	```
	curl -XPUT http://localhost:5000/fight
	```
5. Get current Score.
	```
	curl http://localhost:5000/fight
	```
6. End Fighting.
	```
	curl -XDELETE http://localhost:5000/fight
	```
7. URL query string to set a prefix for the Score response.
	```
	curl http://localhost:5000/fight?score_prefix=Damage%20is%3A%20
	```
7. Post fields to set a multiplier of doing punches
	```
    curl -XPUT --data "multiplier=2" http://localhost:5000/fight
	```
8. Post fields as JSON
	```
    curl -XPUT --header "Content-Type:application/json" --data "{\"multiplier\": 2, \"whining_choices\": [\"AAArg...\", \"Uaala\"]}" http://localhost:5000/fight
	```
n. Template, Upload file, Authorization, encoding,...
n. Fighting automation.

## HTTP Punch ##
 
The approach for this dojo is a game based practice and we are going to learn
some basic features of Flask in an entertaining way. The principles and rules
for this game below:

* Developer = Player.
* Limit of punches for each fight = 25.
* Minimum Damage starts at 0 and Maximum Damage is at 100.
* Third party Damage is a random result value returned in responses, and is not 
  cumulative.
* The result for each HTTP request is a random number between Minimum Damage and
  Maximum Damage range.
* Each punch updates the Minimum Damage value with a random result.
* HTTP Request = Playing turn.
* HTTP POST Endpoint Request = Start fighting. 201 Created status code.
* HTTP PUT Endpoint Request = Do punch on started fight. 204 No Content status 
  code.
* HTTP GET Endpoint Request = Returns the current Minimum Range as current 
  fighting Score. 200 Success status.
* HTTP DELETE Endpoint Request = End fighting, last Score got by GET is the final 
  Score. 204 No Content status code.
  
  
### Penalties ###

* If Minimum Damage reaches Maximum Damage, the score will turn to 0, and there 
  is no chance to increase anymore.
* If number of done punches exceeds the punches limit, the score will turn to 0, 
  and there is no chance to increase anymore.
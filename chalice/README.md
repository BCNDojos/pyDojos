Chalice Dojo
============

1. Create IAM Role with policies AmazonAPIGatewayAdministrator and
   AWSLambdaFullAccess.
2. Add role settings to chalice configuration file ".chalice/config.json" as
   follows:
```
...
"manage_iam_role":false,
"iam_role_arn":"arn:aws:iam::018128475095:role/tank-dev"
...
```
3. Configure AWS credentials key/secret:
```
$ mkdir ~/.aws
$ cat >> ~/.aws/config
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=YOUR_REGION (such as us-west-2, us-west-1, etc)
```
4. Install chalice and create new project, "hello world" by default.
```
$ pip install chalice
$ chalice new-project tank && cd tank
```
5. Deploy "hello world". Manually check (Commit #1).
```
$ chalice deploy
```
6. Random tank commander. Manually check.
7. Manually check as follows:
```
curl -XPOST https://o3pl7kr1sd.execute-api.eu-central-1.amazonaws.com/api/command
```
8. Check testing the tank API and fix with Cross-Origin Resource Sharing
   (https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (Commit #2).
9. Adding requirements. Add required packages into
   "tank/requirements.txt" as follows (Commit #3):
```
pytz==2017.3
```
10. Be creative and get lucky in the Dojo's Tank Wars League!!

## Tank Wars ##

* API Docs: https://tankwars.serverless.camp/pages/api.html.
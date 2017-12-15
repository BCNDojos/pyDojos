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
5. Deploy "hello world" (Commit #1).
```
$ chalice deploy
```


## Tank Wars ##

* API Docs: https://tankwars.serverless.camp/pages/api.html.
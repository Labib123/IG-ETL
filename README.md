# Instagram Comments ETL  

The aim of this project is to provide a simple ETL that will extract Instagram comments data from Phantombuster, transform it and move to Amazon S3 Data Lake 

To start using this ETL: 

## 1 - Add AWS Local Configuration 

```bash
~/.aws/credentials

[default] 
aws_access_key_id=
aws_secret_access_key=
```
```bash
~/.aws/config

[default] 
region=us-west-2
output=json
```


## 2 - Install AWS SAM CLI 


* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)


## 3 - Start building and deploying  



```
sam build --config-env ci 
sam deploy 
sam local invoke InfdbInstagramCommentsWebhook --event events/event.json

```


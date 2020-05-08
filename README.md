# A knative based bridge to mimic AWS Eventbridge

This is based on knative. It consumes messages from SQS and send them to Lambda.

Note that this could be a different cloud event source going to a totally different target ...

* An event source using an object `ContainerSource`
* A trigger object `Trigger` which defines the equivalent of a rule 
* A service object `service` which defines the target

## Store your AWS credentials in a `credentials` text file

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

## Create the secret that stores your `credentials` file

```
kubectl create secret generic awscredsfile --from-file credentials --dry-run -o yaml > awscreds-file.yaml
```

## Create all objects

After editing all objects to reflect your own setup (e.g queue name)

```
kubectl apply -f ksvc.yaml
kubectl apply -f trigger.yaml
kubectl apply -f sqs-source.yaml
```

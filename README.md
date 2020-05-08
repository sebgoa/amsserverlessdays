# A knative based bridge to mimic AWS Eventbridge

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

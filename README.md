# Red-Team-Resources

### Cloud Enum
Multi-cloud OSINT tool. Enumerate public resources in AWS, Azure, and Google Cloud.
```
https://github.com/initstring/cloud_enum
```
### AWS S3 Google Dork
```
site:s3.amazonaws.com | site:amazonaws.com "Target_Organization"
site:amazonaws.com company
site:"s3-external-1.amazonaws.com" and intext:CONFIDENTIAL
site:"s3-external-1.amazonaws.com" and intext:TOP SECRET
site:"s3.amazonaws.com" and intext:CONFIDENTIAL
site:"s3.dualstack.us-east-1.amazonaws.com" and intext:CONFIDENTIAL
site:"s3.amazonaws.com" and intext:"tlp:red"
site:"s3.amazonaws.com" and intext:"tlp:amber"
site:s3.amazonaws.com and example
site:s3.amazonaws.com and example.com
site:s3.amazonaws.com filetype:xls password
site:http://s3.amazonaws.com intitle:index of bucket
s3 site:amazonaws.com filetype:log
site:http://trello.com "aws.amazon.com" "password"
```

### Other Google Dorks
```
# Azure Blob
site:http://blob.core.windows.net and "Target_Organization"
site:http://blob.core.windows.net "targetdomain.com"

# GoogleApis
site:https://googleapis.com "Target_Organization"
```
## Other Online Resources
1. https://mr-koanti.github.io/github
2. https://mr-koanti.github.io/shodan
3. https://dorks.faisalahmed.me/

### Lists of IP ranges from: Google (Cloud & GoogleBot), Bing (Bingbot), Amazon (AWS), Microsoft (Azure), Oracle (Cloud) and DigitalOcean. Updated every 6 hours.
```
https://kaeferjaeger.gay/?dir=ip-ranges/
```
### IP Behind WAF: See the real IP of websites that have been protected by CloudFlare.
```
https://github.com/zidansec/CloudPeler
```

### Passive URL Recon
```
https://web.archive.org/web/*/archive.org*

https://web.archive.org/cdx/search/cdx?url=archive.org&matchType=domain&fl=original&collapse=urlkey&fastLatest=true
https://web.archive.org/cdx/search/cdx?url=archive.org&output=json
Tools - Use gau
```

### SSL/TLS Enumeration
```
cat ipv4_merged.txt | tlsx -json -silent -o certdb.json
cat certdb.json | jq -c 'select(.probe_status) | { "ip": .ip, "port": .port, "organization_name": .issuer_org[0], "common_name": .subject_cn, "san": .subject_an[] }' 2>/dev/null 1> certdb.json
```

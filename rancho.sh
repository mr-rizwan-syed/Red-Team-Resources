#!/bin/bash
# rancho.sh - v1
# Realtime TLD Domain Mapper with CloudRecon SSL CERT Json file
# cat urls.txt | nuclei | ./rancho.sh | notify
# Prereq - jq, python3, tr
# File required tldextractor.py file
# https://gist.githubusercontent.com/mr-rizwan-syed/8933e5183fd8313d24cf854f8a4e9fcd/raw/e02f6bface3485cd5f449a9d6b43e48f4e09a0a7/tldextractor.py

SSLCERTDB="ssl-cert-1008202411PM.json"

# Function to extract IP address from input URL
extract_ip() {
    nucleiout="$1"
    ip=$(echo "$nucleiout" | cut -d ' ' -f4 | cut -d '/' -f3)
    echo "$ip"
}

while read -r line; do
    # Extracting IP address
    ip=$(extract_ip "$line")

    # Check if IP is found in the JSON file
    if rg -q "$ip" $SSLCERTDB; then
        tlsx1=$(echo $ip | tlsx -cn -silent -ro)
        httpx1=$(echo $ip | httpx -title -fr -silent| grep -oP '\[\K[^\]]+')
        # Extracting commonNames if IP is found
        commonNames=$(grep "$ip" $SSLCERTDB | jq -r '.commonName' | python3 tldextractor.py)

        # Constructing the output format
        output="$line - [$(echo "$commonNames" | tr '\n' ', ' | sed 's/,$//')] $tlsx1 $httpx1"

        # Echo input and result on the same line
        echo "$output"
    fi
done

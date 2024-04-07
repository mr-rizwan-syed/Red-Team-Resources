#!/bin/bash
# rancho.sh - v1
# Realtime TLD Domain Mapper with CloudRecon SSL CERT Json file
# cat urls.txt | nuclei | ./rancho.sh | notify
# Prereq - jq, python3, tr
# File required tldextractor.py file

SSLCERTDB="05042024-ssl-cert.json"

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
    if grep -q "$ip" $SSLCERTDB; then
        # Extracting commonNames if IP is found
        commonNames=$(grep "$ip" $SSLCERTDB | jq -r '.commonName' | python3 tldextractor.py)

        # Constructing the output format
        output="$line - [$(echo "$commonNames" | tr '\n' ', ' | sed 's/,$//')]"

        # Echo input and result on the same line
        echo "$output"
    fi
done 

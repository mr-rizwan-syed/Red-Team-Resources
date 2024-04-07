import sys
import tldextract

def is_valid_domain(domain):
    # Check if the domain contains only alphanumeric characters and hyphens
    if not domain.replace('-', '').replace('.', '').isalnum():
        return False
    
    # Check if the domain doesn't end with a period
    if domain.endswith('.'):
        return False
    
    return True

def extract_apex_domains_from_input(input_data):
    subdomains = input_data.splitlines()

    apex_domains = set()

    for subdomain in subdomains:
        # Use tldextract to extract the domain information
        domain_info = tldextract.extract(subdomain)

        # Construct the apex domain
        apex_domain = f"{domain_info.domain}.{domain_info.suffix}"

        # Check if the apex domain is valid
        if is_valid_domain(apex_domain):
            # Add to the set to ensure uniqueness
            apex_domains.add(apex_domain)

    return list(apex_domains)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r') as file:
                input_data = file.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
    elif len(sys.argv) == 1:
        # Read from stdin
        input_data = sys.stdin.read()
    else:
        print("Usage: python script.py [<subdomains_file>]")
        sys.exit(1)

    apex_domains = extract_apex_domains_from_input(input_data)

    if apex_domains:
        for apex_domain in apex_domains:
            print(apex_domain)
    else:
        print("No valid apex domains found.")

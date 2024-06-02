import sys
import tldextract

def extract_apex_domains(subdomains):
    apex_domains = set()

    for subdomain in subdomains:
        # Use tldextract to extract the domain information
        domain_info = tldextract.extract(subdomain)

        # Construct the apex domain
        apex_domain = f"{domain_info.domain}.{domain_info.suffix}"

        # Add to the set to ensure uniqueness
        apex_domains.add(apex_domain)

    return list(apex_domains)

def extract_apex_domains_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            subdomains = [line.strip() for line in file.readlines()]
        return extract_apex_domains(subdomains)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def extract_apex_domains_from_stdin():
    subdomains = [line.strip() for line in sys.stdin.readlines()]
    return extract_apex_domains(subdomains)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: python script.py [<subdomains_file>]")
        sys.exit(1)

    if len(sys.argv) == 2:
        subdomains_file = sys.argv[1]
        apex_domains = extract_apex_domains_from_file(subdomains_file)
    else:
        apex_domains = extract_apex_domains_from_stdin()

    print("Apex Domains:")
    for apex_domain in apex_domains:
        print(apex_domain)

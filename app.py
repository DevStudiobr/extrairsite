import requests
from bs4 import BeautifulSoup
import whois

def get_http_headers(url):
    try:
        response = requests.get(url)
        return response.headers
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar o site: {e}"

def get_site_metadata(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        metadata = {meta.get('name'): meta.get('content') for meta in soup.find_all('meta') if meta.get('name')}
        return metadata
    except Exception as e:
        return f"Erro ao coletar metadados: {e}"

def get_whois_data(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"Erro ao consultar WHOIS: {e}"

# Exemplo de uso
site_url = input("Digite o URL do site: ")
domain = site_url.replace("http://", "").replace("https://", "").split('/')[0]

# Coletando headers HTTP
print("\n=== Headers HTTP ===")
headers = get_http_headers(site_url)
for header, value in headers.items():
    print(f"{header}: {value}")

# Coletando metadados
print("\n=== Metadados do site ===")
metadata = get_site_metadata(site_url)
for meta, content in metadata.items():
    print(f"{meta}: {content}")

# Coletando informações WHOIS
print("\n=== Informações WHOIS ===")
whois_info = get_whois_data(domain)
print(whois_info)

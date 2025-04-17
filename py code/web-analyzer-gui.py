import tkinter as tk
from tkinter import ttk, scrolledtext
import socket
import ssl
import requests
from urllib.parse import urlparse
import dns.resolver
import whois
from datetime import datetime

class WebAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Analyzer by Omiya")
        self.root.geometry("800x600")
        
        # Add title label
        title_label = tk.Label(root, text="Web Analyzer by Omiya", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        
        # Create input frame
        input_frame = ttk.Frame(root)
        input_frame.pack(pady=10, padx=10, fill='x')
        
        # URL input
        ttk.Label(input_frame, text="Enter Website URL:").pack(side='left')
        self.url_entry = ttk.Entry(input_frame, width=50)
        self.url_entry.pack(side='left', padx=5)
        
        # Analyze button
        self.analyze_button = ttk.Button(input_frame, text="Analyze", command=self.analyze)
        self.analyze_button.pack(side='left', padx=5)
        
        # Results area
        self.results_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=30)
        self.results_area.pack(pady=10, padx=10, fill='both', expand=True)

    def analyze_website(self, url):
        """
        Analyze publicly available technical information about a website
        """
        results = {
            "basic_info": {},
            "dns_info": {},
            "ssl_info": {},
            "headers": {}
        }
        
        # Clean and parse the URL
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        
        # Basic information
        try:
            ip = socket.gethostbyname(domain)
            results["basic_info"]["ip"] = ip
            results["basic_info"]["hostname"] = domain
        except socket.gaierror as e:
            results["basic_info"]["error"] = f"Could not resolve hostname: {str(e)}"
        
        # DNS Information
        try:
            for qtype in ['A', 'MX', 'NS', 'TXT']:
                answers = dns.resolver.resolve(domain, qtype)
                results["dns_info"][qtype] = [str(rdata) for rdata in answers]
        except Exception as e:
            results["dns_info"]["error"] = f"DNS lookup failed: {str(e)}"
        
        # SSL Certificate Information
        try:
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=domain) as sock:
                sock.connect((domain, 443))
                cert = sock.getpeercert()
                
                results["ssl_info"]["issuer"] = dict(x[0] for x in cert['issuer'])
                results["ssl_info"]["subject"] = dict(x[0] for x in cert['subject'])
                results["ssl_info"]["valid_from"] = cert['notBefore']
                results["ssl_info"]["valid_until"] = cert['notAfter']
        except Exception as e:
            results["ssl_info"]["error"] = f"SSL certificate check failed: {str(e)}"
        
        # HTTP Headers
        try:
            response = requests.get(url, timeout=10)
            results["headers"] = dict(response.headers)
        except Exception as e:
            results["headers"]["error"] = f"Could not fetch headers: {str(e)}"
        
        return results

    def format_results(self, results):
        output = "=== Web Analyzer by Omiya - Analysis Results ===\n\n"
        
        output += "Basic Information:\n"
        for key, value in results["basic_info"].items():
            output += f"  {key}: {value}\n"
        
        output += "\nDNS Information:\n"
        for record_type, records in results["dns_info"].items():
            if isinstance(records, list):
                output += f"  {record_type} Records:\n"
                for record in records:
                    output += f"    {record}\n"
            else:
                output += f"  {record_type}: {records}\n"
        
        output += "\nSSL Certificate Information:\n"
        for key, value in results["ssl_info"].items():
            output += f"  {key}: {value}\n"
        
        output += "\nHTTP Headers:\n"
        for header, value in results["headers"].items():
            output += f"  {header}: {value}\n"
            
        return output

    def analyze(self):
        self.results_area.delete(1.0, tk.END)
        self.results_area.insert(tk.END, "Analyzing... Please wait...\n")
        self.root.update()
        
        url = self.url_entry.get()
        results = self.analyze_website(url)
        formatted_results = self.format_results(results)
        
        self.results_area.delete(1.0, tk.END)
        self.results_area.insert(tk.END, formatted_results)

if __name__ == "__main__":
    root = tk.Tk()
    app = WebAnalyzerGUI(root)
    root.mainloop()

# Simple Web Analyzer By SL oomiBoy

![Interface Screenshot](https://github.com/SL-oomiBoy/Simple-Web-Analyzer/blob/main/images/Screenshot%202025-04-17%20065233.png)

**Web Analyzer by Omiya** is a simple desktop application built with Python and Tkinter that allows users to analyze publicly available technical information about websites.

## 🔍 Features

- **User-Friendly GUI**: Clean interface built with Tkinter for ease of use.
- **Basic Info Lookup**:
  - Extracts IP address and hostname of the entered domain.
- **DNS Information**:
  - Retrieves `A`, `MX`, `NS`, and `TXT` DNS records.
- **SSL Certificate Analysis**:
  - Gathers certificate issuer, subject, validity dates, and more.
- **HTTP Header Inspection**:
  - Fetches and displays response headers of the given website.
- **Scrollable Output**:
  - Displays results in a scrollable text area for convenient viewing.

## 💻 Technologies Used

- Python 3
- Tkinter
- `socket`, `ssl`, `requests`, `dns.resolver`, `whois`, `urllib`

## 📸 Screenshot

Below is the user interface of the application:

![Web Analyzer UI](https://github.com/SL-oomiBoy/Simple-Web-Analyzer/blob/main/images/Screenshot%202025-04-17%20065233.png)

---

## 🚀 Getting Started

> **Note:** Make sure the following Python packages are installed:

```bash
pip install requests dnspython python-whois
```
## To run the script:
```bash
python web_analyzer.py
```
---
## 📌 Note
This tool is intended for educational and informational purposes only.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## ✨ Developed by Omiya






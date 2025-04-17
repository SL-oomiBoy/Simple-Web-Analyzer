# Web Analyzer by Omiya

![Interface Screenshot](3d552517-616c-4d98-b50d-4805496941f8.png)

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

![Web Analyzer UI](3d552517-616c-4d98-b50d-4805496941f8.png)

---

## 🚀 Getting Started

> **Note:** Make sure the following Python packages are installed:

```bash
pip install requests dnspython python-whois

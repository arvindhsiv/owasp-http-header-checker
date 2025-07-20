**OWASP HTTP Security Header Scanner**

A Flask-based web application that scans any public website to detect the presence of important HTTP response security headers recommended by OWASP. The tool helps identify missing or misconfigured headers that are essential for web security.

---

### About the Project

This application is designed to make it easy to verify whether a website includes key HTTP response headers that protect against common security threats such as cross-site scripting (XSS), clickjacking, and data leaks.

Users can input any URL, and the app will perform a real-time HTTP request to retrieve and analyze response headers. The results are displayed in a simple, readable format showing which headers are present and which are missing.

---

### Features

* Accepts any HTTP or HTTPS URL via a web form.
* Performs an HTTP GET request and extracts response headers.
* Compares retrieved headers against a predefined OWASP-aligned list.
* Displays header status (present or missing) in a tabular format.
* Minimal and intuitive web interface built using Flask and Jinja2.
* Containerized using Docker for easy deployment.

---

### HTTP Headers Checked

* Content-Security-Policy
* Strict-Transport-Security
* X-Content-Type-Options
* X-Frame-Options
* Referrer-Policy
* Permissions-Policy
* Clear-Site-Data
* Cache-Control
* Cross-Origin-Embedder-Policy
* Cross-Origin-Opener-Policy
* Cross-Origin-Resource-Policy
* X-Permitted-Cross-Domain-Policies

---

### Getting Started

#### Prerequisites

* Docker (optional for containerized deployment)
* Python 3.9+
* pip

#### Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/arvindhsiv/owasp-http-header-checker.git
   cd owasp-http-header-checker
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

   Visit `http://localhost:5000` in your browser.

---

### Docker Deployment

1. Build the image:

   ```bash
   docker build -t owasp-header-checker .
   ```

2. Run the container:

   ```bash
   docker run -p 5000:5000 owasp-header-checker
   ```

   Visit `http://localhost:5000`

---

### Project Structure

```
.
├── app.py                  # Flask application logic
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image definition
├── templates/
│   └── index.html          # HTML template using Jinja2
```

---

### License

This project is licensed under the MIT License.

---


#HTTP Header Checker
# A simple Flask application to check HTTP headers against OWASP recommendations.
# This application allows users to input a URL and checks the HTTP headers
# against a predefined list of OWASP security headers.
# created by: [ArvindhSiva]


#import Flask: the micro web framework to handle HTTP routes and templates
#render_template: used to render HTML files (Jinja2 templates)
#request: handles incoming data (form data)
#random: used to randomly pick a word if the user doesn't give one

from flask import Flask, render_template, request
import random


# Instantiates the app
app = Flask(__name__)

# Http Security Headers
OWASP_HEADERS = [
    {"name": "Cache-Control", "expected": "no-store"},
    {"name": "Clear-Site-Data", "expected": "cache"},
    {"name": "Content-Security-Policy", "expected": "default-src"},
    {"name": "Cross-Origin-Embedder-Policy", "expected": "require-corp"},
    {"name": "Cross-Origin-Opener-Policy", "expected": "same-origin"},
    {"name": "Cross-Origin-Resource-Policy", "expected": "same-origin"},
    {"name": "Permissions-Policy", "expected": "accelerometer"},
    {"name": "Referrer-Policy", "expected": "no-referrer"},
    {"name": "Strict-Transport-Security", "expected": "max-age"},
    {"name": "X-Content-Type-Options", "expected": "nosniff"},
    {"name": "X-Frame-Options", "expected": "deny"},
    {"name": "X-Permitted-Cross-Domain-Policies", "expected": "none"}
]

#https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers - reference for HTTP headers

@app.route('/', methods=['GET', 'POST'])
def index():
    headers_result = {}
    error = None

    if request.method == 'POST':
        url = request.form['url']
        if not url.startswith('http'):
            url = 'https://' + url

        try:
            response = requests.get(url, timeout=5)
            for header in OWASP_HEADERS:
                name = header["name"]
                value = response.headers.get(name, None)
                headers_result[name] = value if value else  "Missing"
        except Exception as e:
            error = f"Could not reach {url}: {e}"

    return render_template('index.html', headers=headers_result, known_headers=OWASP_HEADERS, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

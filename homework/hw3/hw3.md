# **Homework: Web Security**

## **Part 1: Research and Analysis of DDoS Attack Techniques (Unchanged)**

**Objective:** Students will conduct in-depth research on the common methods used to execute Distributed Denial of Service (DDoS) attacks, focusing on the layers of the OSI model they target and how they operate.

* Task A: Categorization and Description  
  Research and define the three primary categories of DDoS attacks (Volumetric, Protocol, Application Layer). For each category, describe its goal and provide at least two specific attack examples. Present your findings in a comparison table.

| DDoS Category | OSI Layer(s) Targeted | Primary Goal of Attack | Specific Attack Example 1 | Specific Attack Example 2 |
| :---- | :---- | :---- | :---- | :---- |
| **Volumetric** | L3, L4 | Consume all available bandwidth | **UDP Flood** | **DNS Amplification** |
| **Protocol** | L3, L4 | Exhaust server connection state tables | **SYN Flood** | **ICMP Flood** |
| **Application Layer** | L7 | Exhaust application/server resources | **HTTP Flood** | **Slowloris** |

*   
  Task B: In-Depth Attack Profile  
  Choose one specific attack from your table (e.g., DNS Amplification) and write a detailed profile (250-350 words) that explains its Mechanism, the Resource Exhaustion it causes, and how Botnets/Amplification are used.

## **Part 2: Hands-On: DVWA Deployment and Common Attacks**

**Objective:** Students will deploy a vulnerable web application using Docker and execute common web attacks in a safe, controlled environment, learning to bypass **basic** security measures.

**⚠️ Ethical Warning:** This task is for **educational, local simulation only**. Students are **strictly forbidden** from attempting these attacks on any public, external, or third-party web resource.

* **Task A: DVWA Installation via Docker**  
  1. Ensure **Docker** is installed and running on your local machine.  
  2. Pull and run the Damn Vulnerable Web Application (DVWA) using a public Docker image (e.g., vulnerables/web-dvwa or citizenstig/dvwa). You will need to map a local port (e.g., port 80\) to the container's web server.  
     **Example Command:** docker run \--rm \-it \-p 80:80 vulnerables/web-dvwa  
  3. Access the DVWA login page at http://localhost/ (or your mapped port). Log in with the default credentials (admin/password) and complete the database setup.  
  4. **Submission:** Provide the exact Docker command(s) you used to pull and run the container, and a screenshot of the DVWA home page.  
* **Task B: Attack Execution and Documentation (Medium Security)**  
  1. Set the DVWA security level to **Medium**. This level often includes functions like mysql\_real\_escape\_string() for SQLi, or basic string replacement for XSS, requiring students to look for weaknesses like lack of case sensitivity or incomplete filtering.  
  2. Successfully execute **three** distinct common web application attacks using the DVWA menu options. Focus on vulnerabilities from the **OWASP Top 10**:  
     * **SQL Injection (SQLi)**: You may need to use **time-based blind techniques** or other bypasses since the standard UNION attack may be sanitized.  
     * **Cross-Site Scripting (XSS)**: You may need to bypass basic input filters by using different encodings, event handlers, or mixed-case tags.  
     * **Command Injection**: Look for ways to bypass filtering of commands like | or & by using other command separators (e.g., &&, ||, or \\n).  
  3. For each of the three attacks, provide:  
     * The **Vulnerability Name** (e.g., SQL Injection).  
     * The **Payload** used (the malicious input string).  
     * A **Screenshot** of the successful exploitation (e.g., the alert box for XSS, or the SQL query result for SQLi).  
     * A **brief explanation** (1-2 sentences) of *why* the attack payload needed to be modified to bypass the Medium security filter.

---

## **Part 3: Defensive Installation: Web Application Firewall (WAF)** 

**Objective:** Students will install a reverse proxy and WAF solution to understand the defensive mechanisms required to block the attacks performed in Part 2\.

* **Task A: WAF Deployment**  
  1. Research and select an **open-source Web Application Firewall (WAF)** solution that can be run as a reverse proxy, such as **ModSecurity** (often used with Nginx/Apache) or **BunkerWeb** (Docker-friendly).  
  2. Install and configure your chosen WAF to sit **in front of** the running DVWA container.  
  3. Ensure the WAF is configured with a default rule set (e.g., the **OWASP Core Rule Set (CRS)** for ModSecurity, if applicable).  
* **Task B: Defense Testing and Analysis**  
  1. Attempt to execute the **same three attack payloads** from Part 2 *through* the WAF proxy.  
  2. For each payload, document the result: Did the WAF **successfully block** the attack? What **HTTP Status Code** or **Error Message** did the WAF return?  
  3. Locate the WAF's security log and identify the **Rule ID** (if applicable) that triggered the block for at least one of the attacks.  
  4. **Submission:**  
     * The name of the WAF solution installed.  
     * A diagram or detailed explanation of your network setup (WAF $\\rightarrow$ DVWA).  
     * A screenshot of the WAF blocking one of the attack attempts.  
     * An analysis (150-200 words) of the difference between an **Application Layer attack (L7)** you performed (like SQLi) and the **DDoS Application Layer attack** researched in Part 1 (like HTTP Flood).


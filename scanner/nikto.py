# scanner/nikto.py

import subprocess
import json
from db.models import CVE, ScanResult


def run_nikto(target):
    print(f"[Nikto] Сканируем {target}...")
    try:
        output_file = "nikto_output.json"
        subprocess.run(["nikto", "-h", target, "-Format", "json", "-output", output_file], check=True)
        with open(output_file, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка при запуске Nikto: {e}")
        return {}


def process_nikto_result(data, cursor, url_id):
    vulnerabilities = data.get("vulnerabilities", [])

    for vuln in vulnerabilities:
        cve_id = vuln.get("osvdb_id") or vuln.get("id", "N/A")
        description = vuln.get("description", "")
        severity = vuln.get("severity", "Medium")

        CVE.insert(cursor, cve_id=cve_id, description=description, severity=severity)
        cve_db_id = cursor.lastrowid

        ScanResult.insert(cursor, url_id=url_id, cve_id=cve_db_id, status="Exploitable")

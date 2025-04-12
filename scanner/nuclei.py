# scanner/nuclei.py

import subprocess
import json
from db.models import CVE, ScanResult


def run_nuclei(target):
    print(f"[Nuclei] Сканируем {target}...")
    try:
        result = subprocess.run(["nuclei", "-u", target, "-json"], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().splitlines()
        return [json.loads(line) for line in lines if line.strip()]
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске Nuclei: {e}")
        return []


def process_nuclei_result(data, cursor, url_id):
    for finding in data:
        cve_id = finding.get("info", {}).get("cve", ["unknown"])[0]
        description = finding.get("info", {}).get("name", "")
        severity = finding.get("info", {}).get("severity", "Medium")

        CVE.insert(cursor, cve_id=cve_id, description=description, severity=severity)
        cve_db_id = cursor.lastrowid

        ScanResult.insert(cursor, url_id=url_id, cve_id=cve_db_id, status="Exploitable")

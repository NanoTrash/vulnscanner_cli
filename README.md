project_root/
│
├── main.py
├── scanner/
│   ├── parser.py
│   ├── wappalyzer.py
│   ├── nikto.py
│   └── nuclei.py
│
└── db/
    ├── models.py
    ├── schema.py
    └── report.py

🛠 Зависимости:
pip install -r requirements.txt
sudo apt install nikto
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
npm install -g wappalyzer

▶️ Запуск:
python main.py https://example.com --report

	•	--db scanner.db — путь к SQLite (по умолчанию создастся scanner.db)
	•	--report — выводит отчёт по завершении

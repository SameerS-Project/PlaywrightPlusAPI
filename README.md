# PlaywrightPlusAPI: UI + API Automation Framework

This project demonstrates a real-world automation setup using **Python**, **Playwright**, **Pytest**, and **Requests**. It includes both **UI** and **API** test coverage, with GitHub Actions configured for continuous integration.

---

## 🔧 Tech Stack

- **Language**: Python  
- **UI Testing**: Playwright + Pytest  
- **API Testing**: Requests + Pytest  
- **Structure**: Page Object Model (POM)  
- **CI/CD**: GitHub Actions  
- **Reports**: HTML via Pytest plugins  

---

## How to Run

### UI Tests:
```bash
pytest -m ui --html=reports/ui_report.html
API Tests:
bash
Copy
Edit
pytest -m api --html=reports/api_report.html
Markers defined in pytest.ini
Note: Some API tests are marked as skipped due to 401 Unauthorized responses from the Reqres test API.


📂 Folder Overview
bash
Copy
Edit
pages/            # Page objects (UI locators/actions)
tests/            # Test cases (UI + API)
.github/          # CI config (pytest.yml)
conftest.py       # Shared fixtures
requirements.txt  # Dependencies
🛠️ Setup
bash
Copy
Edit
pip install -r requirements.txt
playwright install

👤 Author
Sameer Siddiqui
QA Automation Engineer | Python, Playwright
GitHub
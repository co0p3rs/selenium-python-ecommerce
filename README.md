# Selenium Python Ecommerce Framework

Production-style UI automation framework for the public SauceDemo test application. The project demonstrates the same engineering patterns used in larger commercial suites without exposing employer code, selectors, accounts, or business rules.

## Coverage

- Authentication: successful, invalid, locked, missing credentials
- Inventory: rendering, sorting, product details, cart badges
- Cart: add/remove, persistence, multiple products
- Checkout: validation, totals, cancellation, completed purchase
- End-to-end purchase path
- Smoke and regression markers
- Multi-browser support through `--browser`
- Screenshots and page source on failure
- GitHub Actions matrix for Chrome and Firefox

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -m smoke --browser chrome
pytest -m regression --browser firefox
```

Windows activation:

```powershell
.venv\Scripts\Activate.ps1
```

The default target and accounts belong to SauceDemo and are intended for test automation practice.


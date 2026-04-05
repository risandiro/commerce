# Commerce

**Live demo:** _https://risandiro.pythonanywhere.com/_
**Source:** _https://github.com/risandiro/commerce_

---

Auction-style marketplace where users can post listings, place bids, manage a watchlist, and browse by category. Built as a capstone-style web app (Django + SQLite).

## Features

- User registration, login, and logout (custom user model)
- Create listings with title, description, image URL, starting bid, and category
- Active / closed listings; highest bid wins when a listing is closed
- Place bids with validation (must exceed current bid and meet minimum)
- Watchlist: add/remove listings and quick access from the nav
- Comments on listings
- Category pages and "all categories" overview
- Django admin for content management (optional)

## Tech stack

- **Python 3**
- **Django** 3.x
- **SQLite** (development)
- **HTML / CSS** (Django templates)

## Getting started

### Prerequisites

- Python 3.8.5+ recommended
- `pip`

### Setup

```bash
git clone https://github.com/risandiro/commerce.git
cd commerce
python -m venv venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

pip install "Django>=3.2,<5"
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

### Optional: admin user

```bash
python manage.py createsuperuser
```

Then visit **http://127.0.0.1:8000/admin/**.

## Project layout (high level)

```
commerce/          # project settings, urls
auctions/          # models, views, templates, static
manage.py
```

## What I learned

- Server-rendered apps with Django (URLs, views, templates, forms)
- Relational modeling (users, listings, bids, categories, watchlist, comments)
- Auth and per-user state in a web app

## License / attribution

Coursework inspired by **CS50's Web Programming with Python and JavaScript** (Harvard). This repository is my own implementation for portfolio purposes.

---

**Author:** Richard Král ([@risandiro](https://github.com/risandiro))

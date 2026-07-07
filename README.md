# Rukmini — 3D Django Portfolio

A full-stack personal portfolio site built with Django. The frontend features a
signature interactive element: three translucent "glass" panels (Database /
Backend / Frontend) arranged in real 3D space in the hero section, tilting as
you move your cursor — a literal visual of what "full-stack" means. Project
cards use the same 3D-tilt treatment on hover.

All content — profile info, skills, projects, and the timeline — is stored in
the database and editable through the Django admin, not hardcoded in the
templates.

## Features

- Fully responsive, single-page portfolio (hero, about, skills, projects, journey, contact)
- 3D CSS hero visual with mouse-parallax tilt (no JS 3D library required)
- Project cards with a subtle 3D tilt-on-hover effect
- Content-managed through Django admin:
  - `Profile` — hero text, about copy, resume file, profile photo, social links
  - `SkillCategory` + `Tag` — skill chips grouped by category
  - `Project` — title, description, screenshot, tech tags, GitHub/live links, status
  - `TimelineEntry` — "Journey" section rows
- Pre-seeded with real project content (SecureHire AI, LocalFix, Cookly) via a Django data migration — works out of the box, no manual data entry needed to see it running
- Media uploads (profile photo, project screenshots) handled through Django's `ImageField`

## Tech stack

| Layer | Tech |
|---|---|
| Backend | Django 5 |
| Database | SQLite (default) — swap to PostgreSQL by editing `DATABASES` in `settings.py` |
| Frontend | Django templates, vanilla CSS (CSS custom properties + 3D transforms), vanilla JS |
| Fonts | Fraunces (display), Inter (body), IBM Plex Mono (labels/tags) |
| Images | Pillow (for `ImageField` support) |

## Project structure

```
portfolio_site/
├── manage.py
├── requirements.txt
├── portfolio_project/        # Django project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── portfolio/                 # The single Django app
    ├── models.py               # Profile, Tag, SkillCategory, Project, TimelineEntry
    ├── admin.py                # Admin registration for all models
    ├── views.py                # Single home view, queries all content
    ├── urls.py
    ├── migrations/
    │   └── 0002_seed_data.py    # Seeds real starter content on first migrate
    ├── templates/portfolio/
    │   ├── base.html
    │   └── home.html
    └── static/portfolio/
        ├── css/style.css
        └── js/main.js
```

## Getting started

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations (this also seeds the starter content automatically)
python manage.py migrate

# 5. Create an admin login for yourself
python manage.py createsuperuser

# 6. Run the dev server
python manage.py runserver
```

Then open:
- `http://127.0.0.1:8000/` — the portfolio site
- `http://127.0.0.1:8000/admin/` — the admin panel to edit content

## Adding your real photos and screenshots

The site ships with clearly marked placeholders instead of stock content:

1. Go to `/admin/`, open **Profile**, and upload your **profile photo** and **resume file**.
2. Open each **Project**, and upload its **screenshot**.

The templates automatically swap the placeholder frames for your real images
once they're uploaded — no template editing needed.

## Editing content

Everything on the page is editable from `/admin/` — no need to touch HTML:

- **Profile** → hero headline, intro text, about section, social links, grad year, LeetCode count
- **Skill categories** → add/reorder skill groups and the tags inside them
- **Projects** → add new project cards, reorder them, change status (Live build / In progress / Archived)
- **Timeline entries** → add/reorder rows in the "Journey" section

## Deployment notes

Before deploying anywhere public:

- Set `DEBUG = False` in `portfolio_project/settings.py`
- Move `SECRET_KEY` out of `settings.py` into an environment variable
- Set `ALLOWED_HOSTS` to your real domain
- Configure a production database (PostgreSQL recommended) and static/media file serving (e.g. WhiteNoise for static files, S3/Cloudinary for media)

## Author

**Rukmini** — B.Tech CS & IT, Ajay Kumar Garg Engineering College, Ghaziabad (2023–2027)

- GitHub: [@rukmini12438](https://github.com/rukmini12438)
- LinkedIn: [rukmini-96b005287](https://www.linkedin.com/in/rukmini-96b005287)

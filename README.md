# FeedMap

**FeedMap** is a collaborative roadmap platform where users can upvote, comment, and engage with predefined feature items.

## Features
### Version-1
- User login/signup with JWT
- View roadmap items (read-only)
- Upvote items (1 vote per user)
- Comment and reply in nested threads
- Edit/delete own comments

## Tech Stack
- React.js
- Django REST Framework
- Neon PostgreSQL
- JWT Auth

## Code Documentation
See `/docs/` for architecture, code style, and API design details.

- [Code Style](docs/code-style.md)
- [System Architecture](docs/architecture.md)
- [API Spec](docs/api-spec.md)

## Getting Started
```bash
git clone https://github.com/shemanto27/feedmap.git
cd feedmap/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver

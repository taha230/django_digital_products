# Django Digital Products

A Django REST API for digital products: catalog, subscriptions, and payments. Uses a **custom user model** with **phone number** (and optional email) for authentication.


---

## Applications

| App            | Purpose |
|----------------|--------|
| **users**      | Custom user model (phone + optional email), registration, JWT auth, profiles, devices, provinces. |
| **products**   | Product catalog: categories (with optional parent), products, and files (audio/video/PDF). |
| **subscriptions** | Subscription packages (SKU, price, duration) and user subscriptions (linked to `User` and `Package`). |
| **payments**   | Payment gateways and payment records (status, user, package, gateway). |
| **utils**      | Shared validators (e.g. SKU, phone number). |

---

## Custom user model (phone number)

The project uses a **custom user** (`users.User`) instead of Django’s default. It is configured in `settings.py` as:

```python
AUTH_USER_MODEL = 'users.User'
```

### Main fields

- **username** — Required, unique. Must start with a letter; letters, numbers, `_`, `.` allowed.
- **phone_number** — Optional, unique. Iranian mobile format: `989[0-3,9]` + 8 digits (e.g. `989123456789`). Validated via `RegexValidator`.
- **email** — Optional, unique. Used for login/contact if provided.
- **first_name**, **last_name** — Optional.
- **password** — Hashed; can be omitted when creating users with `no password` (e.g. social/phone-only flows).
- **is_staff**, **is_active**, **is_superuser**, **date_joined**, **last_seen** — Standard/auth fields.

### UserManager behavior

- **create_user** — If `username` is not given, it is derived from `email` (part before `@`) or from `phone_number` (random letter + last 7 digits, made unique).
- **create_superuser** — Requires `username`, `phone_number`, `email`, `password`.
- **get_by_phone_number(phone_number)** — Lookup user by phone.

### Related models (in `users`)

- **UserProfile** — One-to-one with `User`: nick_name, avatar, birthday, gender, province (FK to `Province`).
- **Device** — Per-user devices: device_uuid, type (web/ios/android), last_login, device_os, device_model, app_version.
- **Province** — Name, is_valid; used by `UserProfile`.

---

## API endpoints

Base URL is the project root (e.g. `http://localhost:8000/`). Auth uses **JWT** (Bearer token).

### Users & auth

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/register/` | Register a new user. |
| POST   | `/users/token/` | Obtain JWT access + refresh (login). |
| POST   | `/users/token/refresh/` | Refresh access token. |

### Products (catalog)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/products/` | List products. |
| GET    | `/products/<id>/` | Product detail. |
| GET    | `/categories/` | List categories. |
| GET    | `/categories/<id>/` | Category detail. |
| GET    | `/products/<product_id>/files/` | List files of a product. |
| GET    | `/products/<product_id>/files/<id>/` | File detail. |

### Subscriptions

| Method | Endpoint | Description |
|--------|----------|-------------|
| *       | `/subs/packages/` | Packages (list/detail as defined in views). |
| *       | `/subs/subscriptions/` | User subscriptions (list/create as defined in views). |

### Payments

| Method | Endpoint | Description |
|--------|----------|-------------|
| *       | `/payments/gateways/` | Payment gateways. |
| *       | `/payments/pay/` | Create or process payment. |

### Admin

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/admin/` | Django admin (staff users). |

### Media (development)

When `IS_DEVEL` is True, media files are served at `/media/`.

---

## Tech stack

- **Django** 4.2
- **Django REST Framework**
- **djangorestframework-simplejwt** for JWT auth
- **SQLite** (default DB); media stored under `media/`

---

## Quick start

```bash
# Create venv, install deps
pip install -r requirements.txt

# Configure local settings (copy from local_settings.example if needed)
# Ensure SECRET_KEY, DEBUG, IS_DEVEL, DB, etc. are set.

# Migrate
python manage.py migrate

# Create superuser (username, phone_number, email required)
python manage.py createsuperuser

# Run server
python manage.py runserver
```

Then use `/users/token/` with username + password to get a JWT and call the endpoints above.


## 👤 Author

**Taha Hamedani**  
📧 [taha.hamedani8@gmail.com](mailto:taha.hamedani8@gmail.com)  


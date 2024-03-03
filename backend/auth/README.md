# Auth Service

## Endpoints
| Description           | Method | URL                   | Request Body                             |
|-----------------------|--------|-----------------------|------------------------------------------|
| Register a user       | POST   | `/api/user/register/` | `username`, `password1`, and `password2` |
| Obtain a token pair   | POST   | `/api/token/`         | `username`, `password`                   |
| Refresh an auth token | POST   | `/api/token/refresh/` | `refresh`                                |
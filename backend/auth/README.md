# Auth Service

## Endpoints
| Description           | Method | URL                   | Request Body                             | Body Type |
|-----------------------|--------|-----------------------|------------------------------------------|-----------|
| Register a user       | POST   | `/api/user/register/` | `username`, `password1`, and `password2` | Form Data |
| Obtain a token pair   | POST   | `/api/token/`         | `username`, `password`                   | JSON      |
| Refresh an auth token | POST   | `/api/token/refresh/` | `refresh`                                | JSON      |
intro to Django. Setting it up and all that
accounts app
## Permissions and Groups Setup

This application uses Django's permission and group system to control access.

### Custom Permissions
Defined in the Article model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

### Enforcement
Permissions are enforced in views using Django's
@permission_required decorator with raise_exception=True.

## HTTPS and Secure Redirect Configuration

### Enforced HTTPS
- All HTTP traffic is redirected to HTTPS using SECURE_SSL_REDIRECT.
- HSTS is enabled for one year with preload support.

### Secure Cookies
- Session and CSRF cookies are restricted to HTTPS connections.

### Security Headers
- Clickjacking protection via X_FRAME_OPTIONS
- XSS protection via browser filtering
- MIME sniffing prevention enabled

### Deployment
- SSL/TLS configured at the web server level (Nginx)
- Django configured to recognize secure proxy headers

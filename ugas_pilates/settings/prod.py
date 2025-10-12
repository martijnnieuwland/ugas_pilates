"""
Production settings for Uga's Pilates project.
"""

from .base import *

DEBUG = False

# Security best practices
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"

# Add any production-specific apps, middleware, or caching later

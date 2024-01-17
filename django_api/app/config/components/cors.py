CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:*'
    'http://localhost:*',
]

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:*',
    'http://localhost:*',
]

CSRF_COOKIE_SECURE = False

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = ('content-disposition',
                      'accept-encoding',
                      'content-type',
                      'accept',
                      'origin',
                      'authorization',
                      'x-api-key',
                      )

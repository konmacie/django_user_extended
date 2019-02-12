A few snippets useful for extending Django's built-in _User model_.

## Installation
Copy package into your project directory.
Add `'user_extended'` to `INSTALLED_APPS` in project's settings.

## Extending _User model_ using _Profile_
#### `models.py`
Two significant parts:
- using Meta API makes User's email field __unique__ and __required__
- creates `Profile` model with One-To-One relation with `User` model.
#### `forms.py`
Simple model forms used to edit existing `User` and `Profile` instances.
#### `views.py`
Example view used to edit logged-in user's `Profile`
#### `admin.py`
Adds and register `ProfileInline` to enable editing Profile in _Django's Admin_

## Email backend
#### `backend.py`
Backend that allows User to authenticate using email. Can be used alongside Django's built-in username backend.

To enable backend add following lines in project's settings:
```python
AUTHENTICATION_BACKENDS = [
    'user_extended.backend.EmailBackend',
    'django.contrib.auth.backends.ModelBackend', # default backend
]
```

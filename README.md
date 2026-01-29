Python Settings Manager

A simple Python project to manage user settings with add, update, delete, and view functionality.

Features
- Add new settings
- Update existing settings
- Delete settings
- View all settings

Usage
```python
from settings_manager import add_setting, update_setting, delete_setting, view_settings

settings = {}
print(add_setting(settings, ('theme', 'dark')))
print(update_setting(settings, ('theme', 'light')))
print(view_settings(settings))# python_settings_manager

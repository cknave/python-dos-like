Release History
===============

0.0.4 (21-Aug 2022)
-------------------
- Raise a runtime error when trying to run in the background on macOS

0.0.3 (14-Aug-2022)
-------------------
- Free dos-like allocated buffers when owning Python object is deleted
- Standardize on always raising an exception instead of sometimes returning
  ``None``
- Types are mypy approved

0.0.2 (11-Aug-2022)
-------------------
- Upgrade to dos-like d174ca4f
- Define dos-like ALWAYS_UPDATE flag by default

0.0.1 (10-Aug-2022)
-------------------
- Upgrade to dos-like 82085955
- Fix build and tests for Windows
- Fix build for macOS, but tests will not run in background thread

0.0.0 (09-Aug-2022)
-------------------
- Initial version, tested on Linux

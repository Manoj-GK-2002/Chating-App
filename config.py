import os


class Config:
    """Set Flask configuration variables from environment variables."""

    # Secret key for session management. You should generate a random key.
    SECRET_KEY = os.environ.get('60af9113343fa91b3b672bf99c2b2c22') or 'a-super-secret-key-that-you-should-change'

    # Database configuration for MySQL
    # File: config.py - CORRECTED EXAMPLE

    # ... other settings ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+mysqlconnector://root:root@localhost/finance_db'
    # ... other settings ...
    # Silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

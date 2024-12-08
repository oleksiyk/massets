# config.py

class Config:
    """
    Application configuration settings.
    """
    # Database settings
    MYSQL_USER = 'your_user'
    MYSQL_PASSWORD = 'your_password'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_DB = 'company_assets'

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
    SQLALCHEMY_ECHO = False  # Set to True for SQL debug logs

    # Google Sheets API settings
    GOOGLE_SHEETS_CREDENTIALS = 'path/to/credentials.json'

    # Export settings
    EXPORT_DIRECTORY = './exports/'

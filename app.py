# app.py

import sys
from PyQt6.QtWidgets import QApplication
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from assets.views.main_window import MainWindow  # Main window class
from config import Config

def setup_database():
    """
    Initializes the SQLAlchemy engine and session.
    """
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=Config.SQLALCHEMY_ECHO)
    Session = sessionmaker(bind=engine)
    return Session, engine

def main():
    """
    Entry point for the PyQT application.
    """
    # Initialize the database
    Session, engine = setup_database()

    # Initialize the PyQt application
    app = QApplication(sys.argv)

    # Pass the session and engine to the main window
    main_window = MainWindow(Session=Session, engine=engine)
    main_window.show()

    # Start the event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

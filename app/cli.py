import click
from app import db
from app.parse_logs import process_logs


def register(app):
    @app.cli.command("init-db")
    @click.argument("db-url", required=False)
    def init_db(db_url):
        """Initialize the database"""
        app.config['SQLALCHEMY_DATABASE_URI'] = db_url
        with app.app_context():
            db.create_all()
        click.echo("Database initialized.")

    @app.cli.command("load-data")
    @click.argument("logfile")
    @click.argument("db-url", required=False)
    def load_data(logfile, db_url):
        """Fill the database (use filename as argument)"""
        app.config['SQLALCHEMY_DATABASE_URI'] = db_url
        with app.app_context():
            db.create_all()
            process_logs(logfile)
        click.echo("Data loaded from log file.")

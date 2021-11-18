""" Application Script. The application instance is defined here """

import os

from application import create_app, db
from application.models import Users, OwnedStock, Transactions

app = create_app(os.getenv("FLASK_CONFIG") or "default")


""" More info at https://blog.miguelgrinberg.com/post/migrating-from-flask-script-to-the-new-flask-cli """


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=Users, OwnedStock=OwnedStock, Transactions=Transactions)

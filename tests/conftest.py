"""Support/configuration info for unit testing.

NOTE: use 'pytest' to run unit tests while in virtual env
    In event of module errors, you may need to add '.' to PYTHONPATH
"""
from app_package import app, db
import pytest
from app_package.models import ClassSchema
from flask import Flask

@pytest.fixture(autouse=True)
def test_client():
    flask_app = app
    app.config['TESTING'] = True

    testing_client = flask_app.test_client()

    context = flask_app.app_context()
    context.push()

    yield testing_client

    context.pop()

@pytest.fixture(autouse=True)
def init_database():
    db.create_all()

    yield db

    db.drop_all()

    
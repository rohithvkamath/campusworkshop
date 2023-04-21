"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="@dpg-ch135533cv203buiagig-a.oregon-postgres.render.com",
        database="todo_app_k9n3",
        user="todo_app_k9n3_user",
        password="Ry3t3cg1HL7veNeTVoYu8U0zJG8CVDGR")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

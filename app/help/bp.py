from flask import Flask


def register_api_v1(app: Flask, bp):
    app.register_blueprint(bp, url_prefix="/api")

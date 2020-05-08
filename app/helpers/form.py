from werkzeug.datastructures import MultiDict

from flask import session

from app.poezie.forms import *


def create_form(form_class, **kwargs):
    form_data = None
    if session.get("formdata") is not None:
        form_data = MultiDict(session.get("formdata"))
        session.pop("formdata")

    if "obj" in kwargs:
        # Fill with data from object
        form = form_class(obj=kwargs["obj"])
    elif form_data:
        form = form_class(form_data)
        form.validate()
    else:
        form = form_class()

    return form


def save_form_to_session(form_data):
    session["formdata"] = form_data

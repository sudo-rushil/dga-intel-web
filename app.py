# -*- coding: utf-8 -*-
import tensorflow as tf 
import numpy as np
import pandas as pd
import argparse as ap
import os
import uuid
from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError
from forms import LoginForm
from dgaintel import get_prob
from intel_query import get_whois

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'super secret')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    show_predictions_modal=False
    if form.validate_on_submit():
        _prediction = get_prob([form.domain.data])  
        form.whois = get_whois(form.domain.data)
        if _prediction == -1:
            form.prediction = "invalid (contains invalid characters)"
        elif _prediction > 0.5:
            form.prediction = "dga ({0:.2f})".format(_prediction)
        else:
            form.prediction = "legit ({0:.2f})".format(_prediction)
        return render_template('bootstrap.html', show_predictions_modal=True, form=form)
    return render_template('bootstrap.html', show_predictions_modal=False, form=form)

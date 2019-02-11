#!/usr/bin/python
# -*- coding: <utf-8> -*-
	import os, sys
from marketing import ap p
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, request,jsonify
from marketing.contactdefweb import *

from datetime import timedelta
from datetime import datetime
from flask import abort, redirect, url_for
from datetime import date
import datetime
from jinja2 import Environment
import jinja2
import logging
import logging.handlers
from flask_wtf import Form
from marketing.forms import SignupForm,ExtendedRegisterForm,addroll,addrollToUser
from flask_misaka import Misaka
from flask_simplemde import SimpleMDE
from flask_login import LoginManager,AnonymousUserMixin, current_user
from flask_security import Security, SQLAlchemyUserDatastore,UserMixin, RoleMixin, login_required,roles_required,user_registered,login_user, logout_user
from werkzeug import secure_filename
from flask import send_from_directory
from tasks import sendemailvagozar,  cdataAedit, newway, sendemailnoteToC,sendemailnoteToV,sendemailvagozar3rd
import redis
import json
import marketing.learn as  yad
from bs4 import BeautifulSoup



app = Flask(__name__)



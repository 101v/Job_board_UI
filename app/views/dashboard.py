import json
import random
import time
from flask import Blueprint, render_template, session, redirect, url_for, Response
from flask_login import login_required, current_user
from ..models.lv_jobtweet import JobTweet
from datetime import datetime
from sqlalchemy import text

dashboard_bluprint = Blueprint('dashboard', __name__)


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


def checkSession():
    if not session.get("name"):
        return redirect(url_for('auth.login'))


def getData():
    return JobTweet.query.all()


def generate_chart_data(tweets):

    for tweet in tweets:
        json_data = json.dumps(
            {
                "time": tweet.keywords,
                "value": float(tweet.confidence),
            }
        )
        yield f"data:{json_data}\n\n"
        time.sleep(2)


@dashboard_bluprint.route('/')
@dashboard_bluprint.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():

    checkSession()

    tweets = JobTweet.query.all()

    bar_labels = []
    bar_values = []
    bar_colors = []

    for tweet in tweets:
        bar_labels.append(tweet.keywords)
        bar_values.append(tweet.confidence)
        bar_colors.append(random.choice(colors))

    return render_template("dashboard/dashboard.html", tweets=tweets, max=1, labels=bar_labels, values=bar_values, set=zip(bar_values, bar_labels, bar_colors))


@dashboard_bluprint.route("/chart-data")
def chart_data():
    tweets = JobTweet.query.all()

    return Response(generate_chart_data(tweets), mimetype="text/event-stream")

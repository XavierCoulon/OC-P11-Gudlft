import json
import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


app = Flask(__name__)
app.secret_key = 'something_special'

# To set up the number of points required to book a place
POINTS_BY_PLACE = 3


def load_json(data):
    """

    Args:
        data: JSON file path

    Returns:
        list of dict.
    """
    with open(f"{data}.json") as c:
        return json.load(c)[data]


competitions = load_json('competitions')
clubs = load_json('clubs')
clubs_booking = {}

# Set up some datas for testing
if os.environ["ENV"] == "TEST":
    clubs = load_json("tests/clubs_dataset")
    competitions = load_json("tests/competitions_dataset")
    clubs_booking = {
        "Club Can Not Book More Than 12": {
            "Competition Can Not Book More Than 12": 10,
            "Competition 2": 0,
            "Competition 3": 0},
        "Club 2": {"Competition 1": 11, "Competition 2": 0, "Competition 3": 0},
        "Club 3": {"Competition 1": 0, "Competition 2": 0, "Competition 3": 0}
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show_summary', methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        flash("Sorry, that email was not found.")
        return redirect(url_for('index'))
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    try:
        found_club = [c for c in clubs if c['name'] == club][0]
        found_competition = [c for c in competitions if c['name'] == competition][0]
        return render_template('booking.html', club=found_club, competition=found_competition)
    except IndexError:
        flash("Competition or club not found")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchase_places', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    points = int(club["points"])
    places_required = int(request.form['places'])
    points_required = places_required * POINTS_BY_PLACE

    if datetime.now() > datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S"):
        flash(f"Not possible to book places on a post-dated competition - date: {competition['date']}.")
    elif places_required > 12:
        flash('Can not book more than 12 places!')
    elif points_required > points:
        flash('Not enough points!')
    elif places_required > int(competition['numberOfPlaces']):
        flash('Not enough places available in the competition!')
    else:
        try:
            # if places have already been booked for this club
            places = clubs_booking[club["name"]][competition["name"]]
        except KeyError:
            clubs_booking[club["name"]] = {competition["name"]: 0}
            places = 0
        if places + places_required > 12:
            flash(f"Not possible, you have already booked {places} places, the maximum must be <= 12")
        else:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
            points -= points_required
            club["points"] = str(points)
            clubs_booking[club["name"]][competition["name"]] += places_required
            flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/points')
def display_points():
    return render_template('points.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

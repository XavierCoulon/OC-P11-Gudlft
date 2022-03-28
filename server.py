import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()
clubs_booking = {}


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
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchase_places', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    points = int(club["points"])
    places_required = int(request.form['places'])

    if datetime.now() > datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S"):
        flash(f"Not possible to book places on a post-dated competition - date: {competition['date']}.")
    elif places_required > points:
        flash('Not enough points!')
    elif places_required > int(competition['numberOfPlaces']):
        flash('Not enough places available in the competition!')
    else:
        try:
            places = clubs_booking[club["name"]][competition["name"]]
            if places + places_required > 12:
                flash(f"Not possible, you have already booked {places} places, the maximum must be <= 12")
            else:
                competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
                points -= places_required
                club["points"] = str(points)
                clubs_booking[club["name"]][competition["name"]] += places_required
                flash(f"Great-booking complete! {places_required} places booked.")
        except KeyError:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
            points -= places_required
            club["points"] = str(points)
            try:
                clubs_booking[club["name"]][competition["name"]] = places_required
            except KeyError:
                clubs_booking[club["name"]] = {competition["name"]: places_required}
            flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)

# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

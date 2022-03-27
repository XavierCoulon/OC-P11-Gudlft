import json
from flask import Flask,render_template,request,redirect,flash,url_for, session


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
clubs_booking = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        flash("Sorry, that email was not found.")
        return redirect(url_for('index'))
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    points = int(club["points"])
    placesRequired = int(request.form['places'])
    if placesRequired > points:
        flash('Not enough points!')
    elif placesRequired > int(competition['numberOfPlaces']):
        flash('Not enough places available in the competition!')
    else:
        try:
            places = clubs_booking[club["name"]][competition["name"]]
            if places + placesRequired > 12:
                flash(f"Not possible, you have already booked {places} places, the maximum must be <= 12")
            else:
                competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
                points -= placesRequired
                club["points"] = str(points)
                clubs_booking[club["name"]][competition["name"]] += placesRequired
                flash('Great-booking complete!')
        except KeyError:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
            points -= placesRequired
            club["points"] = str(points)
            try:
                clubs_booking[club["name"]][competition["name"]] = placesRequired
            except KeyError:
                clubs_booking[club["name"]] = {competition["name"]: placesRequired}
            flash('Great-booking complete!')
    print(clubs_booking)
    return render_template('welcome.html', club=club, competitions=competitions)

# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
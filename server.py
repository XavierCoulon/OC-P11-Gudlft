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


@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        flash("Sorry, that email was not found.")
        return redirect(url_for('index'))
    if not club["name"] in clubs_booking:
        clubs_booking[club["name"]] = 0
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
    if clubs_booking[club["name"]] + placesRequired > 12:
        flash(f"Not possible, you have already booked {clubs_booking[club['name']]} places, the total should be <= 12")
    elif placesRequired <= points:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        points -= placesRequired
        club["points"] = str(points)
        clubs_booking[club["name"]] += placesRequired
        flash('Great-booking complete!')
    else:
        flash('Not enough points!')

    return render_template('welcome.html', club=club, competitions=competitions)



# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
from flask import Flask, jsonify
import requests
import os  # You need to import os to get the PORT

app = Flask(__name__)

# Function to fetch data from Sleeper API
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data"}, response.status_code

# Route to fetch league info
@app.route('/league/<league_id>', methods=['GET'])
def get_league_info(league_id):
    url = f"https://api.sleeper.app/v1/league/{league_id}"
    return fetch_data(url)

# Route to fetch draft info
@app.route('/draft/<draft_id>', methods=['GET'])
def get_draft_info(draft_id):
    url = f"https://api.sleeper.app/v1/draft/{draft_id}"
    return fetch_data(url)

# Route to fetch roster data
@app.route('/league/<league_id>/rosters', methods=['GET'])
def get_rosters(league_id):
    url = f"https://api.sleeper.app/v1/league/{league_id}/rosters"
    return fetch_data(url)

# Route to fetch transactions for a league and round
@app.route('/league/<league_id>/transactions/<round>', methods=['GET'])
def get_transactions(league_id, round):
    url = f"https://api.sleeper.app/v1/league/{league_id}/transactions/{round}"
    return fetch_data(url)

# Route to fetch matchups for a specific week
@app.route('/league/<league_id>/matchups/<week>', methods=['GET'])
def get_matchups(league_id, week):
    url = f"https://api.sleeper.app/v1/league/{league_id}/matchups/{week}"
    return fetch_data(url)

# Route to fetch trending players (add/drop)
@app.route('/players/nfl/trending/<type>', methods=['GET'])
def get_trending_players(type):
    url = f"https://api.sleeper.app/v1/players/nfl/trending/{type}"
    return fetch_data(url)

# Route to fetch NFL state
@app.route('/state/nfl', methods=['GET'])
def get_nfl_state():
    url = "https://api.sleeper.app/v1/state/nfl"
    return fetch_data(url)

# Route to fetch all NFL players
@app.route('/players/nfl', methods=['GET'])
def get_all_nfl_players():
    url = "https://api.sleeper.app/v1/players/nfl"
    return fetch_data(url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

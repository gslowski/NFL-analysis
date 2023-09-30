class Constants:
    TEAM_NAME_ABBR = {
                        "ARI": "Arizona Cardinals",
                        "ATL": "Atlanta Falcons",
                        "BAL": "Baltimore Ravens",
                        "BUF": "Buffalo Bills",
                        "CAR": "Carolina Panthers",
                        "CHI": "Chicago Bears",
                        "CIN": "Cincinnati Bengals",
                        "CLE": "Cleveland Browns",
                        "DAL": "Dallas Cowboys",
                        "DEN": "Denver Broncos",
                        "DET": "Detroit Lions",
                        "GNB": "Green Bay Packers",
                        "HOU": "Houston Texans",
                        "IND": "Indianapolis Colts",
                        "JAX": "Jacksonville Jaguars",
                        "KAN": "Kansas City Chiefs",
                        "LVR": "Las Vegas Raiders",
                        "LAC": "Los Angeles Chargers",
                        "LAR": "Los Angeles Rams",
                        "MIA": "Miami Dolphins",
                        "MIN": "Minnesota Vikings",
                        "NWE": "New England Patriots",
                        "NOR": "New Orleans Saints",
                        "NYG": "New York Giants",
                        "NYJ": "New York Jets",
                        "PHI": "Philadelphia Eagles",
                        "PIT": "Pittsburgh Steelers",
                        "SFO": "San Francisco 49ers",
                        "SEA": "Seattle Seahawks",
                        "TAM": "Tampa Bay Buccaneers",
                        "TEN": "Tennessee Titans",
                        "WAS": "Washington Commanders"
                    }
    
    TEAM_NAME_ABBR_SWAPPED = {v: k for k, v in TEAM_NAME_ABBR.items()}
    TEAM_NAME_ABBR_SWAPPED['San Diego Chargers'] = 'SDG'
    TEAM_NAME_ABBR_SWAPPED['Oakland Raiders'] = 'OAK'
    TEAM_NAME_ABBR_SWAPPED['Washington Redskins'] = 'WAS'
    TEAM_NAME_ABBR_SWAPPED['Washington Football Team'] = 'WAS'
    TEAM_NAME_ABBR_SWAPPED['St. Louis Rams'] = 'STL'
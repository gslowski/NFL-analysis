class NFLFootballGame:
    def __init__(self, home_team, away_team, date, time, location):
        # Game metadata
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.time = time
        self.location = location
        
        # Coaches
        self.home_coach = ''
        self.away_coach = ''
        
        # Score
        self.home_score = 0
        self.away_score = 0
        
        # Records (after final)
        self.home_win_record = 0
        self.home_loss_record = 0
        self.home_tie_record = None
        self.away_win_record = 0
        self.away_loss_record = 0
        self.away_tie_record = None
        
        # Stat tables
        self.quarter_table = None
        self.game_info_table = None
        self.officials_table = None
        self.expected_points_table = None
        self.team_stats_table = None

    def display_score(self):
        print(f"{self.home_team} {self.home_score} - {self.away_team} {self.away_score}")

class StatTable:
    def __init__(self, table_name, df):
        self.table_name = table_name
        self.df = df

class QuarterScores(StatTable):
    def __init__(self, table_name, df):
        super().__init__(table_name, df)
        self.q1_away_score=0
        self.q2_away_score=0
        self.q3_away_score=0
        self.q4_away_score=0
        self.q1_home_score=0
        self.q2_home_score=0
        self.q3_home_score=0
        self.q4_home_score=0

class Scoring(StatTable):
    def __init__(self, table_name, df):
        super().__init__(table_name, df)
        
class GameInfo(StatTable):
    def __init__(self, table_name, df):
        super().__init__(table_name, df)
        self.roof=''
        self.surface=''
        self.vegas_line=''
        self.over_under=0

class Officials(StatTable):
    def __init__(self, table_name, df):
        super().__init__(table_name, df)
        self.referee=''
        self.umpire=''
        
class ExPtsSummary(StatTable):
    def __init__(self, table_name, df):
        super().__init__(table_name, df)
        
class TeamStats(StatTable):
    def __init__(self, table_name, df):
        super().__init__(table_name, df)
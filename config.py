API_LOCATION = '/api'
APP_SCHEME = 'http'
SQLALCHEMY_DATABASE_URI = 'postgresql://mreport:password@localhost:5432/dataviz'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SCHEMA = "data" ## Comment this line if you don't need schema or if you use SQLite
MREPORT_REPORTS = "backend/reports"
MREPORT_LOCATION = "/mreport"
import nest
import sys
import db_home_weather
from datetime import datetime

# nest api setup
client_id = '3e3232bf-5f6b-48e8-948f-a9d5cb88ae48'
client_secret = 'ELCczbwUnXhnSp66CfC7GeeqP'
access_token_cache_file = 'nest.json'
napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_cache_file)

# home_weather db setup
db = db_home_weather.db_home_weather()

# get variables
for structure in napi.structures:
    for device in structure.thermostats:
        Temp = device.temperature
        Mode = device.mode
        Humidity = device.humidity
        Target = device.target
        State = device.hvac_state

# load data into home_weather
db.run_sql("""INSERT INTO nest_log (Mode, State, Temp, Target, Humidity)
    VALUES ('{}','{}',{},{},{})""".format(Mode, State, Temp, Target, Humidity))
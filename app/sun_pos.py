import datetime
from pysolar import solar


# Calculate the altitude and azimuth of the sun given the location and the time
def sun_pos(payload):
    # Input variables
    lat = payload["lat"]  # Lattitude (deg)
    lon = payload["lon"]  # Longitude (deg)
    epoch = payload["epoch"]  # time (Linux epoch in seconds)

    # Calculate UTC time
    date = datetime.datetime.fromtimestamp(epoch, tz=datetime.timezone.utc)

    # Calculate the azimuth and altitude of the sun using [Pysolar](https://pysolar.org/)
    altitude_sun = solar.get_altitude(lat, lon, date)  # Sun's altitude (deg)
    azimuth_sun = solar.get_azimuth(lat, lon, date)  # Sun's azimuth (deg)

    return {"altitude": altitude_sun, "azimuth": azimuth_sun}

from app.angle_functions import normalize_angle


def is_glare(sun, orientation):
    altitude_sun = sun["altitude"]  # Sun's altitude (deg)
    azimuth_sun = sun["azimuth"]  # Sun's azimuth (deg)

    heading = normalize_angle(orientation - azimuth_sun)
    altitude = normalize_angle(altitude_sun)

    # There is a possibility of a direct glare if the azimuthal difference between the sun and the direction of the car travel (and hence
    # the direction of forward-facing camera) is less than 30 degrees and the altitude of the sun is less than 45 degrees.
    if abs(heading) <= 30.0 and 45.0 >= altitude >= 0:
        glare = "true"
    else:
        glare = "false"

    return glare

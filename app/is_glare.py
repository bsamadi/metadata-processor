def is_glare(sun,orientation):
    altitude_sun = sun['altitude'] # Sun's altitude (deg)
    azimuth_sun = sun['azimuth']   # Sun's azimuth (deg)

    # There is a possibility of a direct glare if the azimuthal difference between the sun and the direction of the car travel (and hence 
    # the direction of forward-facing camera) is less than 30 degrees and the altitude of the sun is less than 45 degrees.
    if abs(orientation - azimuth_sun) <= 30.0 and 45.0 >= altitude_sun >= 0:
       glare="true"
    else:
       glare="false"
    
    return glare
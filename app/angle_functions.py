def normalize_angle(angle):
    # reduce the angle
    angle = angle % 360

    # angle in [0,360)
    angle = (angle + 360) % 360

    # angle in (-180,180]
    if (angle > 180):
        angle -= 360

    return angle

def traffic_light_system():
    states = ["Red," "Yellow," "Green"]
    directions = ["North," "South," "East," "West"]
    green_duration = 25 #seconds
    yellow_duration = 5 #seconds
    red_duration = 25 #seconds
    pedestrian_duration = 10 #seconds

    while True():
        if "emergency_vehicle":
         # Handle emergency vehicle
          current_direction = "get_emergency_direction"()
          change_light = (current_direction, "Green", "emergency_direction")
          set_other_directions = ("Red")

    for direction in directions():
       # Manage normal traffic 
         change_light (direction, "Green", green_duration)
         change_light (direction, "Yellow", yellow_duration)
         change_light (direction, "Red", red_duration)

       # Start pedestrian crossing
         "start_pedestrian_crossing"(pedestrian_duration)

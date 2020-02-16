#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:18:20 2020

@author: jaco
"""
import json

print("Read JSON from file")
filename = "calculateroute.json"
file = open(filename)

print("Converting JSON to dictionary")
route_json = file.read()
route_dict = json.loads(route_json)

print("Parsing data")
response_dict = route_dict["response"]
route_list = response_dict["route"]
#waypoint_dict = route_list[0]
for waypoint_dict in route_list:
    leg_list = waypoint_dict["leg"]
    mode_dict = waypoint_dict["mode"]
    summary_dict = waypoint_dict["summary"]
    waypoint_list = waypoint_dict["waypoint"]
    
    for leg_dict in leg_list:
        # Start leg
        start_dict = leg_dict["start"]
        label = start_dict["label"]
        side_of_street = start_dict["sideOfStreet"]
        type_ = start_dict["type"]
        output = "Leg Start - Street name: {}, Side of Street: {}, Type: {}"
        print(output.format(label, side_of_street, type_))
        
        # End leg
        end_dict = leg_dict["end"]
        label = end_dict["label"]
        sideOfStreet = end_dict["sideOfStreet"]
        type_ = end_dict["type"]
        output = "Leg End - Street name: {}, Side of Street: {}, Type: {}"
        print(output.format(label, sideOfStreet, type_))
        
        # Maneuver
        maneuver_list = leg_dict["maneuver"]
        for maneuver_dict in maneuver_list:
            instruction = maneuver_dict["instruction"]
            position = maneuver_dict["position"]
            output = "Maneuver = Position: {}, Instruction: {}"
            print(output.format(position, instruction))
    
    # Waypoints
    for waypoint_dict in waypoint_list:
        mapped_position = waypoint_dict["mappedPosition"]
        latitude = mapped_position["latitude"]
        longitude = mapped_position["longitude"]
        combined = str(latitude) + "," + str(longitude)
        output = "Waypoint - Latitude: {}, Longitude: {}, Combined: {}"
        print(output.format(latitude, longitude, combined))
    
    # Mode
    mode_type = mode_dict["type"]
    transport_modes = mode_dict["transportModes"]
    output = "Mode - Type: {}, Transport modes: {}"
    print(output.format(mode_type, transport_modes))
    
    # Summary
    distance = round(summary_dict["distance"] / 1000, 1)
    base_time = round(summary_dict["baseTime"] / 60, 0)
    output = "Summary - Distance: {} km, Base Time: {} min"
    print(output.format(distance, base_time))
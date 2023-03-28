#Train Journey
stations=["station1","station2","station3","station4"]
current_station=0
destination_station="station3"
while stations[current_station] !=destination_station:
        print(f"Condition : {stations[current_station] !=destination_station}")
        print(f"current station is :{stations[current_station]}")
        print(f"my destination is:{destination_station}")
        print("continue the journey i have not reached the destination")
        current_station=current_station+1
        print(f"Next station is : {stations[current_station]}")
else:
        print(f"Condition : {stations[current_station] !=destination_station}")
        print(f"i have arrived at {stations[current_station]}")


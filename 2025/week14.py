

#******************************************************
#   Object oriented programming 
#******************************************************

class Satellite:
    def __init__(self, name, orbit_type, altitude):
        self.name = name
        self.orbit_type = orbit_type
        self.altitude = altitude  # in kilometers
        self.is_operational = False

    def launch(self):
        if not self.is_operational:
            self.is_operational = True
            return f"{self.name} has been launched into {self.orbit_type} orbit at {self.altitude} km."
        return f"{self.name} is already operational."

    def change_orbit(self, new_orbit, new_altitude):
        self.orbit_type = new_orbit
        self.altitude = new_altitude
        return f"{self.name} changed orbit to {self.orbit_type} at {self.altitude} km."

    def report_status(self):
        status = "operational" if self.is_operational else "not operational"
        return f"{self.name} is {status}, orbit: {self.orbit_type}, altitude: {self.altitude} km."


sat1 = Satellite(name = "Hubble", orbit_type = "Low Earth Orbit", altitude = 569)
sat2 = Satellite(name = "GPS IIF",orbit_type = "Medium Earth Orbit", altitude = 20200)

print(sat1.report_status(), "\n")
print(sat1.launch(), "\n")
print(sat1.report_status(), "\n")
print(sat2.launch(), "\n")





import time

class RocketLaunchSimulator:
    def __init__(self):
        self.stage = "Pre-Launch"
        self.fuel = 100
        self.altitude = 0
        self.speed = 0

    def start_checks(self):
        print("Pre-Launch Checks: All systems are 'Go' for launch.")

    def launch(self):
        print("Launching...")
        self.stage = 1
        self.update_parameters()

        while self.stage != "Mission Successful" and self.stage != "Mission Failed":
            user_input = input("Type 'fast_forward X' to simulate X seconds (or type 'launch' to end the mission): ")
            if user_input.lower() == 'launch':
                break
            elif user_input.startswith('fast_forward'):
                try:
                    seconds = int(user_input.split()[1])
                    self.fast_forward(seconds)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def fast_forward(self, seconds):
        for _ in range(seconds):
            time.sleep(1)  # Simulate one second passing
            self.update_parameters()

    def update_parameters(self):
        if self.stage == "Mission Successful" or self.stage == "Mission Failed":
            return

        # Simulate rocket parameters update
        self.fuel -= 1
        self.altitude += 10
        self.speed += 100

        # Check if fuel is depleted
        if self.fuel <= 0:
            self.stage = "Mission Failed due to insufficient fuel"
        else:
            print(f"Each Second of Flight: Stage: {self.stage}, Fuel: {self.fuel}%, Altitude: {self.altitude} km, Speed: {self.speed} km/h")

# Main program
simulator = RocketLaunchSimulator()
simulator.start_checks()
simulator.launch()

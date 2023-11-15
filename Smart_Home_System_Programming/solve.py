from abc import ABC, abstractmethod
from datetime import datetime
import json

# Device Factory
class DeviceFactory:
    @staticmethod
    def create_device(device_info):
        device_type = device_info['type']
        if device_type == 'light':
            return Light(device_info['id'], device_info['status'])
        elif device_type == 'thermostat':
            return Thermostat(device_info['id'], device_info['temperature'])
        elif device_type == 'door':
            return Door(device_info['id'], device_info['status'])
        else:
            raise ValueError(f"Invalid device type: {device_type}")

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, device):
        pass

# Subject Interface
class Subject(ABC):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, device):
        for observer in self.observers:
            observer.update(device)

# Smart Device (Proxy Pattern)
class SmartDevice(Subject, Observer):
    def __init__(self, device_id):
        super().__init__()
        self.device_id = device_id

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def set_status(self, status):
        pass

    def update(self, device):
        pass

# Light (Concrete Device)
class Light(SmartDevice):
    def __init__(self, device_id, status):
        super().__init__(device_id)
        self.status = status

    def get_status(self):
        return f"Light {self.device_id} is {self.status}."

    def set_status(self, status):
        self.status = status
        self.notify_observers(self)

# Thermostat (Concrete Device)
class Thermostat(SmartDevice):
    def __init__(self, device_id, temperature):
        super().__init__(device_id)
        self.temperature = temperature

    def get_status(self):
        return f"Thermostat is set to {self.temperature} degrees."

    def set_status(self, temperature):
        self.temperature = temperature
        self.notify_observers(self)

# Door (Concrete Device)
class Door(SmartDevice):
    def __init__(self, device_id, status):
        super().__init__(device_id)
        self.status = status

    def get_status(self):
        return f"Door is {self.status}."

    def set_status(self, status):
        self.status = status
        self.notify_observers(self)

# Smart Home System
class SmartHomeSystem:
    def __init__(self, devices):
        self.devices = [DeviceFactory.create_device(device_info) for device_info in devices]

    def execute_command(self, command):
        eval(command)

    def get_status_report(self):
        status_report = [device.get_status() for device in self.devices]
        return " ".join(status_report)

# Smart Home System Commands
def turn_on(device_id):
    device = find_device(device_id)
    device.set_status('on')

def set_schedule(device_id, time, command):
    device = find_device(device_id)
    schedule_task(device, time, command)

def add_trigger(condition, operator, value, action):
    device_id = extract_device_id(action)
    device = find_device(device_id)
    automate_trigger(device, condition, operator, value, action)

# Utility Functions
def find_device(device_id):
    return next((device for device in smart_home_system.devices if device.device_id == device_id), None)

def schedule_task(device, time, command):
    task = {'device': device.device_id, 'time': time, 'command': command}
    scheduled_tasks.append(task)

def automate_trigger(device, condition, operator, value, action):
    trigger = {'condition': f"{device.device_id} {operator} {value}", 'action': action}
    automated_triggers.append(trigger)

def extract_device_id(action):
    return int(action.split('(')[1].split(')')[0])

# Client Code
devices_info = [
    {'id': 1, 'type': 'light', 'status': 'off'},
    {'id': 2, 'type': 'thermostat', 'temperature': 70},
    {'id': 3, 'type': 'door', 'status': 'locked'}
]

smart_home_system = SmartHomeSystem(devices_info)
scheduled_tasks = []
automated_triggers = []

commands = [
    'turn_on(1)',
    'set_schedule(2, "06:00", "turn_on(1)")',
    'add_trigger("temperature", ">", 75, "turn_on(1)")'
]

for command in commands:
    smart_home_system.execute_command(command)

# Output
print(smart_home_system.get_status_report())
print(f"Scheduled Tasks: {json.dumps(scheduled_tasks)}")
print(f"Automated Triggers: {json.dumps(automated_triggers)}")

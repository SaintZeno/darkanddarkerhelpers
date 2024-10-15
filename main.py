import keyboard
import time
import yaml
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController

from helpers.banners import print_banner  

GLOBAL_SLEEP = 0.01

# Initialize the keyboard controller
keyboard_controller = KeyboardController()
mouse_controller = MouseController()


# Load configuration
def load_config(file_path='config.yml'):
    try:
        with open(file_path, 'r') as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError:
        print_banner("no-clear", "helpers-intro")
        

# Execute a macro based on the configuration
def execute_macro(macro_name, config):
    macro = config['macros'].get(macro_name)
    if macro:
        for action in macro:
            action_type = action['action']
            
            if action_type == 'move_cursor':
                mouse_controller.position = (action['x'], action['y'])
            
            elif action_type in ['press', 'press_and_hold', 'release']:
                key = action['key']
                if key == 'space':
                    key = Key.space
                elif key == 'shift':
                    key = Key.shift
                
                if action_type == 'press':
                    keyboard_controller.press(key)
                    time.sleep(action['duration'])
                    keyboard_controller.release(key)
                elif action_type == 'press_and_hold':
                    keyboard_controller.press(key)
                    time.sleep(action['duration'])
                elif action_type == 'release':
                    keyboard_controller.release(key)
                elif action_type == 'wait':
                    time.sleep(action['duration'])
            
            time.sleep(GLOBAL_SLEEP)  # Small delay between actions
    else:
        print(f"Macro '{macro_name}' not found in configuration.")

# Main function
def main():
    config = load_config()
    active_state = False
    last_toggle_state = False
    active_macro = None

    print_banner("single", "header-start")
    print_banner("no-clear", "user-options")
    #print("\nMacro script is running. Press Ctrl+C to exit.")

    try:
        while True:
            
            key_state = keyboard.is_pressed(config['toggle_button'])

            # Update and display the current state
            print(f"MACRO-CONTROL: {'ON' if active_state else 'OFF'} | ACTIVE-MACRO: {active_macro or 'None'}", end="\r")

            # Toggle the active state
            if key_state != last_toggle_state:
                last_toggle_state = key_state
                if last_toggle_state:
                    active_state = not active_state
                    #print_banner("no-clear", "header-start")
                    print(f"\nMacro Control: {'Enabled' if active_state else 'Disabled'}")

            # Check for hotkey presses and execute macros if active
            if active_state:
                for hotkey, macro_name in config['hotkeys'].items():
                    if keyboard.is_pressed(hotkey):
                        active_macro = macro_name
                        execute_macro(macro_name, config)

            # Option to kill the program
            if keyboard.is_pressed("esc"):
                print_banner("single", "header-stop")
                print_banner("no-clear", "action-close-program")
                break

            # Small delay to prevent high CPU usage
            time.sleep(0.001)

    except KeyboardInterrupt:
        print_banner("single", "header-stop")
        print_banner("no-clear", "action-close-program")

if __name__ == "__main__":
    main()
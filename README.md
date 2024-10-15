# Dark and Darker Macro System

This project implements a customizable macro system for a game, specifically designed for Dark and Darker. It allows users to define and execute complex sequences of keyboard and mouse actions using a simple configuration file.

## Features

- Custom macro definitions using YAML configuration
- Support for keyboard presses, holds, and releases
- Mouse cursor movement integration
- Hotkey mapping for quick macro execution
- Toggle functionality for enabling/disabling macros

## Requirements

- Python 3.x
- see requirements.txt

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/druid-macro-system.git
   cd druid-macro-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Macros and hotkeys are defined in the `config.yml` file. Here's an example structure:
# config.yaml
macros:
  druid_rat_jump:
    # turn into rat
    - action: press_and_hold
      key: q
      duration: 0.1
    - action: move_cursor
      x: 1415
      y: 870
    - action: release
      key: q
    # jump with space immediately after transforming
    - action: press
      key: space
      duration: 0.5
  druid_panther_jump:
    # turn into panther
    - action: press_and_hold
      key: q
      duration: 0.5
    - action: move_cursor
      x: 1050
      y: 500
    - action: release
      key: q
    # wait a split second
    - action: wait
      duration: 0.1
    # as panther, jump
    - action: press
      key: space
      duration: 0.5 
    # as panther, dash, with F
    - action: press
      key: f
      duration: 0.05
    # wait a split second
    #- action: wait
    #  duration: 0.1
    # turn into chicken
    - action: press_and_hold
      key: q
      duration: 0.01
    - action: move_cursor
      x: 890
      y: 850
    - action: release
      key: q
    # use the first chicken jump
    - action: press
      key: space
      duration: 0.5 
    - action: press
      key: space
      duration: 0.5 
    

hotkeys:
  '5': druid_rat_jump
  c: druid_panther_jump
  
toggle_button: f4
# end config


### Macro Actions

- `move_cursor`: Move the mouse cursor to specified coordinates
- `press`: Press and release a key for a specified duration
- `press_and_hold`: Press and hold a key
- `release`: Release a previously held key

## Usage

1. Edit the `config.yml` file to define your macros and hotkey mappings.
2. Run the main script:
   ```
   python main.py
   ```
3. Press the toggle button (default: F4) to enable/disable the macro system.
4. Use the defined hotkeys to execute macros in-game.

## Customization

You can easily extend the system by adding new action types in the `execute_macro` function and updating the configuration file accordingly.
If you're not sure what the coordinates should be for the `move_cursor` action, you can use the script in `helpers/mouse_coordinates.py` to find them. Run the script and move your cursor to the desired location, then the coordinates will be printed to the console.

## Disclaimer

This tool is for educational purposes only. Make sure to comply with the terms of service of any games you use this with.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

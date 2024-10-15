from os import system
import yaml


with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

def generate_user_options():
    options = ["All available options listed below:\n"]
    
    # Add toggle macro option
    options.append(f"1. Toggle On/Off | Press {config['toggle_button'].upper()}")
    
    # Add hotkey options
    for i, (hotkey, macro) in enumerate(config['hotkeys'].items(), start=2):
        options.append(f"{i}. Enable {macro} | Press {hotkey.upper()}")
    
    # Add kill program option
    options.append(f"{len(config['hotkeys']) + 2}. Kill program | Press ESC")
    
    return "\n".join(options)

banners = {
    "header-start": """
██████╗  █████╗ ██████╗ ██╗  ██╗     █████╗ ███╗   ██╗██████╗     ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔══██╗████╗  ██║██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║  ██║███████║██████╔╝█████╔╝     ███████║██╔██╗ ██║██║  ██║    ██║  ██║███████║██████╔╝█████╔╝ █████╗  ██████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗     ██╔══██║██║╚██╗██║██║  ██║    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║  ██║██║  ██╗    ██║  ██║██║ ╚████║██████╔╝    ██████╔╝██║  ██║██║  ██║██║  ██╗███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                   
███╗   ███╗ █████╗  ██████╗██████╗  ██████╗ ███████╗                                                               
████╗ ████║██╔══██╗██╔════╝██╔══██╗██╔═══██╗╚══███╔╝                                                               
██╔████╔██║███████║██║     ██████╔╝██║   ██║  ███╔╝                                                                
██║╚██╔╝██║██╔══██║██║     ██╔══██╗██║   ██║ ███╔╝                                                                 
██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║╚██████╔╝███████╗                                                               
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                                                               
by: .... | inspired by: ...
    """,
    "header-stop": """
███████╗████████╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ ██╗
██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██║
███████╗   ██║   ██║   ██║██████╔╝██████╔╝█████╗  ██║  ██║██║
╚════██║   ██║   ██║   ██║██╔═══╝ ██╔═══╝ ██╔══╝  ██║  ██║╚═╝
███████║   ██║   ╚██████╔╝██║     ██║     ███████╗██████╔╝██╗
╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚═════╝ ╚═╝
    """,
    "user-options": generate_user_options(),
    "action-close-program": "ACTION: Program Closed",
    "helpers-scan-one": "Please input the values for the first scan box below: [Ex. - left,top,width,height]",
    "helpers-scan-two": "Please input the values for the second scan box below: [Ex. - left,top,width,height]",
    "helpers-modifier": "Please input the macro timing modifier value below: [Ex. 1.5]",
    "helpers-intro": """
STATUS: Config file not found!
Please create a config file called config.yml and run the script again.
    """
}

def print_banner(ban_type, *banner):
    if ban_type == "single":
        system("cls")
        print(banners[banner[0]])
    elif ban_type == "double":
        system("cls")
        print(banners[banner[0]])
        print(banners[banner[1]])
    elif ban_type == "no-clear":
        print(banners[banner[0]])

# Example usage:
# print_banner("single", "header-start")
# print_banner("double", "header-start", "user-options")
# print_banner("no-clear", "helpers-intro")
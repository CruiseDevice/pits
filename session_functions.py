from global_settings import SESSION_FILE
import yaml
import os

def save_session(state):
    state_to_save = {
        key: value for key, value in state.items()
    }
    with open(SESSION_FILE, 'w') as f:
        yaml.dump(state_to_save, f)


def load_session(state):
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as f:
            try:
                loaded_state = yaml.safe_load(f) or ()
                for key, value in loaded_state.items():
                    state[key] = value

                return True
            except yaml.YAMLError:
                return False
            

def delete_session(state):
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
    for key in list(state.keys()):
        del state[key]


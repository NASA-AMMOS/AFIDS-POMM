class State():
    def __init__(self):
        self.state = {
            'core': {
                'planet': None,
                'command': None,
            },
            'MapProject': {},
            'CoRegister': {},
            'Mosaic': {}
        }

    def set_state(self, command, key, value):
        if (command in self.state):
            self.state[command][key] = value

    def get_state(self):
        return self.state

    def output_state():
        print('output')

import numpy as np

### ENVIRONMENT ###

class Environment:
    '''The class that represents our pretty environment'''
    default_parameters = {
        'width': 10,
        'height': 10,
        'obstacles': [(2, 2), (2, 3), (2, 4), (6, 7), (7, 7)],
        'nb_trashes': 30
    }

    def __init__(self, pos = (0, 0), w=0, h=0, nb_trashes=0):
        '''
        class initialisation

        :param w: width of the environment (not including walls)
        :param h: height of the environment (not including walls)
        :param nb_trashes: number of trashes in the environment
        '''

        self.width = self.default_parameters['width'] if w == 0 else w

        self.height = self.default_parameters['height'] if h == 0 else h

        self.nb_trashes = self.default_parameters['nb_trashes'] if nb_trashes == 0 else nb_trashes

        self.obstacles = self.default_parameters['obstacles']

        self.action_space_n = 4 # cardinality of action space : {LEFT, RIGHT, UP, DOWN} = {0, 1, 2, 3}

        self.state_space_n = self.width * self.height # cardinality of action space : Position of agent

        self.agent_state = pos

        # randomize positions of trashes
        self.trashes = []
        i = 0
        while i < self.nb_trashes:
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            if (x, y) not in self.trashes and (x, y) not in self.obstacles:
                self.trashes.append((x, y))
                i += 1

    def display(self):
        for i in range(self.height + 1):
            for j in range(self.width + 1):
                if j < self.width:
                    if (i, j) in self.trashes:
                        symbol = '*'
                    elif (i, j) in self.obstacles:
                        symbol = '#'
                    elif (i, j) == self.agent_state:
                        symbol = 'o'
                    else:
                        symbol = ' '
                    print('| %s ' % symbol, end='',
                          flush=True)  # don't bother these parameters I only use those to print on same line
                else:
                    print('|', end='', flush=True)
            print()
        print(self.trashes)
        self.step(1)

    def step(self, a):
        '''
        execute action a

        :param a: an action in {LEFT, RIGHT, UP, DOWN}
        :return: new state, reward, termination flag, info
        '''

        # calculate new state
        go_into_wall = False
        if a == 0:  # LEFT
            if self.agent_state[0] == 0:
                go_into_wall = True
            else:
                self.agent_state = (self.agent_state[0] - 1, self.agent_state[1])
        elif a == 1:  # RIGHT
            if self.agent_state[0] == self.width - 1:
                go_into_wall = True
            else:
                self.agent_state = (self.agent_state[0] + 1, self.agent_state[1])
        elif a == 2:  # UP
            if self.agent_state[1] == 0:
                go_into_wall = True
            else:
                self.agent_state = (self.agent_state[0], self.agent_state[1] - 1)
        else:  # DOWN
            if self.agent_state[1] == self.height - 1:
                go_into_wall = True
            else:
                self.agent_state = (self.agent_state[0], self.agent_state[1] + 1)
        print(self.agent_state)

        # calculate reward
        if go_into_wall:
            reward = -5
        elif self.agent_state in self.trashes:
            reward = 0
        else:
            reward = -1
        print(reward)
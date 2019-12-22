import sys

DIRECTIONS = ['N', 'E', 'S', 'W']


class Rover:

    def __init__(self, x: int, y: int, direction: str):
        self.x, self.y, self.direction = x, y, direction

    def perform_action(self, action):
        if action in ('L', 'R'):
            self.rotate(action)
        else:
            self.move_forward()

    def rotate(self, d):
        index = DIRECTIONS.index(self.direction)
        index += (1 if d == 'R' else -1)
        index = index % 4
        self.direction = DIRECTIONS[index]

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'W':
            self.x -= 1


def main(input_file):
    with open(input_file) as f:
        input_lines = f.readlines()

    plateau_width, plateau_height = (int(x) for x in input_lines[0].strip().split(' '))

    for i in range(1, len(input_lines), 2):
        x, y, d = input_lines[i].strip().split(' ')
        rover = Rover(int(x), int(y), d)

        for action in input_lines[i + 1].strip():
            rover.perform_action(action)
            assert 0 <= rover.x <= plateau_width and 0 <= rover.y <= plateau_height
        print('%d %d %s' % (rover.x, rover.y, rover.direction))


if __name__ == '__main__':
    main(sys.argv[1])

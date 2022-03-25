with open('input.txt', 'r') as f:
    line = f.read().replace("target area: ", '')
x_rng, y_rng = line.split(',')
x_rng = tuple(map(int, x_rng.replace('x=', '').split('..')))
y_rng = tuple(map(int, y_rng.replace('y=', '').split('..')))
y_vel_max = -y_rng[0] - 1
print(y_vel_max * (y_vel_max + 1) // 2)

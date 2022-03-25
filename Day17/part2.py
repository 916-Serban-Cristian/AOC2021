with open('input.txt', 'r') as f:
    line = f.read().replace("target area: ", '')
x_rng, y_rng = line.split(',')
x_rng = tuple(map(int, x_rng.replace('x=', '').split('..')))
y_rng = tuple(map(int, y_rng.replace('y=', '').split('..')))
x_rng2 = range(x_rng[0], x_rng[1] + 1)
y_rng2 = range(y_rng[0], y_rng[1] + 1)
velocities = 0
for x in range(1, x_rng[1] + 1):
    for y in range(y_rng[0], -y_rng2[0]):
        passed = False
        x_vel = x
        y_vel = y
        curr_x = 0
        curr_y = 0
        while curr_x <= x_rng[1] and curr_y >= y_rng2[0]:
            curr_x += x_vel
            curr_y += y_vel
            x_vel -= (x_vel > 0)
            y_vel -= 1
            if curr_x in x_rng2 and curr_y in y_rng2:
                passed = True
                break
        if passed:
            velocities += 1
print(velocities)

from phi.flow import *
import matplotlib.pyplot as plt

plt.style.use("dark_background")

v = StaggeredGrid(
    values = lambda pos: vec(
        x = math.cos(pos).vector["x"] * math.sin(pos).vector["y"],
        y = math.sin(pos).vector["x"] * math.cos(pos).vector["y"]
    ),
    extrapolation=extrapolation.PERIODIC,
    x = 25,
    y = 25,
    bounds = Box(x = 2 * PI, y = 2 * PI)
)

# plot(v)
# plt.show() Plot showing the vector field at initial conditions

def make_step(v, dt = 0.1):                 # change dt to modify animation "fluidity"
    v = advect.semi_lagrangian(v, v, dt=dt)
    v = diffuse.implicit(v, 0.1, dt=dt)
    v, _ = fluid.make_incompressible(v)
    return v

trj = iterate(make_step, batch(time=40), v)
plot(trj, animate="time", size=(5, 5))
plt.show()

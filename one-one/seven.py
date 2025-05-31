import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 8)
y = np.linspace(-10, 10, 8)
z = np.linspace(-10, 10, 8)
X, Y, Z = np.meshgrid(x, y, z)

U = np.zeros_like(X)
V = np.zeros_like(Y)
W = X**2 + Y**2

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W, length=1, normalize=True, color='teal')

ax.set_title(r"$\vec{F}(x, y, z) = \langle 0,\ 0,\ x^2 + y^2 \rangle$")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.savefig("one-one/vector_field_3d.png", dpi=300, bbox_inches='tight')
plt.show()

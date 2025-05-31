import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 8)
y = np.linspace(-3, 3, 8)
z = np.linspace(-10, 10, 4)
X, Y, Z = np.meshgrid(x, y, z)

U = X + Y
V = X - Y
W = -Z

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")
ax.quiver(X, Y, Z, U, V, W, length=0.3, normalize=False, color="blue")
ax.set_title(r"$\vec{F}(x, y, z) = \langle x + y,\ x - y,\ -z \rangle$", fontsize=16)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)
ax.set_zlabel("z", fontsize=14)
ax.tick_params(labelsize=12)
ax.set_box_aspect([1, 1, 1])
plt.tight_layout()
plt.savefig("one-one/seven/vector_field_c.png", dpi=150, bbox_inches="tight")
plt.show()

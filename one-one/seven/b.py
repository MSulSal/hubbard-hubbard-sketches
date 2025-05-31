import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# Parameters
radii = np.linspace(0, 12, 4)
thetas = np.linspace(0, 2 * np.pi, 16, endpoint=False)
zs = np.linspace(-6, 6, 4)

R, T, Z = np.meshgrid(radii, thetas, zs, indexing='ij')
X = R * np.cos(T)
Y = R * np.sin(T)

U = Y
V = -X
W = -Z

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")
ax.quiver(X, Y, Z, U, V, W, length=0.2, normalize=False, color="blue", arrow_length_ratio=0.3)

ax.set_title(r"$\vec{F}(x, y, z) = \langle y,\ -x,\ -z \rangle$", fontsize=16)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)
ax.set_zlabel("z", fontsize=14)
ax.set_box_aspect([1, 1, 1])
ax.tick_params(labelsize=12)

plt.tight_layout()
plt.savefig("one-one/seven/images/vector_field_b.png", dpi=600, bbox_inches="tight")
plt.show()

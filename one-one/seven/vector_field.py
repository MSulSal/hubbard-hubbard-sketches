import numpy as np
import matplotlib.pyplot as plt

def vf_plot(url, fx=lambda x,y,z: 0, fy=lambda x,y,z: 0, fz=lambda x,y,z: 0, title="", length=0.05):
    r = np.linspace(0, 12, 4)
    t = np.linspace(0, 2 * np.pi, 16, endpoint=False)
    z = np.linspace(-12, 12, 3)

    R, T, Z = np.meshgrid(r, t, z, indexing="ij")
    X = R * np.cos(T)
    Y = R * np.sin(T)
    U = fx(X, Y, Z)
    V = fy(X, Y, Z)
    W = fz(X, Y, Z)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.quiver(X, Y, Z, U, V, W, length=length, normalize=False, color="blue", arrow_length_ratio=0.3)

    ax.set_title(title, fontsize=16)
    ax.set_xlabel("x", fontsize=14)
    ax.set_ylabel("y", fontsize=14)
    ax.set_zlabel("z", fontsize=14)
    ax.set_box_aspect([1, 1, 1])
    ax.tick_params(labelsize=12)

    plt.tight_layout()
    plt.savefig(f"one-one/seven/images/vector_field_{url}.png", dpi=600, bbox_inches="tight")
    plt.show()
from vector_field import vf_plot

vf_plot("a", fz=lambda x, y, z: x**2 + y**2, title=r"$\vec{F}(x, y, z) = \langle 0,\ 0,\ x^2 + y^2 \rangle$")
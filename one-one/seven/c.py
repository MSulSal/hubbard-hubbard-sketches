from vector_field import vf_plot

vf_plot(
    "c", 
    fx=lambda x,y,z: x + y, 
    fy=lambda x,y,z: x - y,
    fz=lambda x, y, z: -z, 
    title=r"$\vec{F}(x, y, z) = \langle x + y,\ x - y,\ -z \rangle$",
    length=0.2
)
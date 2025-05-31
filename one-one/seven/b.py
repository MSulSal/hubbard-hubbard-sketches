from vector_field import vf_plot

vf_plot(
    "b", 
    fx=lambda x,y,z: y, 
    fy=lambda x,y,z: -x,
    fz=lambda x, y, z: -z, 
    title=r"$\vec{F}(x, y, z) = \langle y,\ -x,\ -z \rangle$",
    length=0.2
)
import math

def sphere_volume(radius):
    """
    Compute the volume of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    if radius < 0:
        return "Invalid radius. Please provide a non-negative value."
    volume = (4 / 3) * math.pi * radius**3
    return volume

radius = float(input("Enter the radius of the sphere: "))
result = sphere_volume(radius)
print(f"Volume of the sphere with radius {radius:.2f} units: {result:.2f} cubic units")

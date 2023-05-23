"""
controller.py by Jeshua Gonzalez Valentin
functions to operatre the VolCube Calculator.
"""
# imports

# Functions
def get_volume(length: int, width: int, height: int) -> str:
    """ calculates Volume and returns results """
    results = ""
    volume = (length * width * height)
    results = f"You have a width of {width}, multiplyed"
    results += f" by a length of {length}, and a height of {height}."
    results += f" You have a volume of {volume} eu^3"
    return results

# Global scope
if __name__ == "__main__":
    results = get_volume(5, 5, 5)
    print(results)
    


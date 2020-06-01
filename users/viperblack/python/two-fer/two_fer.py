def two_fer(name = None):
    try:
        return "One for " + name + ", one for me."
    except:
        name = "you"
        raise ("No argument passed!")
    finally:
        return "One for " + name + ", one for me."
class Puppy:
    n_puppies = 0  # number of created puppies
    LIMIT = 10

    def __new__(cls):
        if cls.LIMIT > cls.n_puppies:
            cls.n_puppies += 1
            return object.__new__(cls)
    # define __new__

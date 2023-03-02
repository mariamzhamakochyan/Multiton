class Multiton:
    instances = {}
    max_instances = 3

    def __new__(cls, *args, **kwargs):
        if len(cls.instances) >= cls.max_instances:
            len(cls.instances) -=cls.max_instances
            return cls.instances[len(cls.instances)]
        else:
            instance = super().__new__(cls)
            cls.instances[len(cls.instances)] = instance
            return instance

    def __init__(self, *args, **kwargs):
        pass

instance1 = Multiton()
instance2 = Multiton()
instance3 = Multiton()
instance4 = Multiton()
instance5 = Multiton()
instance6 = Multiton()
instance7 = Multiton()

print(instance1 is instance4)
print(instance2 is instance5) 
print(instance1 is instance7) 

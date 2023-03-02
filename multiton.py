class Multiton:
    instances = {}
    max_instances = 3
    ref = 0

    def __new__(cls, *args, **kwargs):
        if len(cls.instances) < cls.max_instances:
            instance = super().__new__(cls)
            cls.instances[len(cls.instances)] = instance
            return instance
        else:
            cls.ref += 1
            if cls.ref > cls.max_instances:
                cls.ref = 0
                return cls.instances[cls.ref]
            return cls.instances[cls.ref - 1]            

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
print(instance3 is instance6) 
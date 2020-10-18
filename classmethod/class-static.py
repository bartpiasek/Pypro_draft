class ClassTest:
    """
    """
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_ethod of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method.")


# INSTANCE METHOD
# test = ClassTest()

# test.instance_method()
# ClassTest.instance_method(test)

# CLASS METHOD
# ClassTest.class_method()

# STATIC METHOD
# ClassTest.static_method()
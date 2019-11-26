# outsource
# I claim I can do this, I can do that
# When you ask me to do this/that, I secretly delegate(委托) to another person to do it for me.

class A:
    def spam(self, x):
        pass
    def foo(self):
        pass

class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        return getattr(self._a, name)


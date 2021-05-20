class A(object):
    def foo(self, x):
        print ("executing foo(%s, %s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print ("executing class_foo(%s, %s)" % (cls, x))

    @staticmethod
    def static_foo(cls, x):
        print ("executing static_foo(%s, %s)" % (cls,x))

a = A()

a.foo(1)         # 클래스에 대한 object와 변수출력(클래스에 대한 object로 class 함수에 접근)
a.class_foo(1)   # 클래스에 대한 object와 변수출력(클래스에 대한 object로 classmethod에 접근)
a.class_foo(1)   # 클래스에 대한 object와 변수출력(클래스명으로 classmethod에 접근)
a.static_foo(1)  # class method와 다르게 class argument로 접근 불가능
class A:
    super()
    print("I am A")
class B:
    super()
    print("I am B")
class C(A,B):
    super()
    print("I am C")

obj=C()

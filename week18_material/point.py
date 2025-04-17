class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return (f"Point({self.x}, {self.y}, {self.z})") # print the Point nicely

    def __eq__(self, o):
        if self is o:
            return True
        if not isinstance(o, Point):
            return False
        # Change this to properly compare two points
        return True

    def __hash__(self):
        return(hash(self.x), hash(self.y), hash(self.z))



def main():
    l = [Point(1,2,3), Point(0,0,0), Point(3, 2, 1), Point(1, 2, 3)]
    print("List:")
    for p in l:
        print(p)
    print()
    print("Set:")
    for p in set(l):
        print(p)
    print()
    print(f"Equality: {Point(1, 2, 3) == Point(1, 2, 3)}")
    

if __name__ == "__main__":
    main()

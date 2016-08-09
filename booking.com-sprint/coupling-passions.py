import math


class Destination:
    def __init__(self, name, guest_passions, latitude, longitude, passions):
        self.name = name
        self.guest_passions = guest_passions
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.passions = passions
        self.found_passions = set()
        self.found_passions = self.guest_passions.intersection(self.passions)

    def count_found_passions(self):
        return len(self.found_passions)

    def __str__(self):
        return self.name + " lat:" + str(self.latitude) + " long:" + str(self.longitude) + \
               " found:" + str(self.count_found_passions())


def distance_between(point1, point2):
    EARTH_RADIUS = 6371
    point1_lat_in_radians = math.radians(point1.latitude)
    point2_lat_in_radians = math.radians(point2.latitude)
    point1_long_in_radians = math.radians(point1.longitude)
    point2_long_in_radians = math.radians(point2.longitude)

    return math.acos(math.sin(point1_lat_in_radians) * math.sin(point2_lat_in_radians) +
                     math.cos(point1_lat_in_radians) * math.cos(point2_lat_in_radians) * math.cos(
                         point2_long_in_radians - point1_long_in_radians)) * EARTH_RADIUS


n = int(input())
passions = set()

for i in range(n):
    a = input().split()
    ar = a[1:]
    for x in ar:
        passions.add(x)

y = int(input())

destinition_list = []

for x in range(y):
    line = input().split()
    dest = Destination(line[0], passions, line[1], line[2], line[4:])
    if dest.count_found_passions() > 0:
        destinition_list.append(dest)

sorted_destinitions = sorted(destinition_list, key=lambda x: x.count_found_passions())

max_found = sorted_destinitions[len(sorted_destinitions) - 1].count_found_passions()

search_list = [sorted_destinitions.pop()]

while sorted_destinitions:
    element = sorted_destinitions.pop()
    search_list.append(element)
    if element.count_found_passions() < max_found:
        break

max_dist = distance_between(search_list[0], search_list[1])

a = search_list[0]
b = search_list[1]
_intersect = set(set(a.passions) | set(b.passions)) | passions

for x in range(len(search_list)):
    for y in range(x + 1, len(search_list)):
        dst = distance_between(search_list[x], search_list[y])
        __intersect = set(set(search_list[x].passions) | set(search_list[y].passions)) | passions
        if dst < max_dist and len(__intersect) > len(_intersect):
            max_dist = dst
            a = search_list[x]
            b = search_list[y]
            _intersect = __intersect

lst = sorted([a.name, b.name])
print(" ".join(lst))

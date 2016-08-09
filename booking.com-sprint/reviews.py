
class Review:
    def __init__(self, id, time, body):
        self.id = id
        self.time = time
        self.body = body
        self.score = 0
        self.calculate_rate()

    def calculate_rate(self):
        start_timestamp = 1465948800
        end_timestamp = 1468540800

        if start_timestamp <= self.time <= end_timestamp:
            self.score += 20
        else:
            self.score += 10

        if len(self.body) >= 100:
            self.score += 20
        else:
            self.score += 10

    def __str__(self):
        return str(self.id) + " " + str(self.score)


n, m = [int(x) for x in input().split()]



_passions = []
_reviews = []

for x in range(n):
    _passions.append(input())

for x in range(m):
    id, time = [int(x) for x in input().split()]
    body = input()
    review = Review(id, time, body)
    _reviews.append(review)


for x in _passions:
    _sortable_reviews = []
    for r in _reviews:
        if x.lower() in r.body.lower():
            _sortable_reviews.append(r)
    if _sortable_reviews:
        _sorted_reviews = sorted(_sortable_reviews, key=lambda q: q.score)
        _max_score = _sorted_reviews[len(_sorted_reviews) - 1].score
        __result_reviews = [_sortable_reviews.pop()]
        while _sorted_reviews:
            element =_sorted_reviews.pop()
            if element.score == _max_score:
                __result_reviews.append(element)
            else:
                break
        __result_sorted_reviews = sorted(__result_reviews, key=lambda q: q.id, reverse=True)
        print(__result_sorted_reviews.pop().id)
    else:
        print(-1)
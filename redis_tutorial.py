import redis

r = redis.Redis()

r.set("First", "example")
print(r.get("First"))

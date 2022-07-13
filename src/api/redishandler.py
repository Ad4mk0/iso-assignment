from redis import Redis


# host = "127.0.0.1:6379"
password = "KiwiLetsGo"
redis = Redis(host='redis', port=6379, db=0,
              password=f"{password}", decode_responses=True)

def is_occupied_redis():
    return redis.keys()!=[]


def set_to_redis(key, val):
    redis.set(key, val)


def get_set_from_redis(key):
    return redis.smembers(key)


def add_set_to_redis(key, vals):
    redis.sadd(key, *vals)


def intersection_set_input(key, vals):
    add_set_to_redis("TO_COMPARE", vals)
    res = redis.sinter("TO_COMPARE", key)
    redis.delete("TO_COMPARE")
    return res

# print(is_occupied_redis())
# print(add_set_to_redis('SK', {'Slovakia', 'Slovakiya', 'Slowakei'}))

# print(get_set_from_redis('SVK'))
# print(intersection_set_input(iso, input_list))

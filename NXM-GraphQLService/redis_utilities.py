# Redis operations 
# PUT / GET / DELETE
# 
import redis
import logging

class RedisUtilities:
    
    def __init__(self, sentinels, redis_master, redis_db):
        self.sentinels = sentinels
        self.redis_master = redis_master
        self.redis_db = redis_db
    
    # fetch data from redis
    # If no entry available, return None
    # 
    # The cache logic is supposed to be simple, no additional filtering
    # applied on top of the data. In other words, the cache is hit
    # only when full key match.
    #
    def get(self, access_key):

        master = self.sentinels.master_for(self.redis_master, socket_timeout=3, db=self.redis_db)
        cache_data = master.get(access_key)

        if (cache_data is None):
            return None
        else:
            logging.info('[cache-hit] - {}'.format(access_key))
            return cache_data.decode('utf-8')
    
    # push a key into the redis
    # set the default time to 5 minutes
    #
    def put(self, group, access_key, json):

        master = self.sentinels.master_for(self.redis_master, socket_timeout=3, db=self.redis_db)
        master.set(access_key, json, 60)
        
        # add the key to a grounp so that we don't have to do full scan
        # in redis key universe
        master.sadd(group, access_key)
        master.expire(group, 60)
    
    # delete all keys that match the given group
    #
    def delete_group(self, group):
        master = self.sentinels.master_for(self.redis_master, socket_timeout=3, db=self.redis_db)
        members = master.smembers(group)
        logging.info('delete {} redis keys in group [{}] ..'.format(str(len(members)), group))
        for mem in members:
            master.delete(mem)
        # also delete the group
        master.delete(group)

    # delete a single keys that match
    #
    def delete_key(self, group, access_key):
        master = self.sentinels.master_for(self.redis_master, socket_timeout=3, db=self.redis_db)
        master.srem(group, access_key)
        master.delete(access_key)
# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2022/3/28 16:43
from redis import RedisCluster
from redis.cluster import ClusterNode
from rq import Queue

nodes = [
    ClusterNode('localhost', 1379),
    ClusterNode('localhost', 2378),
    ClusterNode('localhost', 3378),
    ClusterNode('localhost', 4378),
    ClusterNode('localhost', 5378),
    ClusterNode('localhost', 6378),
]
redis_connect = RedisCluster(startup_nodes=nodes)
redis_connect.set('test', 'test')
print(redis_connect.get('test'))
queue = Queue(name='test', connection=redis_connect)
print(queue.job_ids)

# job = queue.enqueue('test')
# print(job.get_id())



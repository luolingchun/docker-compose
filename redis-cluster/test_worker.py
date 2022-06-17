# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2022/3/29 10:24
from redis import RedisCluster
from redis.cluster import ClusterNode
from rq import Queue, Worker

nodes = [
    ClusterNode('localhost', 1379),
    ClusterNode('localhost', 2378),
    ClusterNode('localhost', 3378),
    ClusterNode('localhost', 4378),
    ClusterNode('localhost', 5378),
    ClusterNode('localhost', 6378),
]
redis_connect = RedisCluster(startup_nodes=nodes)

worker = Worker(queues=['test'], connection=redis_connect)

worker.work(burst=True)

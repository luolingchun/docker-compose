redis-cli --cluster create \
  localhost:1379 \
  localhost:2379 \
  localhost:3379 \
  localhost:4379 \
  localhost:5379 \
  localhost:6379 \
  --cluster-replicas 1

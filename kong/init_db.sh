docker run -it --rm \
    --link kong-database:kong-database \
    --network kong_default \
    -e "KONG_DATABASE=postgres" \
    -e "KONG_PG_DATABASE=kong" \
    -e "KONG_PG_HOST=kong-database" \
    -e "KONG_PG_USER=kong_postgres_user" \
    -e "KONG_PG_PASSWORD=kong_postgres_password" \
    kong:2.2.1-ubuntu kong migrations bootstrap --v


docker run -it --rm \
    pantsel/konga:0.14.9 \
    -c prepare \
    -a postgres \
    -u postgresql://kong_postgres_user:kong_postgres_password@172.17.0.1:9002/konga
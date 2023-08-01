# скрипт для синхронизации проекта с БД

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

until PGPASSWORD=$DATABASES_PASSWORD psql -h "$host" -p "$port" -U "$DATABASES_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
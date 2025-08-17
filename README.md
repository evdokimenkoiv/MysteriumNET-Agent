# MysteriumNET-Agent

Простой агент, который регистрируется у менеджера и периодически отправляет heartbeat.

## Запуск
```bash
cp .env.example .env
# правим переменные:
# MANAGER_URL=http://<ip-менеджера>:8080
# MANAGER_SECRET=<секрет из менеджера>
# WALLET_ADDRESS=<ваш_кошелёк>
docker compose -f docker-compose.standalone.yml up -d --build
```

## Поведение
- При старте делает `POST /agents/register` на менеджере с заголовком `X-Manager-Secret`.
- Каждые 60 секунд повторяет регистрацию как heartbeat (обновляет last_seen).

# Pitada

App de receitas para a casa (2 pessoas): cadastro rápido por texto, link ou foto com extração por IA, busca por nome e ingrediente, despensa com "o que dá pra fazer" e lista de compras somada.

Status: F0 (fundação). Veja as fases e os critérios de pronto na especificação do MVP.

## Rodar localmente

Requisitos: Python 3.12+, Docker.

```bash
cp .env.example .env
make install     # cria .venv e instala as dependências
make up          # Postgres local (docker compose)
make migrate     # aplica as migrações
make run         # API em http://localhost:8000 (docs em /docs)
```

`make check` roda lint, tipos e testes, o mesmo que o CI.

## Estrutura

- `app/`: backend FastAPI, organizado em módulos (`app/modules/<nome>`).
- `migrations/`: Alembic.
- `web/`: frontend (a Prisma define o framework). O build estático é servido pelo FastAPI.
- `docs/adr/`: decisões de arquitetura.

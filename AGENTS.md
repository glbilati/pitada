# AGENTS.md

Comandos:
- `make install` instala; `make up` sobe o Postgres local; `make migrate` aplica migrações.
- `make check` (ruff, mypy strict, pytest) tem que passar antes de qualquer PR.

Regras que não dá para adivinhar lendo o código:
- Contrato primeiro: mudou endpoint ou schema, atualize o OpenAPI e avise a Prisma no PR antes de mexer em `web/`.
- Erros da API são sempre RFC 7807 (`application/problem+json`). Lista vazia responde 200, nunca 404.
- Toda tabela tem `household_id` e toda query filtra por ele.
- Conversões de unidade e cálculo de cobertura são funções puras, com teste. Sem I/O dentro delas.
- Segredos (chave da IA, `SESSION_SECRET`, `DATABASE_URL`) nunca no repositório.
- Mudou o esquema do banco: migração Alembic nova, nunca editar migração já aplicada.
- Não force push na `main`. Um PR pequeno por vez.

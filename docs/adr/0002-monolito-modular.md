# ADR-0002: Monólito modular, um container

Status: aceita (2026-11-23)

## Contexto

Dois usuários, um desenvolvedor. Microsserviços trariam custo operacional sem benefício.

## Decisão

- Um serviço FastAPI, um banco, um container. O FastAPI serve o front estático (`web/dist`): mesma origem, sem CORS.
- Código em módulos por domínio em `app/modules/<nome>` (hoje `health` e `auth`; depois `recipes`, `ingredients`, `pantry`, `shopping`, `extraction`). Cada módulo tem `router.py`, `schemas.py` e, quando houver, `models.py` e `service.py`.
- Regra de dependência: um módulo não importa o `models.py` de outro. Se precisar de dado alheio, chama o `service.py` dele.
- Regras de negócio puras (unidades, cobertura, soma da lista) ficam em funções sem I/O, testáveis sem banco.
- O contrato é o OpenAPI gerado pelo FastAPI. Ele vem antes das telas.

## Consequências

- Deploy e depuração simples.
- Se um módulo precisar escalar sozinho (improvável aqui), a fronteira já está desenhada.

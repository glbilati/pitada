import json
from pathlib import Path

from app.main import app

CONTRACT = Path(__file__).resolve().parent.parent / "docs" / "openapi.json"


def test_openapi_contract_is_up_to_date() -> None:
    """O contrato versionado e o que a Prisma consome. Mudou a API? Rode `make openapi`."""
    committed = json.loads(CONTRACT.read_text(encoding="utf-8"))
    assert committed == json.loads(json.dumps(app.openapi()))

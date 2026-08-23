import os

os.environ["JWT_SECRET_KEY"] = "test-secret-key"

import pytest
from fastapi.testclient import TestClient

from app.auth.dependencies import get_current_user_id
from app.main import app


@pytest.fixture
def client():
    app.dependency_overrides[get_current_user_id] = lambda: 1

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()

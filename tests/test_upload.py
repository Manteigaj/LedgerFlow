from unittest.mock import patch

from fastapi.testclient import TestClient


def test_upload_csv(client: TestClient):
    csv_content = "date,description,amount\n2026-08-20,Market,100.50\n"

    with patch("app.routes.upload.process_csv.delay") as mock_task:
        response = client.post(
            "/upload/csv",
            files={
                "file": (
                    "transactions.csv",
                    csv_content,
                    "text/csv",
                )
            },
        )

    assert response.status_code == 200

    assert response.json() == {
        "message": "File sent for processing.",
        "quantity": 0,
    }

    mock_task.assert_called_once_with(
        csv_content,
        1,
    )

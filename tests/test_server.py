from vulndify_mcp_server.server import SERVER_NAME, hello, mcp


def test_hello_returns_expected_value() -> None:
    assert hello() == "hello"


def test_server_has_expected_name() -> None:
    assert SERVER_NAME == "vulndify-demo"
    assert mcp.name == SERVER_NAME

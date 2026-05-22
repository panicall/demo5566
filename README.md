# vulndify-mcp-server

一个最小可运行的 MCP Server 示例项目，基于官方 Python SDK `mcp` 构建，并暴露一个演示用 tool:

- tool 名称: `hello`
- 调用结果: 直接返回字符串 `hello`

这个项目已经包含:

- Python 包结构
- MCP Server 入口
- 可发布到 PyPI 的 `pyproject.toml`
- 基础测试
- 本地开发和打包说明

## 目录结构

```text
.
├── pyproject.toml
├── README.md
├── LICENSE
├── src
│   └── vulndify_mcp_server
│       ├── __init__.py
│       ├── __main__.py
│       └── server.py
└── tests
    └── test_server.py
```

## 本地安装

建议先创建虚拟环境，然后安装本项目:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## 启动服务

安装后可以直接通过命令行启动:

```bash
vulndify-mcp-server
```

也可以用模块方式启动:

```bash
python -m vulndify_mcp_server
```

服务默认通过 stdio 方式运行，适合被 MCP Client 拉起。

## 核心代码示例

`hello` tool 定义在 `src/vulndify_mcp_server/server.py` 中，调用时直接返回固定字符串:

```python
@mcp.tool(name="hello")
def hello_tool() -> str:
    return "hello"
```

## 开发测试

运行测试:

```bash
pytest
```

构建发布包:

```bash
python -m build
```

检查发布产物:

```bash
twine check dist/*
```

## 发布到 PyPI

正式发布前，建议先修改 `pyproject.toml` 中的以下字段:

- `name`
- `version`
- `description`
- `license`
- `authors`
- `urls`

然后执行:

```bash
python -m build
python -m twine upload dist/*
```

如果要先发布到 TestPyPI:

```bash
python -m twine upload --repository testpypi dist/*
```

## 后续可扩展方向

- 增加更多 tools
- 添加 resources / prompts
- 增加 CI 工作流
- 添加 lint 和类型检查
- 接入真实业务逻辑

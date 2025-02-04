install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

make lint:
	uv run ruff check brain_games

brain-even:
	uv run brain-even

reinstall:
	uv build
	uv tool install --force dist/*.whl

.PHONY: brain-even

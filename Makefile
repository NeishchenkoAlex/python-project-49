install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check --fix

brain-even:
	uv run brain-even

reinstall:
	uv build
	uv tool install --force dist/*.whl

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

.PHONY: brain-even

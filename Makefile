.PHONY: help clear clean run test install

# Переменные
PYTHON = python3
APP_DIR = app
SNAKES_DIR = $(APP_DIR)/snakes

help:
	@echo "Доступные команды:"
	@echo "  make clear    - Очистить кеш Python и временные файлы"
	@echo "  make clean    - Полная очистка (включая .pyc и __pycache__)"
	@echo "  make run      - Запустить приложение"
	@echo "  make test     - Запустить тесты"
	@echo "  make install  - Установить зависимости"

clear:
	@echo "Очистка кеша Python..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type f -name "*.so" -delete 2>/dev/null || true
	@echo "Очистка временных файлов..."
	@rm -rf /tmp/training-snakes* 2>/dev/null || true
	@echo "Готово!"

clean: clear
	@echo "Полная очистка..."
	@rm -rf .pytest_cache 2>/dev/null || true
	@rm -rf .coverage 2>/dev/null || true
	@rm -rf htmlcov 2>/dev/null || true
	@rm -rf dist build *.egg-info 2>/dev/null || true
	@echo "Готово!"

run:
	@echo "Запуск приложения..."
	gunicorn --bind 0.0.0.0:8081  'app.main:app'

test:
	@echo "Запуск тестов..."
	@$(PYTHON) -m pytest $(APP_DIR)/ -v

install:
	@echo "Установка зависимостей..."
	@pip install -r requirements.txt

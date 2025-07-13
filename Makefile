.PHONY: tests
test:
	@echo "Running tests..."
	@cd hospital-be && python -m pytest && cd ..
	@echo "Tests completed."
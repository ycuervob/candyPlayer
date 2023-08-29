NODE = node
HTTP_SERVER = http-server
GAME_DIR = Game
PORT = 3006

BOLD = \032[1m
GREEN = \033[32m
RESET = \033[0m
GREEN = \033[32m
RED = \033[31m

.PHONY: start

default: 
	@echo "$(GREEN)Makefile para ejecutar http-server en la carpeta Game$(GREEN)"
	@echo "$(GREEN)-----------------------------------------------------------$(GREEN)"
	@echo "$(GREEN)Comandos y opciones$(RESET)"
	@echo "$(RED)make start ->$(RESET) Inicia el servidor en el puerto $(PORT)"

start:
	@echo "Iniciando http-server en el puerto $(PORT)..."
	$(HTTP_SERVER) $(GAME_DIR) -p $(PORT)


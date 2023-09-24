NODE = node
NPM = npm
HTTP_SERVER = http-server
GAME_DIR = Game
PORT = 3006

BOLD = \032[1m
GREEN = \033[32m
RESET = \033[0m
GREEN = \033[32m
RED = \033[31m

.PHONY: start install-http-server install-winapi-linux

default: 
	@echo "$(GREEN)Makefile para ejecutar http-server en la carpeta Game$(GREEN)"
	@echo "$(GREEN)-----------------------------------------------------------$(GREEN)"
	@echo "$(GREEN)Comandos y opciones$(RESET)"
	@echo "$(RED)make start ->$(RESET) Inicia el servidor en el puerto $(PORT)"

install-http-server:
	@echo "$(GREEN)Instalando http-server...$(RESET)"
	$(NODE) -v
	sudo $(NPM) -g install http-server

start:
#@read -p "Presione [Y] para instalar http-server: " REPLY && if [ "$$REPLY" = "y" ] || [ "$$REPLY" = "Y" ]; then make install-http-server; fi
	@echo "Iniciando http-server en el puerto $(PORT)..."
	$(HTTP_SERVER) $(GAME_DIR) -p $(PORT)


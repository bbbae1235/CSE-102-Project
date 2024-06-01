PYTHON = python3
# Source files
SRC = MWST.py

# Executable name
EXEC = MWST

# Default target
all: $(EXEC)

# Rule to create an executable script
$(EXEC): $(SRC)
	@echo "#!/bin/bash" > $(EXEC)	
	@echo "$(PYTHON) $(SRC) \"\$$@\"" >> $(EXEC)	
	@chmod +x $(EXEC)	

# Clean up
clean:
	@rm -f $(EXEC)	

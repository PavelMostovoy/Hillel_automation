import logging

logging.basicConfig(filename="data.log",
                    level=logging.ERROR,
                    format='%(asctime)s - $(name) '
                           ' - %(levelname)s - %(message)s')
logger = logging.getLogger("Our logger")

file_name = "example.txt"
try:
    with open(file_name, "r") as f:
        logger.info(f"File {file_name} successfully opened")
        data = f.read()
        if data:
            logger.debug(
                f" Data has been successfully read from file {file_name}")
        else:
            logger.debug(
                    f" Data has not been  read from file {file_name}")
except FileNotFoundError:
    logger.error(f"File with name {file_name} not found")

    with open(file_name, "w") as f:
        logger.warning(f"File with name {file_name} was crated")

    data = "inside file"

print(data)

#
# logger.debug("Debug ")
# logger.info("Info  ")
# logger.warning("Warn ")
# logger.error("Error ")
# logger.critical("Critical ")
#

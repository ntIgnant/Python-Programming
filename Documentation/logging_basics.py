import logging # python standard library

logging.basicConfig(level=logging.INFO, filename="myLogs.log") # this can also be logging.INFO | The logs will me writen in 'myLogs.log'
# In the basic configuration for the logging, the level is the minimum level of 'error' that needs to be tracked in the log file

# Logging Hierarchy: DEBUG < INFO < WARNING < ERROR < CRITICAL

userNum1 = int(input("Enter a Number: "))
logging.debug("Debug message (for devs mainly)")

userNum2 = int(input("Enter another Number: "))
logging.info("Some information message")

logging.warning("Some warning message")

logging.error("Some error happens here, but the code still runs")

logging.critical("This basically means that the code got fucked here")

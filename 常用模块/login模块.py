import logging



LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"   #日志格式
DATE_FORMAT = "%m-%d-%Y %H:%M:%S %p"             #设置时间格式
logging.basicConfig(level=logging.DEBUG,filename='my.log',datefmt=DATE_FORMAT,format=LOG_FORMAT)


#创建日志记录  日志级别从左往右依次减弱:DEBUG < INFO < WARNING < ERROR < CRITICAL
logging.debug('this is a debug!....')  #	最详细的日志信息，典型应用场景是 问题诊断
logging.info('this is a info!....') #信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
logging.warning('this is a warning!....') #当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
logging.error('this is a error!....')  #由于一个更严重的问题导致某些功能不能正常运行时记录的信息
logging.critical('this is a critical!....')  #当发生严重错误，导致应用程序不能继续运行时记录的信息

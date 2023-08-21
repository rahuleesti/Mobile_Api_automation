import inspect
import logging


class Utils:

    def custom_logger(loglevel=logging.DEBUG):
        """

        :rtype: object
        :param loglevel:
        :return:
        """
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        fh = logging.FileHandler("automation.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name) - %(message)s',
                                      datefmt='%m/%d/%y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

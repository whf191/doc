#coding=utf-8
import logging
def log_jilu(filename='/root/celerys/logcaiji.log',info=None,warning=None,critical=None):
    logging.basicConfig(format='%(levelname)s  %(asctime)s %(message)s  ', filename=filename, level=logging.DEBUG,filemode='w')
    if info:
        logging.info(info)
    elif warning:
        logging.warning(warning)
    elif critical:
        logging.critical(critical)


if __name__ == '__main__':

    log_jilu(info="标准输出")
    log_jilu(warning="错误输出")


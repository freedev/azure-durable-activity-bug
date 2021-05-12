import logging
import azure.functions as func

def main(name: str, outmsg: func.Out[str]) -> str:
    logging.info("====+"*100)
    logging.info(name)
    logging.info("====+"*100)
    outmsg.set(name)
    return f"Ok"

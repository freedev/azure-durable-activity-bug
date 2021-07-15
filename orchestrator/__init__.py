
import logging
import json

import azure.functions as func
import azure.durable_functions as df

log = logging.getLogger()

def orchestrator_function(context: df.DurableOrchestrationContext):
    try:
        str_input = context.get_input()
        msg = json.loads(str_input)
        log.info('message received')
        result1 = yield context.call_activity('send_similarity', json.dumps(msg))
        return [result1]
    except Exception:
        log.exception('orchestrator_function')
    return []

main = df.Orchestrator.create(orchestrator_function)

import logging
import json
import azure.functions as func
import os
import azure.durable_functions as df

async def function_handler(message: func.ServiceBusMessage, starter: str):
    for msg in [message]:
        client = df.DurableOrchestrationClient(starter)
        message_body = msg.get_body().decode("utf-8")

        # Log the Service Bus Message as plaintext
        #dictionary
        msg = json.loads(message_body)

        instance_id = await client.start_new('orchestrator', None, json.dumps({ 'moco' : 'A', 'attrib': 'a' }))
        instance_id = await client.start_new('orchestrator', None, json.dumps({ 'moco' : 'B', 'attrib': 'b' }))


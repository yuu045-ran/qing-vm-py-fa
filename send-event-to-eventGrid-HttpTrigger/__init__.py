import logging
import azure.functions as func
import datetime

def main(req: func.HttpRequest, outputEvent: func.Out[func.EventGridOutputEvent]) -> None:

 #   logging.log("eventGridEvent: ", eventGridEvent)

    outputEvent.set(
        func.EventGridOutputEvent(
            id="test-id",
            data={"tag1": "value1", "tag2": "value2"},
            subject="test-subject",
            event_type="test-event-1",
            event_time=datetime.datetime.utcnow(),
            data_version="1.0"))
import datetime
import json


class SerializeJson(object):

    def __init__(self):
        pass

    def todo(self):
        """
        serialize and deserialize json or dict?
        https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable?page=1&tab=active#tab-top
        """
        # sort events with eventid using datetime string
        pass

    def serialize_dirty(self):
        """
        json.dumps(my_dictionary, indent=4, sort_keys=True, default=str)
         quick & dirty JSON dump that eats dates and everything
        """
        pass

    def serialize2(self, obj):
        json.dumps(datetime.datetime.now(), default=self.json_serial2)

    def json_serial2(self, obj):
        """
        JSON serializer for objects not serializable by default json code
        """
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        raise TypeError("Type %s not serializable" % type(obj))

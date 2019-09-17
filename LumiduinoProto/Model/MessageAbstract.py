import json

class MessageAbstract(object):
    def __init__(self, messagebytes):
        try:
            self.command_json = json.dumps(messagebytes)
            self.command_int = self.command_json['cmd']
            self.errors = self.command_json['err']
            self.body = self.command_json['body']
        except Exception as err:
            print(err)
            raise(Exception("Message {} is not a valid command".format(
                messagebytes
            )))

    def serialize(self):
        return ""

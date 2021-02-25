import json

from flask import Response


class Controller:

    @classmethod
    def response(cls, res, status_code):
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=status_code
        )

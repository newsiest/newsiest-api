from flask import jsonify


class ResponseFormatter:

    @staticmethod
    def get_paginated(data=[], status_code=200, limit=10, offset=0):
        resp = {
            "pagination": {
                "limit": limit,
                "offset": offset,
                "total_size": len(data)
            },
            "results": data[offset:offset + limit]
        }
        return jsonify(resp), status_code, {'Content-Type': 'application/json'}


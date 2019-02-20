class QueryGenerator:
    def __init__(self, optDict):
        self.optDict = optDict
        print(optDict)

    def generate(self):
        return "SELECT * FROM rw_service_mst"

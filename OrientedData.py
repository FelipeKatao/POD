import json 

class OrientedData:
    def __init__(self):
        self.Rules = []

    def CreateNewRule(self,RuleOd:str,fileOd:str):
        with open(fileOd,'r') as file:
            data = json.load(file)
        self.Rules.append(data["Rules"][RuleOd])
        
import json 

class OrientedData:
    def __init__(self):
        self.Rules = {}

    def CreateNewRule(self,RuleOd:str,fileOd:str):
        with open(fileOd,'r') as file:
            data = json.load(file)
        self.Rules[RuleOd] = data["Rules"][RuleOd]

    def CommandRule(self,Rule:str,DataInject:list,Callback=False):
        RuleData = self.Rules[Rule]["command"]
        RuleElse = self.Rules[Rule]["elsecommand"]
        for i in DataInject:
            i = str(i)
            if "==" in RuleData: 
                if  i == RuleData.split("==")[1].replace(" ",""):
                    print(self.Rules[Rule]["action"])
                    continue
                if Callback == True:
                    if  i == self.Rules[Rule]["elsecommand"].split("==")[1].replace(" ",""):
                        print(self.Rules[Rule]["elseaction"])
                    else:
                        print(i)
                else:
                    self.CommandRule(Rule,[i],True)



        
import json 

class OrientedData:
    def __init__(self,origin):
        self.Rules = {}
        self.Origin = origin
        self.Results = []

    def CreateNewRule(self,RuleOd:str,fileOd:str):
        with open(fileOd,'r') as file:
            data = json.load(file)
        self.Rules[RuleOd] = data["Rules"][RuleOd]

    def CommandRule(self,Rule:str,DataInject:list,Callback=False):
        RuleData = self.Rules[Rule]["command"]
        for i in DataInject:
            i = str(i)
            if "==" in RuleData: 
                if  i == RuleData.split("==")[1]:
                    if "()" in self.Rules[Rule]["action"]:
                        self.__CallFunctions(Rule,i)
                    self.Results.append(self.Rules[Rule]["action"])

                elif Callback == True:
                    if  i == self.Rules[Rule]["elsecommand"].split("==")[1]:
                        if "()" in self.Rules[Rule]["elseaction"]:
                            self.__CallFunctions(Rule,i)
                        self.Results.append(self.Rules[Rule]["elseaction"])

            if ">=" in RuleData: 
                if  int(i) >= int(RuleData.split(">=")[1]):
                    if "()" in self.Rules[Rule]["action"]:
                        self.__CallFunctions(Rule,i)
                    self.Results.append(self.Rules[Rule]["action"])

                elif Callback == True:
                    if  int(i) >= int(self.Rules[Rule]["elsecommand"].split(">=")[1]):
                        if "()" in self.Rules[Rule]["elseaction"]:
                            self.__CallFunctions(Rule,i)
                        self.Results.append(self.Rules[Rule]["elseaction"])


                elif not Callback:
                    self.CommandRule(Rule,[i],True)
        return self.Results


    def __CallFunctions(self,Rule,i):
        met = getattr(self.Origin,self.Rules[Rule]["action"].replace("()",""))
        met(i)
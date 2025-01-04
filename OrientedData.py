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
        Comand = "command"
        Action_ = "action"
        if Callback == True:
            Comand = "elsecommand"
            Action_ =  "elseaction"
        RuleData = self.Rules[Rule][Comand]
        for i in DataInject:

            i = str(i)
            
            if "==" in RuleData: 
                if  i == RuleData.split("==")[1]:
                    if "()" in self.Rules[Rule][Action_]:
                        self.__CallFunctions(Rule,i)
                    self.Results.append(self.Rules[Rule][Action_])
                else:
                    self.CommandRule(Rule,[i],True)


            if ">=" in RuleData: 
                if  int(i) >= int(RuleData.split(">=")[1]):
                    if "()" in self.Rules[Rule][Action_]:
                        self.__CallFunctions(Rule,i)
                    self.Results.append(self.Rules[Rule][Action_])
                else:
                    self.CommandRule(Rule,[i],True)

            if ">" in RuleData and not "=" in RuleData: 
                if  int(i) > int(RuleData.split(">")[1]):
                    if "()" in self.Rules[Rule][Action_]:
                        self.__CallFunctions(Rule,i)
                    self.Results.append(self.Rules[Rule][Action_])
                else:
                    self.CommandRule(Rule,[i],True)

            if "<=" in RuleData: 
                if  int(i) <= int(RuleData.split("<=")[1]):
                    if "()" in self.Rules[Rule][Action_]:
                        self.__CallFunctions(Rule,i)
                    self.Results.append(self.Rules[Rule][Action_])
                else:
                    self.CommandRule(Rule,[i],True)


            if "<" in RuleData and not "=" in RuleData: 
                if  int(i) < int(RuleData.split("<")[1]):
                    if "()" in self.Rules[Rule][Action_]:
                        self.__CallFunctions(Rule,i)
                    self.Results.append(self.Rules[Rule][Action_])
                else:
                    self.CommandRule(Rule,[i],True)

            
            if "!=" in RuleData: 
                if  i != RuleData.split("!=")[1]:
                    if "()" in self.Rules[Rule][Action_]:
                        self.__CallFunctions(Rule,i)
                    self.Results.append(self.Rules[Rule][Action_])
                else:
                    self.CommandRule(Rule,[i],True)


            # else not Callback:
            #         self.CommandRule(Rule,[i],True)
        return self.Results


    def __CallFunctions(self,Rule,i):
        met = getattr(self.Origin,self.Rules[Rule]["action"].replace("()",""))
        met(i)
class employee:
    def __init__(self):
        self.id=123
        self.salary=500000
        self.designation='SDE'
    def travel(self, designation):
        print(f"The person in travelling to {designation}")
sam=employee()

sam.travel("earth")
print(type(sam))
class CSP:
    def __init__(self, variables, domains):
        self.variables = variables      
        self.domains = domains             
        self.constraints = {}               

        for variable in variables:
            self.constraints[variable] = []

    # def add_constraint(self, var1, var2, constraint_func):  #Add a binary constraint between var1 and var2
        
    #     self.constraints[var1].append((var2, constraint_func(var1,var2)))
    #     self.constraints[var2].append((var1, constraint_func(var2, var1)))

    # def is_valid(self, assignment, var, value): #Check if assigning value to var is valid with current assignment
        
    #     for (neighbor, constraint) in self.constraints[var]:
    #         if neighbor in assignment and not constraint:
    #             return False
    #     return True

    def add_constraint(self, var1, var2, constraint_func):
        # Add a binary constraint between var1 and var2
        self.constraints[var1].append((var2, constraint_func))
        self.constraints[var2].append((var1, lambda x, y : constraint_func(y,x)))

    def is_valid(self, assignment, var, value):
        # Check if assigning value to var is valid with current assignment
        for (neighbor, constraint) in self.constraints[var]:
            if neighbor in assignment and not constraint(value, assignment[neighbor]):
                return False
        return True

    def backtrack(self, assignment=None):  #Basic backtracking algorithm
        if assignment == None:
            assignment = {}

        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]
        for value in self.domains[first]:
            # print ("backtrack classes: ",  value[0])
            # print(value[1])
            if self.is_valid(assignment, first, value):
                local_assignment = assignment.copy()
                local_assignment[first] = value
                result = self.backtrack(local_assignment)
                if result is not None:
                     return result
        return None
    


    

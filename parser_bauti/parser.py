VN = {'Program', 'Block', 'ConstDecl', 'ConstAssigList', 'ConstAssigListAux', 'VarDecl', 'IdList', 
      'IdListAux', 'ProcDecl', 'ProcDeclAux', 'Statement', 'StatementList', 'StatementListAux', 
      'Condition', 'Relation', 'Expression', 'ExpressionAux', 'SumOperator', 'Term', 'TermAux', 
      'MultOperator', 'Factor'}

VT = {'if', 'then', 'call', 'begin', 'end', 'while', 'do', 'odd', 'const', 'var', 'comparation', 
      'assign', 'procedure', 'id', 'operation', '#', 'num', ',', ';', '(', ')', 'EOF'}

P = {}

M = {'if':{'Program': ['Block', '#'], 
           'Block': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'], 
           'ConstDecl':[], 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': [], 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': ['ProcDeclAux'], 
           'ProcDeclAux': [], 
           'Statement':['if', 'Condition', 'then', 'Statement'], 
           'StatementList': ['Statement', 'StatementListAux'], 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term':None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor':None},
      'then':{'Program': None, 
           'Block': None, 
           'ConstDecl':None, 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement':None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': [], 
           'SumOperator': None, 
           'Term':None, 
           'TermAux': [], 
           'MultOperator': None, 
           'Factor':None},
      'call':{'Program': ['Block', '#'], 
           'Block': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'], 
           'ConstDecl':[], 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': [], 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': ['ProcDeclAux'], 
           'ProcDeclAux': [], 
           'Statement':['call', 'id'], 
           'StatementList': ['Statement', 'StatementListAux'], 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term':None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor':None},
      'begin':{'Program': ['Block', '#'], 
           'Block': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'], 
           'ConstDecl':[], 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': [], 
           'IdList': None,
           'IdListAux': None,
           'ProcDecl': ['ProcDeclAux'], 
           'ProcDeclAux': [], 
           'Statement':['begin', 'StatementList', 'end'], 
           'StatementList': ['Statement', 'StatementListAux'], 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term':None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor':None},
      'end':{'Program': None, 
           'Block': None, 
           'ConstDecl': None,
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None,
           'IdList': None,
           'IdListAux': None,
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': ['Statement', 'StatementListAux'], 
           'StatementListAux': [],
           'Condition': None,
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term':None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor':None},
      'while':{'Program': ['Block', '#'], 
           'Block': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'], 
           'ConstDecl':[], 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': [], 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': ['ProcDeclAux'], 
           'ProcDeclAux': [], 
           'Statement':['while', 'Condition', 'do', 'Statement'], 
           'StatementList': ['Statement', 'StatementListAux'], 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term':None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor':None},
      'odd':{'Program': None, 
           'Block': None, 
           'ConstDecl': None, 
           'ConstAssigList': None, 
           'ConstAssigListAux': None,
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': ['odd', 'Expression'], 
           'Relation': None,
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term':None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor':None},
      'const':{'Program': ['Block', '#'], 
           'Block': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'], 
           'ConstDecl':['const', 'ConstAssignList', ';'], 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term':None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor': None},
      'var':{'Program': ['Block', '#'], 
           'Block': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'], 
           'ConstDecl':[], 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': ['var', 'IdList', ';'], 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term': None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor':None},
      'comparation':{'Program': None, 
           'Block': None, 
           'ConstDecl':None, 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term': None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor':None},
      'assign':{'Program': None, 
           'Block': None, 
           'ConstDecl':None, 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term': None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor':None},
      'procedure':{'Program': ['Block', '#'], 
           'Block': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'], 
           'ConstDecl':[], 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': [], 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': ['ProcDeclAux'], 
           'ProcDeclAux': ['procedure', 'id', ';', 'Block', ';', 'ProcDeclAux'], 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term':None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor':None},
      'id':{'Program': ['Block', '#'], 
           'Block': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'], 
           'ConstDecl':[], 
           'ConstAssigList': ['id', '=', 'num', 'ConstAssignListAux'], 
           'ConstAssigListAux': ['id', '=', 'num', 'ConstAssignListAux'], 
           'VarDecl': [], 
           'IdList': ['id', 'IdListAux'],
           'IdListAux': None,
           'ProcDecl': ['ProcDeclAux'], 
           'ProcDeclAux': [], 
           'Statement':['id', ':=', 'Espression'], 
           'StatementList': ['Statement', 'StatementListAux'], 
           'StatementListAux': None,
           'Condition': ['Expression', 'Relation', 'Expression'], 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': ['Term', 'ExpressionAux'], 
           'SumOperator': None, 
           'Term': ['Factor', 'TermAux'], 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor': ['id']},
      'operation':{'Program': None, 
           'Block': None, 
           'ConstDecl':None, 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term': None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor': None},
      '#':{'Program': ['Block', '#'], 
           'Block': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'], 
           'ConstDecl': [], 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': [], 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': ['ProcDeclAux'], 
           'ProcDeclAux': [], 
           'Statement': [], 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': [], 
           'SumOperator': None, 
           'Term': None, 
           'TermAux': [], 
           'MultOperator': None, 
           'Factor': None},
      'num':{'Program': None, 
           'Block': None, 
           'ConstDecl':None, 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': ['Expression', 'Relation', 'Expression'], 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': ['Term', 'ExpressionAux'], 
           'SumOperator': None, 
           'Term': ['Factor', 'TermAux'], 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor': ['num']},
      ',':{'Program': None, 
           'Block': None, 
           'ConstDecl':None, 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': [',', 'id', 'IdListAux'], 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term': None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor': None},
      ';':{'Program': None, 
           'Block': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'], 
           'ConstDecl':[], 
           'ConstAssigList': None, 
           'ConstAssigListAux': [], 
           'VarDecl': [], 
           'IdList': None,
           'IdListAux': [], 
           'ProcDecl': ['ProcDeclAux'], 
           'ProcDeclAux': [], 
           'Statement': [], 
           'StatementList': ['Statement', 'StatementListAux'], 
           'StatementListAux': [';', 'Statement', 'StatementListAux'],
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': [], 
           'SumOperator': None, 
           'Term': None, 
           'TermAux': [], 
           'MultOperator': None, 
           'Factor': None},
      '()':{'Program': None, 
           'Block': None, 
           'ConstDecl':None, 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': ['Expression', 'Relation', 'Expression'], 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': ['Term', 'ExpressionAux'], 
           'SumOperator': None, 
           'Term': ['Factor', 'TermAux'], 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor': ['(', 'Expression', ')']},
      ')':{'Program': None, 
           'Block': None, 
           'ConstDecl':None, 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': [], 
           'SumOperator': None, 
           'Term': None, 
           'TermAux': [], 
           'MultOperator': None, 
           'Factor': None},
      'EOF':{'Program': None, 
           'Block': None, 
           'ConstDecl':None, 
           'ConstAssigList': None, 
           'ConstAssigListAux': None, 
           'VarDecl': None, 
           'IdList': None,
           'IdListAux': None, 
           'ProcDecl': None, 
           'ProcDeclAux': None, 
           'Statement': None, 
           'StatementList': None, 
           'StatementListAux': None,
           'Condition': None, 
           'Relation': None, 
           'Expression': None, 
           'ExpressionAux': None, 
           'SumOperator': None, 
           'Term': None, 
           'TermAux': None, 
           'MultOperator': None, 
           'Factor': None}
      }


def parser(string):
    stack = ['Program', 'EOF']
    counter = 0
    top = stack[0]
    t = string[counter]
    error = False
    while not(counter >= len(string)-1) and not(error):
      if top in VT:
            if top == t:
                  stack.pop(0)
                  counter += 1
                  t = string[counter]
            else:
                  error = True
      elif top in VN:
            if M[t][top] != None:
                  stack.pop(0)
                  stack = M[t][top] + stack
            else:
                  error = True
      else:
           error = True
           
    if error:
      print('La cadena NO pertence al lenguaje')
      return None
    else:
      print('La cadena SI pertenece al lenguaje')
      return None
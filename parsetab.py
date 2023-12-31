
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BEGIN COLON COMMA COMMENT DECIMAL DECLARE DIVIDE DO DOT DOUBLEGREATER DOUBLELESS ELSE END EQUAL FOR GREATER GREATEREQUAL ID IF INTEGER INTERROGATION LESS LESSEQUAL LESSGREATER LITERAL LPAREN MINUS MOD MULTI NOT NUMBER OR PLUS PROGRAM READ RPAREN SEMICOLON THEN TO TRIPLEGREATER TRIPLELESS WHILE WRITEprogram : PROGRAM ID bodybody : DECLARE declaration_list BEGIN statement_list ENDdeclaration_list : declaration SEMICOLON declaration_list_auxdeclaration_list_aux : declaration_list\n                            | emptydeclaration : type identifier_listidentifier_list : ID identifier_list_auxidentifier_list_aux : COMMA identifier_list\n                            | empty type : INTEGER \n                | DECIMALstatement_list : statement SEMICOLON statement_prime\n\n                         statement_prime : statement_list\n                            | emptystatement : assign_statement\n                    | if_statement\n                    | while_statement\n                    | for_statement\n                    | read_statement\n                    | write_statement\n                    | do_while_statement\n                    assign_statement : ID ASSIGN expressionif_statement : IF condition THEN statement_list if_statement_auxif_statement_aux : END\n                        | ELSE statement_list ENDwhile_statement : WHILE condition DO statement_list ENDdo_while_statement : DO statement_list do_while_statement_suffixdo_while_statement_suffix : WHILE conditionfor_statement : FOR assign_statement TO condition DO statement_list ENDread_statement : READ LPAREN ID RPARENwrite_statement : WRITE LPAREN writable RPARENwritable : simple_expression\n                        | literalcondition : expressionexpression : simple_expression expression_auxexpression_aux : relop simple_expression\n                    | emptyrelop : EQUAL \n                | LESS \n                | LESSEQUAL \n                | GREATER \n                | GREATEREQUAL \n                | LESSGREATERpar_expression : LPAREN expression RPARENsimple_expression : term\n                            | par_expression INTERROGATION simple_expression COLON simple_expression\n                            | simple_expression addop term\n                       addop : PLUS \n                | MINUS \n                | ORmulop : MULTI \n                | DIVIDE \n                | MOD \n                | ANDterm : factor_a\n                | term mulop factor_afactor_a : factor \n                | NOT factor \n                | MINUS factorfactor : ID \n                | NUMBER \n                | par_expressionliteral : LITERALempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,4,37,],[0,-1,-2,]),'ID':([2,8,9,10,11,25,26,27,28,35,38,39,46,48,49,55,56,62,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,88,89,108,109,111,],[3,14,-10,-11,24,50,50,24,24,14,24,50,50,50,50,90,50,24,50,50,-48,-49,-50,-38,-39,-40,-41,-42,-43,50,-51,-52,-53,-54,50,24,50,50,24,50,24,]),'DECLARE':([3,],[5,]),'INTEGER':([5,12,],[9,9,]),'DECIMAL':([5,12,],[10,10,]),'BEGIN':([6,12,31,32,33,],[11,-64,-3,-4,-5,]),'SEMICOLON':([7,13,14,16,17,18,19,20,21,22,23,34,36,41,42,43,44,45,47,50,51,57,61,63,66,83,84,85,87,96,97,98,100,102,104,105,106,107,110,113,115,116,],[12,-6,-64,38,-15,-16,-17,-18,-19,-20,-21,-7,-9,-34,-64,-45,-62,-55,-57,-60,-61,-8,-22,-35,-37,-58,-62,-59,-27,-47,-36,-56,-44,-28,-30,-31,-23,-24,-26,-46,-25,-29,]),'IF':([11,27,38,62,86,108,111,],[25,25,25,25,25,25,25,]),'WHILE':([11,27,38,53,58,59,60,62,86,108,111,],[26,26,26,88,-12,-13,-14,26,26,26,26,]),'FOR':([11,27,38,62,86,108,111,],[28,28,28,28,28,28,28,]),'READ':([11,27,38,62,86,108,111,],[29,29,29,29,29,29,29,]),'WRITE':([11,27,38,62,86,108,111,],[30,30,30,30,30,30,30,]),'DO':([11,27,38,41,42,43,44,45,47,50,51,52,62,63,66,83,84,85,86,96,97,98,100,103,108,111,113,],[27,27,27,-34,-64,-45,-62,-55,-57,-60,-61,86,27,-35,-37,-58,-62,-59,27,-47,-36,-56,-44,111,27,27,-46,]),'COMMA':([14,],[35,]),'END':([15,38,58,59,60,95,101,112,114,],[37,-64,-12,-13,-14,107,110,115,116,]),'ASSIGN':([24,],[39,]),'LPAREN':([25,26,29,30,39,46,48,49,56,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,88,89,109,],[46,46,55,56,46,46,46,46,46,46,46,-48,-49,-50,-38,-39,-40,-41,-42,-43,46,-51,-52,-53,-54,46,46,46,46,]),'NOT':([25,26,39,46,56,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,88,89,109,],[48,48,48,48,48,48,48,-48,-49,-50,-38,-39,-40,-41,-42,-43,48,-51,-52,-53,-54,48,48,48,48,]),'MINUS':([25,26,39,42,43,44,45,46,47,50,51,56,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,85,88,89,92,96,97,98,99,100,109,113,],[49,49,49,68,-45,-62,-55,49,-57,-60,-61,49,49,49,-48,-49,-50,-38,-39,-40,-41,-42,-43,49,-51,-52,-53,-54,49,-58,-62,-59,49,49,68,-47,68,-56,68,-44,49,68,]),'NUMBER':([25,26,39,46,48,49,56,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,88,89,109,],[51,51,51,51,51,51,51,51,51,-48,-49,-50,-38,-39,-40,-41,-42,-43,51,-51,-52,-53,-54,51,51,51,51,]),'ELSE':([38,58,59,60,95,],[-64,-12,-13,-14,108,]),'THEN':([40,41,42,43,44,45,47,50,51,63,66,83,84,85,96,97,98,100,113,],[62,-34,-64,-45,-62,-55,-57,-60,-61,-35,-37,-58,-62,-59,-47,-36,-56,-44,-46,]),'PLUS':([42,43,44,45,47,50,51,83,84,85,92,96,97,98,99,100,113,],[67,-45,-62,-55,-57,-60,-61,-58,-62,-59,67,-47,67,-56,67,-44,67,]),'OR':([42,43,44,45,47,50,51,83,84,85,92,96,97,98,99,100,113,],[69,-45,-62,-55,-57,-60,-61,-58,-62,-59,69,-47,69,-56,69,-44,69,]),'EQUAL':([42,43,44,45,47,50,51,83,84,85,96,98,100,113,],[70,-45,-62,-55,-57,-60,-61,-58,-62,-59,-47,-56,-44,-46,]),'LESS':([42,43,44,45,47,50,51,83,84,85,96,98,100,113,],[71,-45,-62,-55,-57,-60,-61,-58,-62,-59,-47,-56,-44,-46,]),'LESSEQUAL':([42,43,44,45,47,50,51,83,84,85,96,98,100,113,],[72,-45,-62,-55,-57,-60,-61,-58,-62,-59,-47,-56,-44,-46,]),'GREATER':([42,43,44,45,47,50,51,83,84,85,96,98,100,113,],[73,-45,-62,-55,-57,-60,-61,-58,-62,-59,-47,-56,-44,-46,]),'GREATEREQUAL':([42,43,44,45,47,50,51,83,84,85,96,98,100,113,],[74,-45,-62,-55,-57,-60,-61,-58,-62,-59,-47,-56,-44,-46,]),'LESSGREATER':([42,43,44,45,47,50,51,83,84,85,96,98,100,113,],[75,-45,-62,-55,-57,-60,-61,-58,-62,-59,-47,-56,-44,-46,]),'TO':([42,43,44,45,47,50,51,54,61,63,66,83,84,85,96,97,98,100,113,],[-64,-45,-62,-55,-57,-60,-61,89,-22,-35,-37,-58,-62,-59,-47,-36,-56,-44,-46,]),'RPAREN':([42,43,44,45,47,50,51,63,66,82,83,84,85,90,91,92,93,94,96,97,98,100,113,],[-64,-45,-62,-55,-57,-60,-61,-35,-37,100,-58,-62,-59,104,105,-32,-33,-63,-47,-36,-56,-44,-46,]),'COLON':([43,44,45,47,50,51,83,84,85,96,98,99,100,113,],[-45,-62,-55,-57,-60,-61,-58,-62,-59,-47,-56,109,-44,-46,]),'MULTI':([43,44,45,47,50,51,83,84,85,96,98,100,],[77,-62,-55,-57,-60,-61,-58,-62,-59,77,-56,-44,]),'DIVIDE':([43,44,45,47,50,51,83,84,85,96,98,100,],[78,-62,-55,-57,-60,-61,-58,-62,-59,78,-56,-44,]),'MOD':([43,44,45,47,50,51,83,84,85,96,98,100,],[79,-62,-55,-57,-60,-61,-58,-62,-59,79,-56,-44,]),'AND':([43,44,45,47,50,51,83,84,85,96,98,100,],[80,-62,-55,-57,-60,-61,-58,-62,-59,80,-56,-44,]),'INTERROGATION':([44,100,],[81,-44,]),'LITERAL':([56,],[94,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'body':([3,],[4,]),'declaration_list':([5,12,],[6,32,]),'declaration':([5,12,],[7,7,]),'type':([5,12,],[8,8,]),'identifier_list':([8,35,],[13,57,]),'statement_list':([11,27,38,62,86,108,111,],[15,53,59,95,101,112,114,]),'statement':([11,27,38,62,86,108,111,],[16,16,16,16,16,16,16,]),'assign_statement':([11,27,28,38,62,86,108,111,],[17,17,54,17,17,17,17,17,]),'if_statement':([11,27,38,62,86,108,111,],[18,18,18,18,18,18,18,]),'while_statement':([11,27,38,62,86,108,111,],[19,19,19,19,19,19,19,]),'for_statement':([11,27,38,62,86,108,111,],[20,20,20,20,20,20,20,]),'read_statement':([11,27,38,62,86,108,111,],[21,21,21,21,21,21,21,]),'write_statement':([11,27,38,62,86,108,111,],[22,22,22,22,22,22,22,]),'do_while_statement':([11,27,38,62,86,108,111,],[23,23,23,23,23,23,23,]),'declaration_list_aux':([12,],[31,]),'empty':([12,14,38,42,],[33,36,60,66,]),'identifier_list_aux':([14,],[34,]),'condition':([25,26,88,89,],[40,52,102,103,]),'expression':([25,26,39,46,88,89,],[41,41,61,82,41,41,]),'simple_expression':([25,26,39,46,56,65,81,88,89,109,],[42,42,42,42,92,97,99,42,42,113,]),'term':([25,26,39,46,56,64,65,81,88,89,109,],[43,43,43,43,43,96,43,43,43,43,43,]),'par_expression':([25,26,39,46,48,49,56,64,65,76,81,88,89,109,],[44,44,44,44,84,84,44,84,44,84,44,44,44,44,]),'factor_a':([25,26,39,46,56,64,65,76,81,88,89,109,],[45,45,45,45,45,45,45,98,45,45,45,45,]),'factor':([25,26,39,46,48,49,56,64,65,76,81,88,89,109,],[47,47,47,47,83,85,47,47,47,47,47,47,47,47,]),'statement_prime':([38,],[58,]),'expression_aux':([42,],[63,]),'addop':([42,92,97,99,113,],[64,64,64,64,64,]),'relop':([42,],[65,]),'mulop':([43,96,],[76,76,]),'do_while_statement_suffix':([53,],[87,]),'writable':([56,],[91,]),'literal':([56,],[93,]),'if_statement_aux':([95,],[106,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID body','program',3,'p_program','yacc.py',17),
  ('body -> DECLARE declaration_list BEGIN statement_list END','body',5,'p_body','yacc.py',20),
  ('declaration_list -> declaration SEMICOLON declaration_list_aux','declaration_list',3,'p_declaration_list','yacc.py',23),
  ('declaration_list_aux -> declaration_list','declaration_list_aux',1,'p_declaration_list_aux','yacc.py',26),
  ('declaration_list_aux -> empty','declaration_list_aux',1,'p_declaration_list_aux','yacc.py',27),
  ('declaration -> type identifier_list','declaration',2,'p_declaration','yacc.py',30),
  ('identifier_list -> ID identifier_list_aux','identifier_list',2,'p_identifier_list','yacc.py',33),
  ('identifier_list_aux -> COMMA identifier_list','identifier_list_aux',2,'p_identifier_list_aux','yacc.py',36),
  ('identifier_list_aux -> empty','identifier_list_aux',1,'p_identifier_list_aux','yacc.py',37),
  ('type -> INTEGER','type',1,'p_type','yacc.py',40),
  ('type -> DECIMAL','type',1,'p_type','yacc.py',41),
  ('statement_list -> statement SEMICOLON statement_prime','statement_list',3,'p_statement_list','yacc.py',44),
  ('statement_prime -> statement_list','statement_prime',1,'p_statement_prime','yacc.py',48),
  ('statement_prime -> empty','statement_prime',1,'p_statement_prime','yacc.py',49),
  ('statement -> assign_statement','statement',1,'p_statement','yacc.py',52),
  ('statement -> if_statement','statement',1,'p_statement','yacc.py',53),
  ('statement -> while_statement','statement',1,'p_statement','yacc.py',54),
  ('statement -> for_statement','statement',1,'p_statement','yacc.py',55),
  ('statement -> read_statement','statement',1,'p_statement','yacc.py',56),
  ('statement -> write_statement','statement',1,'p_statement','yacc.py',57),
  ('statement -> do_while_statement','statement',1,'p_statement','yacc.py',58),
  ('assign_statement -> ID ASSIGN expression','assign_statement',3,'p_assign_statement','yacc.py',62),
  ('if_statement -> IF condition THEN statement_list if_statement_aux','if_statement',5,'p_if_statement','yacc.py',65),
  ('if_statement_aux -> END','if_statement_aux',1,'p_if_statement_aux','yacc.py',68),
  ('if_statement_aux -> ELSE statement_list END','if_statement_aux',3,'p_if_statement_aux','yacc.py',69),
  ('while_statement -> WHILE condition DO statement_list END','while_statement',5,'p_while_statement','yacc.py',72),
  ('do_while_statement -> DO statement_list do_while_statement_suffix','do_while_statement',3,'p_do_while_statement','yacc.py',75),
  ('do_while_statement_suffix -> WHILE condition','do_while_statement_suffix',2,'p_do_while_statement_suffix','yacc.py',78),
  ('for_statement -> FOR assign_statement TO condition DO statement_list END','for_statement',7,'p_for_statement','yacc.py',81),
  ('read_statement -> READ LPAREN ID RPAREN','read_statement',4,'p_read_statement','yacc.py',84),
  ('write_statement -> WRITE LPAREN writable RPAREN','write_statement',4,'p_write_statement','yacc.py',87),
  ('writable -> simple_expression','writable',1,'p_writable','yacc.py',89),
  ('writable -> literal','writable',1,'p_writable','yacc.py',90),
  ('condition -> expression','condition',1,'p_condition','yacc.py',92),
  ('expression -> simple_expression expression_aux','expression',2,'p_expression','yacc.py',94),
  ('expression_aux -> relop simple_expression','expression_aux',2,'p_expression_aux','yacc.py',96),
  ('expression_aux -> empty','expression_aux',1,'p_expression_aux','yacc.py',97),
  ('relop -> EQUAL','relop',1,'p_relop','yacc.py',99),
  ('relop -> LESS','relop',1,'p_relop','yacc.py',100),
  ('relop -> LESSEQUAL','relop',1,'p_relop','yacc.py',101),
  ('relop -> GREATER','relop',1,'p_relop','yacc.py',102),
  ('relop -> GREATEREQUAL','relop',1,'p_relop','yacc.py',103),
  ('relop -> LESSGREATER','relop',1,'p_relop','yacc.py',104),
  ('par_expression -> LPAREN expression RPAREN','par_expression',3,'p_par_expression','yacc.py',107),
  ('simple_expression -> term','simple_expression',1,'p_simple_expression','yacc.py',111),
  ('simple_expression -> par_expression INTERROGATION simple_expression COLON simple_expression','simple_expression',5,'p_simple_expression','yacc.py',112),
  ('simple_expression -> simple_expression addop term','simple_expression',3,'p_simple_expression','yacc.py',113),
  ('addop -> PLUS','addop',1,'p_addop','yacc.py',117),
  ('addop -> MINUS','addop',1,'p_addop','yacc.py',118),
  ('addop -> OR','addop',1,'p_addop','yacc.py',119),
  ('mulop -> MULTI','mulop',1,'p_mulop','yacc.py',122),
  ('mulop -> DIVIDE','mulop',1,'p_mulop','yacc.py',123),
  ('mulop -> MOD','mulop',1,'p_mulop','yacc.py',124),
  ('mulop -> AND','mulop',1,'p_mulop','yacc.py',125),
  ('term -> factor_a','term',1,'p_term','yacc.py',128),
  ('term -> term mulop factor_a','term',3,'p_term','yacc.py',129),
  ('factor_a -> factor','factor_a',1,'p_factor_a','yacc.py',132),
  ('factor_a -> NOT factor','factor_a',2,'p_factor_a','yacc.py',133),
  ('factor_a -> MINUS factor','factor_a',2,'p_factor_a','yacc.py',134),
  ('factor -> ID','factor',1,'p_factor','yacc.py',137),
  ('factor -> NUMBER','factor',1,'p_factor','yacc.py',138),
  ('factor -> par_expression','factor',1,'p_factor','yacc.py',139),
  ('literal -> LITERAL','literal',1,'p_literal','yacc.py',143),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',146),
]

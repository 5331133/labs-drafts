





dic = {}



list_to_input = ['classA : classB classC classD classG classH', 'classB : classC classE classG classH classK classL', 'classC : classE classD classH classK classL', 'classE : classD classF classK classL', 'classD : classG classH', 'classF : classK', 'classG : classF', 'classH : classL', 'classK : classH classL', 'classL']#10 входов

list_to_question=['classK classD', 'classD classA', 'classG classD', 'classH classA', 'classE classE', 'classH classG', 'classE classL', 'classB classD', 'classD classL', 'classD classG', 'classD classE', 'classA classF', 'classA classC', 'classK classA', 'classA classH', 'classK classD', 'classH classB', 'classK classB', 'classD classL', 'classG classG', 'classA classH', 'classK classL', 'classG classE', 'classB classA', 'classC classK', 'classK classL', 'classC classL', 'classG classC', 'classD classD', 'classC classG', 'classE classA', 'classF classK', 'classB classG', 'classH classL', 'classL classF', 'classH classG', 'classD classA', 'classH classL']#38 запросов

answers = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No']#38 ответов
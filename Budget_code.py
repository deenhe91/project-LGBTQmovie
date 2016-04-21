

def get_movie_value(soup, field_name):
    obj = soup.find(text=re.compile(field_name))
    if not obj:
        return None
    next_sibling = obj.findNextSibling()
    if next_sibling:
        return next_sibling.text
    else:
        return None
        
def budget_to_int(budgetstring):
    if budgetstring == 'N/A':
        return None
    else:
        try:
            budgetstring = budgetstring.replace('$','').replace(' million','')
            budget = int(float(budgetstring)*1000000)
            return budget
        except ValueError:
            return budgetstring
        
budgetstring = get_movie_value(soup, 'Production Budget')
budget = budget_to_int(budgetstring)
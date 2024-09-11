#capellmbse_helper
import capellambse
import pandas as pd 
#Monkey Patch to constraint class to extract stipped text without hyper links.
from bs4 import BeautifulSoup   
def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()
def spectext(self):
   
    return strip_html_tags(str(self.specification))
    
capellambse.metamodel.capellacore.Constraint.spectext = spectext

def display_function_property_values(model):
    df = pd.DataFrame({
        'Logical Function': [],
        'Property Value Group Name': [],
        'Propery Name': [],
        'Property Value': [],
        })
    
    for function in model.all_functions:
        for pvg in  function.applied_property_value_groups :
            for pv in  pvg.property_values:
                #print("LogicalFunction=",'"' +function.name+ '"',"property_value_groups=",'"' +pvg.name+ '"','"Property Name"=','"' +pv.name+ '"','"Value"=',pv.value )
                df.loc[len(df)] = [function.name,pvg.name,\
                                    pv.name, pv.value]
    display(df)

def display_component_property_values(model):
    df = pd.DataFrame({
        'Logical Component': [],
        'Property Value Group Name': [],
        'Property Name': [],
        'Property Value': [],
        })
    for component in model.all_components:
        for pvg in  component.applied_property_value_groups :
            for pv in  pvg.property_values:
                #print("LogicalComponents=",'"' +component.name+ '"',"property_value_groups=",'"' +pvg.name+ '"','Property Name=','"' + pv.name + '"','Value=',pv.value  )
                df.loc[len(df)] = [component.name,pvg.name,\
                                    pv.name, pv.value]
    display(df)




def display_function_constraints(model) :
    df = pd.DataFrame({
        'Logical Function': [],
        'Constraint Index':[],
        'Constraint': [],
        })
    
    for function in model.all_functions:
        index = 0
        for constraint in function.constraints:
            df.loc[len(df)] = [function.name,\
                                    index,\
                                    constraint.spectext()]
            index = index +1
    pd.set_option('display.max_colwidth', 200)  # Set the maximum column width
    display(df)

def display_component_constraints(model):
    df = pd.DataFrame({
        'Logical Component': [],
        'Constraint Index':[],
        'Constraint': [],
        })
    for component in model.all_components:
        index = 0
        for constraint in component.constraints:
            df.loc[len(df)] = [component.name,\
                                   index,\
                                   constraint.spectext]
            index = index +1
    pd.set_option('display.max_colwidth', 200)  # Set the maximum column width
    
    display(df)
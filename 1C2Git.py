#!/usr/local/bin/python
import sys
import xml.etree.ElementTree as etree


__author__ = 'jgoncharova'

parametrs = {}
meta_table_dict = {}
meta_table_list = []

def read_meta_object(node,type):

	elements_list = node.findall("{http://v8.1c.ru/8.3/MDClasses}"+type)
	meta_table_dict[type]=[x.text for x in elements_list]
	
	elements_defined_list=[{'type':type,'name':x.text} for x in elements_list]
	meta_table_list.extend(elements_defined_list)




def read_meta_table():
	'''
	считывает список метаданных из файла Configuration.xml
	на всякий случаей формируем 2 коллекции:
	словарь meta_table_dict с значениями-списками объектов метаданных
	и список meta_table_list содержащий словари
	'''

	conf_xml_name = parametrs['full_text_catalog']+'\Configuration.xml'
	conf_xml_tree = etree.parse(conf_xml_name)
	children_objects = conf_xml_tree.getroot()[0][2]
	
	read_meta_object(children_objects,'Language')
	read_meta_object(children_objects,'Subsystem')
	read_meta_object(children_objects,'StyleItem')
	read_meta_object(children_objects,'CommonPicture')
	read_meta_object(children_objects,'SessionParameter')
	read_meta_object(children_objects,'Role')
	read_meta_object(children_objects,'CommonTemplate')
	read_meta_object(children_objects,'FilterCriterion')
	read_meta_object(children_objects,'CommonModule')
	read_meta_object(children_objects,'CommonAttribute')
	read_meta_object(children_objects,'ExchangePlan')
	read_meta_object(children_objects,'XDTOPackage')
	read_meta_object(children_objects,'WebService')
	read_meta_object(children_objects,'EventSubscription')
	read_meta_object(children_objects,'ScheduledJob')
	read_meta_object(children_objects,'SettingsStorage')
	read_meta_object(children_objects,'FunctionalOption')
	read_meta_object(children_objects,'FunctionalOptionsParameter')
	read_meta_object(children_objects,'CommonCommand')
	read_meta_object(children_objects,'CommandGroup')
	read_meta_object(children_objects,'Constant')
	read_meta_object(children_objects,'CommonForm')
	read_meta_object(children_objects,'Catalog')
	read_meta_object(children_objects,'Document')
	read_meta_object(children_objects,'DocumentNumerator')
	read_meta_object(children_objects,'Sequence')
	read_meta_object(children_objects,'DocumentJournal')
	read_meta_object(children_objects,'Enum')
	read_meta_object(children_objects,'Report')
	read_meta_object(children_objects,'DataProcessor')
	read_meta_object(children_objects,'InformationRegister')
	read_meta_object(children_objects,'AccumulationRegister')
	read_meta_object(children_objects,'ChartOfCharacteristicTypes')
	read_meta_object(children_objects,'ChartOfAccounts')
	read_meta_object(children_objects,'AccountingRegister')
	read_meta_object(children_objects,'ChartOfCalculationTypes')




def read_ini_file():
	"""
	считываем файл с настройками
	файл должен называться 1C2Git.ini и лежать рядом со сценарием 1C2Git.py
	"""
	
	ini_file = open('1C2Git.ini') #хардкод
	ini_file_string = ini_file.read()
	
	ini_file_sections = ini_file_string.split('[')

	if len(ini_file_sections) == 0:
		raise Exeption('wrong 1C2Git.ini format: no section')

         
	for current_section in ini_file_sections:
		section_content = current_section.split(']')

		if section_content[0]=='main':
			ini_file_strngs=section_content[1].split('\n')

			for param_string in ini_file_strngs:
				if param_string!='':
					current_param = param_string.split('=')
					parametrs[current_param[0]]=current_param[1]
			
	
	ini_file.close()
	
	return parametrs
	
def	read_item_dependency(metadata_item):
	
	file_name = parametrs['full_text_catalog']+'\\'+metadata_item['type']+'\\'+metadata_item['name']+'.xml'
	print(file_name)

def read_dependency():
	for metadata_item in meta_table_list:
		read_item_dependency(metadata_item)

def save_1c():
	parametrs = read_ini_file()
		
	read_meta_table()
	
	read_item_dependency(meta_table_list[1525])
	
	#read_dependency()
	print(meta_table_list[1525])
	
# основная программа

Operation = sys.argv[1]

if Operation == '-s':
	 save_1c()










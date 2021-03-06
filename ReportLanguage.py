## Report Language Formatting
#
#
import xml.etree.ElementTree as ET

## Language Subroutine
#
# Capture the languages and metrics around them
#
def languageCells(parms) :
	# begin operation by eliminating the 'CodeDx' tag from the XML
	parent = parms['parent']
	parent.remove(parms['child'])
	
	# call Code Dx to get our metrics list
	metrics = parms['cdx'].getCodeMetrics(parms['proj_id'])
	
	# get the parent XML item for this operation.
	parent = parms['parent']
	
	# loop through the incoming metrics and create a series of dictionaries
	# with the data we want to present
	lang_metrics = metrics[0]['data']
	for key, value in sorted(lang_metrics.items()) :
		
		# create an XML line based on the parent
		row = ET.SubElement(parent, 'fo:table-row')
		cell = ET.SubElement(row, 'fo:table-cell', { 'border-width' : 'thin', 'border-style' : 'solid' })
		lang = ET.SubElement(cell, 'fo:block')
		lang.text = key
		cell = ET.SubElement(row, 'fo:table-cell', { 'border-width' : 'thin', 'border-style' : 'solid' })
		loc = ET.SubElement(cell, 'fo:block')
		loc.text = str(value['numTotalLines'])
		cell = ET.SubElement(row, 'fo:table-cell', { 'border-width' : 'thin', 'border-style' : 'solid' })
		num_files = ET.SubElement(cell, 'fo:block')
		num_files.text = str(value['numSourceFiles'])
		cell = ET.SubElement(row, 'fo:table-cell', { 'border-width' : 'thin', 'border-style' : 'solid' })
		findings = ET.SubElement(cell, 'fo:block')
#		findings.text = str(value['numFindings'])
		findings.text = 'TBD'

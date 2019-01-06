# Informatica Converion example

### The Informatica Converion example include:

* __InformaticaSampleData.xml__ - Informatica sample data in XML format.
* __InformaticaMappingLogic.docx__ - Holds the mapping logic used in this sample from Informatica data to Control-M data.
* __InformaticaConversionRules.json__ - The Informatica Conversion Rules json file that holds the Self Converion rules code.
* __ControlM_Result.xml__ - The Control-M data created by the Self Converion when converting the Informatica sample data using the Informatica converion rules.


### Informatica mapping logic  
Every __BOX__ Element        -> Control-M Smart Folder

Attribute __Box_Name__ value -> Smart Folder Name

Every __JOB__ Element        -> Control-M Job

Attribute __UserName__ value -> Job Run As

Attribute __Group__ value    -> Job Application



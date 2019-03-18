# Informatica Conversion example
This repository contains Informatica "Conversion Rules" code samples that use groovy and [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) to convert sample Informatica input data into Control-M Data. 
You can use these Informatica Conversion Rules code samples to convert your Informatica data to Control-M data, or as an example as to how to use the [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) to create Control-M Informatica jobs.

# Online Documentation
For more information, see [**Control-M Self Conversion**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-817142681.html) and the [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) online documentation.
To download the latest Control-M  Self Conversion, go to: <br> **ftp://ftp.bmc.com/pub/control-m/opensystem/Control-M_Conversions_for_DS/**<br>
For Control-M Self Conversion Training Video click [**Here**.](https://www.youtube.com/watch?v=2MrFcahMhH0)
### The Informatica Conversion example include:
* __SampleData.xml__ - Informatica sample data in XML format. [(extract data instructions)](https://github.com/controlm/self-conversion-api-community-solutions/tree/master/Informatica#extract-informatica-data-in-xml-format)
* __MappingLogic.xlsx__ - Holds the mapping logic used in this sample from Informatica data to Control-M data.
* __ConversionRules.json__ - The Informatica Conversion Rules json file that holds the Self Converion rules code samples.
* __ControlM_Result.xml__ - The Control-M data created by the Self Converion when converting the Informatica sample data using the Informatica converion rules sample.

### XML structure sample:
```xml 
<BOX>
  <JOB Name="JOB1">Job Text</JOB>
</BOX> 
```
 __Above sample contains:__
* BOX Element that has child JOB Element. 
* JOB Element contains an "Name" attribute with value "JOB1"
* JOB Element text value is "Job Text"

### Informatica mapping logic  
Informatica Data | Control-M Data
-|-
WORKFLOW Element|Smart Folder
WORKFLOW "NAME" Attribute|Smart Folder Name
WORKLET Element|Sub Folder Definition
WORKLET "NAME" Attribute|Sub Folder Name
TASK Element with Attribute TYPE="Command"|OS Job Definition
TASK "NAME" Attribute|Job Name
TASK "DESCRIPTION" Attribute|Job Description
TASK > VALUEPAIR "VALUE" Attribute|OS Job Command value
TASK Element with Attribute TYPE="start"|Dummy job Definition
SESSION Element|Informatica Job Definition
SESSION "NAME" Attribute|Informatica Job Name
SESSION "DESCRIPTION" Attribute|Informatica Job Description
WORKFLOWLINK Element|Declare dependency between two entities 
WORKFLOWLINK "FROMTASK" Attribute|Name of the Entity that raise Out Condition
WORKFLOWLINK "TOTASK" Attribute|Name of the Entity that accept In Condition
REPOSITORY "NAME" Attribute|Informatica Job Host/Host Group
FOLDER "NAME" Attribute|Informatica Job Repository Folder Name
WORKFLOW "NAME" Attribute|Informatica Job Run Single Task
TASKINSTANCE "TASKNAME" Attribute|Reference to the Job/Sub-Folder Definition
TASKINSTANCE Element|Job/Sub-Folder Instance
WORKFLOW > TASKINSTANCE|Job/Sub-Folder is under  a Smart Folder
WORKLET > TASKINSTANCE|Job/Sub-Folder is under a Sub-Folder

### Usage Instructions
1. Clone or download the repository.
2. Open Control-M Self Conversion.
3. Import the __Informatica Conversion Rules__ json file.
4. Create a new Self Conversion project: 
   * Enter a project name.
   * Load the **Informatica Sample Input Data**.
   * In "Use existing conversion rules" dropdown list, select the conversion rules imported in step 3.
   * Click "Create Project".
5. Click Run.
6. Review the conversion results.

## Contribution guide
To contribute, please follow these guidelines.

### Files, folders and naming conventions
1. Every conversion and its associated files must be contained in its own **folder**. Name this folder as the name of the tool that you convert from.
2. The __folder__ should contain:
   * __SampleData__ - A folder that holds tool sample Input Data in XML format that we want to convert to Control-M data.
   * __MappingLogic.xlsx__ - The mapping logic used for conversion in this sample, from the  tool sample input data to Control-M data.
   * __ConversionRules.json__ - The tool Conversion Rules json file that contains the Self Converion rules code.
   * __ControlM_Result.xml__ - The Control-M data created by the Self Converion when converting the tool sample data using the Demo Tool conversion rules.

3. Include a **README.md** file that explains the sample. A good description helps other community members to understand your sample. The README.md uses [Github Flavored Markdown](https://guides.github.com/features/mastering-markdown/) for formatting text.

## Extract Informatica data in XML format
From repository manager -> click on the workflow -> Repository -> Export Objects…
![Informatica data extraction](images/Informatica_data_extraction.png)



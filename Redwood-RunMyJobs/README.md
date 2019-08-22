# Redwood RunMyJobs Conversion example
This repository contains Redwood RunMyJobs "Conversion Rules" code samples that use groovy and [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) to convert sample Redwood RunMyJobs input data into Control-M Data.<br> 
You can use these Redwood RunMyJobs Conversion Rules code samples to convert your Redwood RunMyJobs data to Control-M data, or use them as an example in using the [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) to create Control-M Redwood RunMyJobs jobs.

### The Redwood RunMyJobs Conversion example includes:
* __SampleData.xml__ - Redwood RunMyJobs sample data in XML format.
* __MappingLogic.xlsx__ - Holds the mapping logic used in this sample to convert from Redwood RunMyJobs data to Control-M data.
* __ConversionRules.json__ - The Redwood RunMyJobs Conversion Rules json file that holds the Self Converion rules code samples.
* __ControlM_Result.xml__ - The Control-M data created by the Self-Conversion when converting the Redwood RunMyJobs sample data using the Redwood RunMyJobs converion rules sample.

### XML structure sample:
```xml 
<BOX>
  <JOB Name="JOB1">Job Text</JOB>
</BOX> 
```
 __Above sample contains:__
* BOX Element that has a child JOB Element. 
* JOB Element contains a "Name" attribute with value "JOB1"
* JOB Element text value is "Job Text"

### Redwood RunMyJobs mapping logic
Redwood RunMyJobs Data | Control-M Data
-|-
**JobDefinitionType > path** attribute: containts "JobChain"|Folder
**JobDefinitionType > path** attribute:  doesn’t containts "JobChain"|Job
Value of **Name** Element|Folder/Job Name
Value of **Description** Element|Folder/Job Description
**ParentApplication > path** attribute: the value between the first and the second dot.<br>For example:<br> ```xml <ParentApplication type="Application" path="GLOBAL.Application.SubApplication" /> ```|Folder/Job Application
**ParentApplication > path** attribute: the value after the second dot.<br> For example:<br> ```xml <ParentApplication type="Application" path="GLOBAL.Application.SubApplication" /> ```|Folder/Job Sub Application
**DefaultQueue > path** attribute: the value after the dot|Job Host
Folder contains **JobChainStep > JobChainCall > JobDefinition > path** attribute: value after the dot is the job / sub-folder name| Hierarchy
Create condition between entities according to the order of **JobChainStep > JobChainCall**|Conditions
**JobDefinitionType > path** attribute = GLOBAL.SAPR3|SAPR3 Job Type
If Value of **JobDefinitionParameter > Name** Element equals JOBNAME then value of  **JobDefinitionParameter > DefaultExpression **|SAPR3 Job Name
If Value of **JobDefinitionParameter > Name** Element equals JOBCLASS then value of  **JobDefinitionParameter > DefaultExpression**|SAPR3 JOBCLASS
Create Variable with name from the Value of **JobDefinitionParameter > Name** Element (**only if the name doesnt include in the "Redwood patameters list that are being converted to control-m attribute"**)|Variable Name
Value of **JobDefinitionParameter > DefaultExpression**|Variable Value
If Value of **JobDefinitionParameter > Name** Element equals Step parameter name then value of DefaultExpression Converted to SAPR3 Step Parameter**(Step parameters description in the "Abap Step Parameters" table)**|SAPR3 Abap Step Parameters
**JobDefinitionType > path** attribute = GLOBAL.SAPR3 && value of **SAPScript > SAPScriptAttribute >Value** Element="BW_CHAIN_RUN"|SAPBW Job Type
If Value of **JobDefinitionParameter > Name** Element equals NAME then value of  **JobDefinitionParameter > DefaultExpression**|SABBW Process Chain Id
**JobDefinitionType > path** attribute doesn’t contains ".SAPR3" && Script element exists |OS Embedded Script Type
Value of **Script > Source** Element|OS Embedded Script - Script
``<Control-M job name>``.cmd|OS Embedded Script - file name
Value of **Script > RunAsUser** Element|OS Embedded Script - Run As

#### Abap Step Parameters table
Abap Step Parameter| Redwood RunMyJobs Value
-|-
Program Name|ABAP_PROGRAM_NAME
Variant Name|ABAP_VARIANT_NAME
Temporary Variant|TEMPORARY_VARIANT
User|SAP_USER_NAME
Language|LANGUAGE
Print Archive Mode|PRINT_ARMOD
Output Device|PRINT_PDEST
Department|PRINT_PRTXT
Recipinet|PRINT_PRTXT
Number of Copies|PRINT_PRCOP
Enable/Disable New Spool Request|PRINT_PRNEW
Spool Request Name|PRINT_PLIST
Time Of Print|PRINT_PRIMM
Enable/Disable Delete After Print|PRINT_PRREL
Print Expiration|PRINT_PEXPI
Output Format Rows|PRINT_LICT
Output Format Columns|PRINT_LISZ
Output Format Layout|PRINT_PAART
Enable/Disable Selection Cover Page|PRINT_PRBIG
Sap Cover Page|PRINT_PRSAP
Spool Request Authorization|PRINT_PRBER
Os Cover Sheet|PRINT_PRUNX
Archive Id|ARCHIVE_SAP_OBJECT
Archive Document Type|ARCHIVE_AR_OBJECT
Archive Information Field|ARCHIVE_INFO
Archive Text|ARCHIVE_ARCTEXT

#### Redwood patameters list that are being converted to Control-M attributes
* JOBNAME
* ABAP_PROGRAM_NAME
* ABAP_VARIANT_NAME
* TEMPORARY_VARIANT
* JOBCLASS
* SAP_USER_NAME
* LANGUAGE
* TARGET_SERVER
* TARGET_GROUP
* PRINT_ARMOD
* PRINT_PDEST
* PRINT_PRTXT
* PRINT_PRCOP
* PRINT_PRNEW
* PRINT_PLIST
* PRINT_PRIMM
* PRINT_PRREL
* PRINT_PEXPI
* PRINT_LICT
* PRINT_LISZ
* PRINT_PAART
* PRINT_PRBIG
* PRINT_PRSAP
* PRINT_PRREC
* PRINT_PRABT
* PRINT_PRBER
* PRINT_PRDSN
* PRINT_PTYPE
* PRINT_FOOTL
* PRINT_PRUNX
* DRAFT_MODE
* PAGE_ORIENTATION
* ARCHIVE_SAP_OBJECT
* ARCHIVE_AR_OBJECT
* ARCHIVE_INFO
* ARCHIVE_ARCTEXT
* SHOWLOG
* SHOWSPOOL
* DELETE_JOB
* JOBCOUNT
* CLIENT
* SAP_SYSTEMS


### Usage Instructions
1. Clone or download the repository.
2. Open Control-M Self Conversion.
3. Import the __Redwood RunMyJobs Conversion Rules__ json file.
4. Create a new Self Conversion project: 
   * Enter a project name.
   * Load the **Redwood RunMyJobs Sample Input Data**.
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
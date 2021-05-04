# Load Sharing Facility Conversion example
This repository contains Load Sharing Facility "Conversion Rules" code samples that use groovy and [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) to convert sample Load Sharing Facility input data into Control-M Data.<br> 
You can use these Load Sharing Facility Conversion Rules code samples to convert your Load Sharing Facility data to Control-M data, or use them as an example in using the [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) to create Control-M Load Sharing Facility jobs.

### The Load Sharing Facility Conversion example includes:
* __SampleData.xml__ - Load Sharing Facility sample data in XML format. [(Load Sharing Facility data extraction)](https://github.com/controlm/self-conversion-api-community-solutions/tree/master/Load-Sharing-Facility#extract-Load-Sharing-Facility-data-in-xml-format)
* __MappingLogic.xlsx__ - Holds the mapping logic used in this sample to convert from Load Sharing Facility data to Control-M data.
* __LoadSharingFacility_ConversionRules.json__ - The Load Sharing Facility Conversion Rules json file that holds the Self Converion rules code samples.
* __ControlM_Result.xml__ - The Control-M data created by the Self-Conversion when converting the Load Sharing Facility sample data using the Load Sharing Facility converion rules sample.
* __HelixControlM_Result.json__ - The Helix Control-M data created by the Helix Control-M Self-Conversion when converting the Load Sharing Facility sample data using the Load Sharing Facility conversion rules sample. 

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

### Load Sharing Facility mapping logic  
Load Sharing Facility Data | Control-M Data
-|-
FlowDef Element|Smart Folder
FlowDef "Name" Attribute|Smart Folder Name
FlowDef > JobDef Element with Attribute TYPE="subFlow"|Sub Folder Definition
FlowDef > JobDef Element with Attribute TYPE="Job"|Job Definition
FlowDef > JobDef "Name" Attribute|Job/Sub-Folder Name
FlowDef > JobDef > TYPE="Job" > JobCmdLine Element with Attribute "Value"|OS Job Command value
FlowDef > JobDef > TYPE="Job" > Host Element with Attribute "Value"| Job Host/Host Group
FlowDef > Dependencies Element with Attribute "Reference"|Name of the Entity that accept In Condition
FlowDef > Dependencies > Events Element with Attribute "CombinationType"|Conditions Relationship in the entity that accept In Conditions
FlowDef > Dependencies > Events > Event Element > done Element with Attribute "Depend"|Name of the Entity that raise Out Condition

### Usage Instructions
1. Clone or download the repository.
2. Open Control-M Self Conversion.
3. Import the __Load Sharing Facility Conversion Rules__ json file.
4. Create a new Self Conversion project: 
   * Enter a project name.
   * Load the **Load Sharing Facility Sample Input Data**.
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
   * __HelixControlM_Result.json__ - The Helix Control-M data created by the Helix Control-M Self-Conversion when converting the tool sample data using the Demo Tool conversion rules.   

   

3. Include a **README.md** file that explains the sample. A good description helps other community members to understand your sample. The README.md uses [Github Flavored Markdown](https://guides.github.com/features/mastering-markdown/) for formatting text.


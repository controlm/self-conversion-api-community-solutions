# MSSQL Agent Jobs Conversion example
This repository contains MSSQL Agent Jobs "Conversion Rules" code samples that use groovy and [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) or [**Helix Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmsaasselfconv/control-m-saas-self-conversion-home-967323185.html) to convert sample MSSQL Agent Jobs input data into Control-M Data.<br> 
You can use these MSSQL Agent Jobs Conversion Rules code samples to convert your MSSQL Agent Jobs data to Control-M data, or use them as an example in using the [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) or [**Helix Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmsaasselfconv/control-m-saas-self-conversion-home-967323185.html) to create Control-M MSSQL Agent database jobs.

### The MSSQL Agent Jobs Conversion example includes:
* __SampleData.xml__ -MSSQL Agent Jobs sample data in XML format.
* __MappingLogic.xlsx__ - Holds the mapping logic used in this sample to convert from MSSQL Agent Jobs data to Control-M data.
* __MSSQLAgentJobs_ConversionRules.json__ - The MSSQL Agent Jobs Conversion Rules json file that holds the Self Conversion rules code samples.
* __ControlM_Result.xml__ - The Control-M data created by the Self-Conversion when converting the MSSQL Agent Jobs sample data using the MSSQL Agent Jobs conversion rules sample.
* __HelixControlM_Result.json__ - The Helix Control-M data created by the Helix Control-M Self-Conversion when converting the MSSQL Agent Jobs sample data using the MSSQL Agent Jobs conversion rules sample.

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

### MSSQL Agent Job mapping logic
|  MSSQL Agent Job Data       | Control-M Data                                |
| --------------------------- | --------------------------------------------- |
|  jobData.category           | Smart Folder                                  |
|  jobData.name               | Smart Folder Name                             |
|  jobData.name               | Job Name                                      |
|  jobData.server             | MSSQL database job connection profile         |

### Usage Instructions
1. Clone or download the repository.
2. Open Control-M Self Conversion.
3. Import the __MSSQL Agent Job Conversion Rules__ json file.
4. Create a new Self Conversion project: 
   * Enter a project name.
   * Load the **MSSQL Agent Jobs Sample Input Data**.
   * In "Use existing conversion rules" dropdown list, select the conversion rules imported in step 3.
   * Click "Create Project".
5. Click Run.
6. Review the conversion results.

## Instructions how to extract MSSQL Agent jobs to XML
1. Make sure you have python version 3.6 or higher installed 
2. download the [MSSQL Agent Jobs extract script](Data_export/extractFromMssqlAgentJobs.py) 
3. Run extractFromMssqlAgentJobs.py c:/workspace/python/extractFromMssqlAgentJobs.py -u user -p password -s database.example.com,1433 -r mssql_agent_sample_input_data.xml 
4. follow the instructions at [Usage Instructions](#usage-instructions)

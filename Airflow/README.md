# Airflow Conversion example
This repository contains Airflow "Conversion Rules" code samples that use groovy and [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) to convert sample Airflow input data into Control-M Data.<br>
You can use these Airflow Conversion Rules code samples to convert your Airflow data to Control-M data, or use them as an example in using the [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) to create Control-M Airflow jobs.

### The Airflow Conversion example includes:
* __SampleData.xml__ - Airflow sample data in XML format. [(Airflow data extraction)](#instructions-how-to-extract-airflow-workflows-to-xml)
* __MappingLogic.xlsx__ - Holds the mapping logic used in this sample to convert from Airflow data to Control-M data.
* __Airflow_ConversionRules.json__ - The Airflow Conversion Rules json file that holds the Self Conversion rules code samples.
* __ControlM_Result.xml__ - The Control-M data created by the Self-Conversion when converting the Airflow sample data using the Airflow conversion rules sample.
* __HelixControlM_Result.json__ - The Helix Control-M data created by the Helix Control-M Self-Conversion when converting the Airflow sample data using the Airflow conversion rules sample. 

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

### Airflow mapping logic
|  Airflow Data               | Control-M Data                                |
| --------------------------- | --------------------------------------------- | 
|  dag                        | Smart Folder                                  |
|  _dag_id                    | Smart Folder Name                             |
|  _description               | Smart Folder Description                      |
|  task_id                    | Job Name                                      |
|  _task_type                 | Job Description                               |
|  bash_operator _task_module | OS Job Definition                             |
|  MySqlOperator _task_module | EmbeddedQuery Database Job Definition         |
|  _downstream_task_id s item | In Condition and Out Condition between jobs   |

### Usage Instructions
1. Clone or download the repository.
2. Open Control-M Self Conversion.
3. Import the __Airflow Conversion Rules__ json file.
4. Create a new Self Conversion project:
   * Enter a project name.
   * Load the [Airflow Sample Input Data](#instructions-how-to-extract-airflow-workflows-to-xml).
   * In "Use existing conversion rules" dropdown list, select the conversion rules imported in step 3.
   * Click "Create Project".
5. Click Run.
6. Review the conversion results.

## Instructions how to extract Airflow workflows to XML
1. Connect to the Airflow database.
2. Make sure the Airflow installation supports [dag serialization](https://airflow.apache.org/docs/apache-airflow/stable/dag-serialization.html).
3. For each dag you want to export run query: `SELECT data FROM serialized_dag;`
4. For each dag copy the json content from the data column to a file and run the [extract_script](Data_export/jsonToXml.py) to convert it to xml.
5. Copy all dag xml files to one folder and follow the instructions at [Usage Instructions](#usage-instructions)
   <br>Example: `jsonToXml.py -j <json_file> -x <xml_file>`

## Contribution guide
To contribute, please follow these guidelines.

### Files, folders and naming conventions
1. Every conversion and its associated files must be contained in its own **folder**. Name this folder as the name of the tool that you convert from.
2. The __folder__ should contain:
   * __SampleData__ - A folder that holds tool sample Input Data in XML format that we want to convert to Control-M data.
   * __MappingLogic.xlsx__ - The mapping logic used for conversion in this sample, from the  tool sample input data to Control-M data.
   * __Airflow_ConversionRules.json__ - The tool Conversion Rules json file that contains the Self Conversion rules code.
   * __ControlM_Result.xml__ - The Control-M data created by the Self Conversion when converting the tool sample data using the Demo Tool conversion rules.

3. Include a **README.md** file that explains the sample. A good description helps other community members to understand your sample. The README.md uses [Github Flavored Markdown](https://guides.github.com/features/mastering-markdown/) for formatting text.
# Airflow Conversion example to Control-M Airflow jobs
This repository contains Airflow "Conversion Rules" code samples that use groovy and [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) or [**Helix Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmsaasselfconv/control-m-saas-self-conversion-home-967323185.html) to convert sample Airflow input data into Control-M Data.<br>
You can use these Airflow Conversion Rules code samples to convert your Airflow data to Control-M Airflow jobs, or use them as an example in using the [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) or [**Helix Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmsaasselfconv/control-m-saas-self-conversion-home-967323185.html) to create Control-M Airflow jobs.

### The Airflow Conversion example includes:
* __SampleData.xml__ - Airflow sample data in XML format. [(Airflow data extraction)](#instructions-how-to-extract-airflow-dags-from-airflow-api)
* __MappingLogic.xlsx__ - Holds the mapping logic used in this sample to convert from Airflow data to Control-M data.
* __AirFlowJobType_ConversionRules.json__ - The Airflow Conversion Rules json file that holds the Self Conversion rules code samples.
* __ControlM_Result.xml__ - The Control-M data created by the Self-Conversion when converting the Airflow sample data using the Airflow conversion rules sample.
* __HelixControlM_Result.json__ - The Helix Control-M data created by the Helix Control-M Self-Conversion when converting the Airflow sample data using the Airflow conversion rules sample. 

### Airflow mapping logic
|  Airflow Data               | Control-M Data                                |
| --------------------------- | --------------------------------------------- | 
|  item                       | Control-M Airflow Job                         |
|  dag_id                     | Control-M Airflow job dag ID                  |
|  schedule_interval          | Control-M Job Scheduling                      |

### Usage Instructions
1. Clone or download the repository.
2. Open Control-M Self Conversion.
3. Import the __Airflow Conversion Rules__ json file.
4. Create a new Self Conversion project:
   * Enter a project name.
   * Load the [Airflow Sample Input Data](#instructions-how-to-extract-airflow-dags-from-airflow-api).
   * In "Use existing conversion rules" dropdown list, select the conversion rules imported in step 3.
   * Click "Create Project".
5. Click Run.
6. Review the conversion results.

## Instructions how to extract Airflow dags from Airflow API
1. Make sure you are running Airflow version >= 2.0.0
2. Run the [extract_script](data_export/airflowDataExtract.py)
   <br>Example: `airflowDataExtract.py -u user -p password -e https://airflow.example.com:8080 -o /home/result.xml`
3. Import the extracted data to by following the instructions at [Usage Instructions](#usage-instructions)

## Contribution guide
To contribute, please follow these guidelines.

### Files, folders and naming conventions
1. Every conversion and its associated files must be contained in its own **folder**. Name this folder as the name of the tool that you convert from.
2. The __folder__ should contain:
   * __SampleData__ - A folder that holds tool sample Input Data in XML format that we want to convert to Control-M data.
   * __MappingLogic.xlsx__ - The mapping logic used for conversion in this sample, from the  tool sample input data to Control-M data.
   * __AirFlowJobType_ConversionRules.json__ - The tool Conversion Rules json file that contains the Self Conversion rules code.
   * __ControlM_Result.xml__ - The Control-M data created by the Self Conversion when converting the tool sample data using the Demo Tool conversion rules.
    * __HelixControlM_Result.json__ - The Helix Control-M data created by the Helix Control-M Self-Conversion when converting the tool sample data using the Demo Tool conversion rules.   

3. Include a **README.md** file that explains the sample. A good description helps other community members to understand your sample. The README.md uses [Github Flavored Markdown](https://guides.github.com/features/mastering-markdown/) for formatting text.
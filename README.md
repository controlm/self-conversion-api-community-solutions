# Control-M Self Conversion API community solutions  
This repository contains "Conversion Rules" code samples created for various Schedulers, Applications and Homegrown's tools.  
You can use those code examples to convert from those tools to Control-M using the Control-M Self-Conversion or as an example
for creating conversion rules using Groovy and [Conversion API](). 
# Online Documentation
For more information, see [**Control-M Self Conversion**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-817142681.html) and the [**Control-M Self Conversion API**](https://docs.bmc.com/docs/ctmselfconv/control-m-self-conversion-api-814570051.html) online documentation.
For Control-M Self Conversion Training Video click [**Here**.](https://www.youtube.com/watch?v=2MrFcahMhH0)
# Download Control-M Self-Conversion
To download the latest Control-M  Self Conversion:
  1) Go to: **ftp://ftp.bmc.com/pub/control-m/opensystem/Control-M_Conversions_for_DS/**
  2) Download ConversionTool.zip file
  3) Extract it
  4) Click Self-Conversion.bat

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

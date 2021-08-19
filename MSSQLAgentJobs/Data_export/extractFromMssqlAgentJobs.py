import sys
import pyodbc
import getopt
import xml.etree.cElementTree as ET


def usage():
    print('Extract MSSQL Agent Jobs from MSSQL server')
    print(
        f'Usage: {sys.argv[0]} -u <mssql username> -p <mssql password> -s <mssql server name[,port]> -r [result output path]')
    print(
        f'Example1: {sys.argv[0]} -u user -p password -s database.example.com,1433 -r result.xml')
    print(
        f'Example2: {sys.argv[0]} -u user -p password -s database.example.com')
    sys.exit(2)

def parse_arguments(argv, username=None, password=None, server=None, result=None):
    try:
        opts, _ = getopt.getopt(argv, 'hu:p:s:r:')
        for opt, arg in opts:
            if opt == '-h':
                usage()
            elif opt in ('-u'):
                username = arg
            elif opt in ('-p'):
                password = arg
            elif opt in ('-s'):
                server = arg
            elif opt in ('-r'):
                result = arg
        if not username or not password or not server:
            raise getopt.GetoptError('Missing mandatory argument')
        return username, password, server, result
    except getopt.GetoptError as e:
        print(e)
        usage()


def query_agent_jobs(server, user, password, odbc_driver="ODBC Driver 17 for SQL Server"):
    try:
        connection = pyodbc.connect(f"DRIVER={{{odbc_driver}}};SERVER={server};DATABASE=master;UID={user};PWD={password}")
    except Exception as err:
        print(f"Login failed for {user}@{server} \n\t{str(err)}")
        return None
    cursor = connection.cursor()
    select_agent_query = """
        SELECT job.name,category.name, server.name 
        FROM 
            [msdb].[dbo].[sysjobs] job, 
            [msdb].[dbo].[syscategories] category,
            [msdb].[sys].[servers] server 
        WHERE 
            job.category_id = category.category_id and job.originating_server_id = server.server_id;"""
    cursor.execute(select_agent_query)
    return cursor.fetchall()


def query_to_xml(rows, filename):
    root = ET.Element("SQLAgentJobs")
    for row in rows:
        job_name, category, server = row
        ET.SubElement(root, "JobData", name=job_name,
                      category=category, server=server)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)

    if(filename):
        tree.write(filename)
    else:
        xmlstr = ET.tostring(root, encoding='utf8', method='xml')
        print(xmlstr.decode('utf8'))


def is_valid_python_version():
    major = sys.version_info[0]
    minor = sys.version_info[1]
    return major >= 3 and minor >= 6


if __name__ == '__main__':
    if not is_valid_python_version():
        print("This utility requires python version >= 3.6")
        sys.exit(3)
    
    username, password, server, filename = parse_arguments(sys.argv[1:])
    rows = query_agent_jobs(server, username, password)
    if rows:
        query_to_xml(rows, filename)

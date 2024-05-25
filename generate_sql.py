import argparse
import os
from generate_temp_table_sql.sql_generator import SQLGenerator

def main():
    parser = argparse.ArgumentParser(description='Process a CSV file to generate SQL statements.')
    parser.add_argument('csv_file', type=str, help='The path to the CSV file')
    parser.add_argument('-o', '--output_file', type=str, help='The path to the output SQL file', default=None)

    args = parser.parse_args()
    
    if args.output_file is None:
        base_name = os.path.splitext(args.csv_file)[0]
        args.output_file = os.path.join(os.getcwd(), base_name + '_temp_table.sql')

    
    sql_generator = SQLGenerator(args.csv_file)
    
    sql_generator.load_csv()
    
    create_table_sql, insert_data_sql = sql_generator.generate_sql('temp_table')
    
    with open(args.output_file, 'w') as f:
        f.write("--Create Table SQL:\n")
        f.write(create_table_sql + "\n\n")
        f.write("--Insert Data SQL:\n")
        for query in insert_data_sql:
            f.write(query + "\n")

if __name__ == '__main__':
    main()



# csv_file_path = 'tests/data/test_data.csv'

# sql_generator = SQLGenerator(csv_file_path)
# create_table_sql, insert_data_sql = sql_generator.generate_sql('your_temp_table')

# print("--Create Table SQL:")
# print(create_table_sql)

# print("\n--Insert Data SQL:")
# for insert_query in insert_data_sql:
#     print(insert_query) 
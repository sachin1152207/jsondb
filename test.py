from main import jsondb

js = jsondb("db.json", intent=4)
schema= {"name":"STRING","email":"STRING","address":"STRING","username":"STRING","password":"STRING","phoneNumber": "INTEGER","salary":"FLOAT"}
js.createTable(tableName="Employee",tableSchema=schema)


data = [
    ["Sachin Shrivastav", "sachinshrivastav152207@gmail.com", "Gaur 9", "sachin1542", "Sachin@9845", 9845123456, 1542.00],
    ["John Doe", "johndoe@gmail.com", "123 Main St", "john123", "John@456", 1234567890, 2500.00],
    ["Jane Smith", "janesmith@gmail.com", "456 Oak Ave", "jane456", "Jane@789", 9876543210, 3000.00],
    ["Alice Johnson", "alicejohnson@gmail.com", "789 Elm St", "alice789", "Alice@1011", 5554443333, 2800.00],
    ["Bob Brown", "bobbrown@gmail.com", "1011 Pine St", "bob1011", "Bob@1213", 1112223333, 3200.00],
    ["Michael Williams", "michaelwilliams@gmail.com", "1213 Cedar Ave", "mike1213", "Mike@1415", 3332221111, 2700.00],
    ["Emily Davis", "emilydavis@gmail.com", "1415 Walnut St", "emily1415", "Emily@1617", 9998887777, 2900.00],
    ["David Wilson", "davidwilson@gmail.com", "1617 Maple Ave", "david1617", "David@1819", 7776665555, 2600.00],
    ["James Taylor", "jamestaylor@gmail.com", "1819 Oak St", "james1819", "James@2021", 4445556666, 3100.00],
    ["Sarah Martinez", "sarahmartinez@gmail.com", "2021 Elm Ave", "sarah2021", "Sarah@2223", 6667778888, 3300.00],
    ["Christopher Garcia", "christophergarcia@gmail.com", "2223 Pine St", "chris2223", "Chris@2425", 2223334444, 2800.00],
    ["Jessica Rodriguez", "jessicarodriguez@gmail.com", "2425 Cedar Ave", "jessica2425", "Jessica@2627", 8889991111, 2900.00],
    ["Matthew Hernandez", "matthewhernandez@gmail.com", "2627 Walnut St", "matthew2627", "Matthew@2829", 5554447777, 3000.00],
    ["Daniel Lopez", "daniellopez@gmail.com", "2829 Maple Ave", "daniel2829", "Daniel@3031", 1112223333, 3100.00],
    ["Ashley Gonzalez", "ashleygonzalez@gmail.com", "3031 Oak St", "ashley3031", "Ashley@3233", 9998887777, 3200.00],
    ["Andrew Perez", "andrewperez@gmail.com", "3233 Elm Ave", "andrew3233", "Andrew@3435", 3332221111, 3300.00],
    ["Taylor Morgan", "taylormorgan@gmail.com", "3435 Pine St", "taylor3435", "Taylor@3637", 7776665555, 3400.00],
    ["Joshua Cook", "joshuacook@gmail.com", "3637 Cedar Ave", "joshua3637", "Joshua@3839", 6665554444, 3500.00],
    ["Lauren Hill", "laurenhill@gmail.com", "3839 Walnut St", "lauren3839", "Lauren@4041", 4443332222, 3600.00],
    ["Brandon Scott", "brandonscott@gmail.com", "4041 Maple Ave", "brandon4041", "Brandon@4243", 2221110000, 3700.00],
]

x = js.insertRow(tableName="Employee", rows=data)
js.save()

x = js.fetchOne(("OBJECT_ID", [1,6,5,4]), tableName="Employee", field=["name"])

print(x)


import psutil

# Get the current process's memory usage
process = psutil.Process()
memory_info = process.memory_info()

# Convert bytes to megabytes
memory_usage_mb = memory_info.rss / (1024.0 * 1024.0)

# Print the memory usage in megabytes
print("Memory usage (in MB):", memory_usage_mb)



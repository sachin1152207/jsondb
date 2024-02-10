import json
from package import *
class jsondb:
    def __init__(self, filePath:str, intent:int):
        self.model = None
        self.filePath = filePath
        self.intent = intent
        self.available_dtype = ["STRING", "INTEGER", "BOOL", "FLOAT"]
        try:
            with open(self.filePath, 'r') as model:
                self.model = json.load(model)
        except(FileNotFoundError):
            with open(self.filePath, 'w') as model:
                json.dump({}, model, indent=self.intent)
        self.model = json.load(open(self.filePath, 'r+'))
    # Commit
    def save(self):
        with open(self.filePath, 'w') as model:
            json.dump(self.model, model, indent=self.intent)
        return True
    # Create Table with Schema
    def createTable(self, tableName:str, tableSchema:dict):
        tableValidSchema ={"<TABLE_SCHEMA>":{"OBJECT_ID":"INTEGER"}}
        for schema, dtype in tableSchema.items():
            if dtype in self.available_dtype:
                tableValidSchema["<TABLE_SCHEMA>"][schema]=dtype
            else:
                print(f"Dtype error: {dtype} is not valid data type.")
                break

        self.model[tableName] = tableValidSchema
        self.model[tableName]["<TABLE_ROW>"] = []
        return f"Change applied: {len(tableValidSchema)-1} column added."
    # insertRow
    def insertRow(self, tableName:str, rows:list):
        try:

            self.model[tableName]["<TABLE_ROW>"]
            cloumnDtype = [dtype for dtype in self.model[tableName]["<TABLE_SCHEMA>"].values()]
            columnName = [dtype for dtype in self.model[tableName]["<TABLE_SCHEMA>"].keys()]
            insertedRow = 0
            for indx, row in enumerate(rows):
                validRow =  True
                OBJECT_ID = len(self.model[tableName]["<TABLE_ROW>"]) + 1
                row.insert(0, OBJECT_ID)

                for index, data in enumerate(row):

                    if getDtype(data) !=  cloumnDtype[index]:
                        print(f"Dtype error: at {indx} '{data}' is not valid data type for cloumn '{columnName[index]}'.")
                        validRow = False
                        break

                if validRow:
                    self.model[tableName]["<TABLE_ROW>"].append(row)
                    insertedRow +=1
            return f"Change applied: {insertedRow} row inserted."
        except(KeyError):
            print(f"Entry error: '{tableName}' named table not found.")
            return None
    # FetchOne Row
    def fetchOne(self, filter:tuple, tableName:str, field:list=[]):
        try:
            row = self.model[tableName]["<TABLE_ROW>"]
            columnName = [dtype for dtype in self.model[tableName]["<TABLE_SCHEMA>"].keys()]
            field = columnName if len(field) == 0 else field
            resultRow = []
            if filter[0] in columnName:
                for index, elemt in enumerate(row):
                    if elemt[columnName.index(filter[0])] in list(filter[1]):
                        tempData = {}
                        for indx, data in enumerate(elemt):
                            if columnName[indx] in field:
                                tempData[columnName[indx]]=data
                        resultRow.append(tempData)
            return resultRow
        except(KeyError):
            print(f"Entry error: '{tableName}' named table not found.")
            return None
    # FetchAll Row
    def fetchAll(self, tableName:str,field:list=[]):
        try:
            row = self.model[tableName]["<TABLE_ROW>"]
            columnName = [dtype for dtype in self.model[tableName]["<TABLE_SCHEMA>"].keys()]
            field = columnName if len(field) == 0 else field
            resultRow = []
            for data in row:
                tempData = {}
                for indx, data in enumerate(data):
                    if columnName[indx] in field:
                        tempData[columnName[indx]]=data
                resultRow.append(tempData)
            return resultRow
        except(KeyError):
            print(f"Entry error: '{tableName}' named table not found.")
            return None
    # DeleteOne
    def deleteOne(self, filter:tuple, tableName:str, commit:bool=False):
        try:
            row = self.model[tableName]["<TABLE_ROW>"]
            columnName = [dtype for dtype in self.model[tableName]["<TABLE_SCHEMA>"].keys()]
            deletedRow = 0
            if filter[0] in columnName:
                for index, elemt in enumerate(row):
                    if elemt[columnName.index(filter[0])] == filter[1]:
                        self.model[tableName]["<TABLE_ROW>"].pop(index)
                        deletedRow += 1
            self.save() if commit else ""
            return f"Change applied: {deletedRow} column deleted."
        except(KeyError):
            print(f"Entry error: '{tableName}' named table not found.")
            return None
    # DeleteMany
    def deleteMany(self, filter:tuple, tableName:str, commit:bool=False):
        try:
            row = self.model[tableName]["<TABLE_ROW>"]
            columnName = [dtype for dtype in self.model[tableName]["<TABLE_SCHEMA>"].keys()]
            deletedRow = 0
            if filter[0] in columnName:
                for index, elemt in enumerate(row):
                    if elemt[columnName.index(filter[0])] in filter[1]:
                        self.model[tableName]["<TABLE_ROW>"].pop(index)
                        deletedRow += 1
            self.save() if commit else ""
            return f"Change applied: {deletedRow} column deleted."
        except(KeyError):
            print(f"Entry error: '{tableName}' named table not found.")
            return None
    # UpdateOne
    def updatOne(self, filter:tuple, newData:dict, tableName:str,commit:bool=False):
        ("name","Sachin Shrivastav")
        {
            "name":"New Name",
            "email":"newemail@gmail.com"
        }
        try:
            row = self.model[tableName]["<TABLE_ROW>"]
            columnName = [dtype for dtype in self.model[tableName]["<TABLE_SCHEMA>"].keys()]
            newDataKeys = [key for key in newData.keys()]
            updatedRow = []
            rowCount = 0 
            if filter[0] in columnName:
                for index, elemt in enumerate(row):
                    
                    if elemt[columnName.index(filter[0])] == filter[1]:
                        for key in newDataKeys:
                            elemt[columnName.index(key)] = newData[key]
                        updatedRow.append(elemt)
                        rowCount += 1
                        self.model[tableName]["<TABLE_ROW>"].pop(index)
            self.model[tableName]["<TABLE_ROW>"].extend(updatedRow)
            self.save() if commit else ""
            return f"Change applied: {rowCount} column deleted."
        except(KeyError):
            print(f"Entry error: '{tableName}' named table not found.")
            return None
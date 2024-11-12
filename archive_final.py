from datetime import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://admin:passwordone@12nov24-cvcie.dublin-irl.a.query.mongodb.net/?ssl=true&authSource=admin&appName=12nov24')
db = client.get_database('airbnb')
coll = db.get_collection('listings')
prefix = '12nov24vdj_3daac9379fa178d234c39e6a6dfc0117'
initials = 'vdj'

pipeline = [
   
    {
        '$out': {
            's3': {
                'bucket': 'ps-ilt-atlas-datalake',
                'region': 'eu-west-1',
                'filename': prefix+'/reviews-parquet/'+initials,
                'format' : {
                    'name' : 'parquet',
                    'maxFileSize' : '10GB',
                    'maxRowGroupSize' : '100MB',
			   	    'columnCompression' : 'gzip'
                }

            }
        }
    }
]

coll.aggregate(pipeline)
print('Archive created!')

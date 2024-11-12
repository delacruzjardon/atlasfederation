# DS120 - 03 - Atlas Data Federation Administration and Data Formats


# Requirements

- Python 3
- install required libs: `pip3 install -r requirements.txt`

# Step 0
Check that the Federated Database Instance is 'eu-west-1'
# Step 1

Create the view
```
use sample_airbnb
db.runCommand({ 
    "create" : "listings", 
    "viewOn" : "listingsAndReviews", 
    "pipeline" : [
    { $addFields: { reviewCount: { $size: "$reviews" } } },
    { $match: { reviewCount: { $gt: 10 } } },
    { $project: { name: 1, reviewCount: 1, latestReviews: { $slice: [ "$reviews", -10 ] } } }
    ] 
})
```

# Step 2 
Copy configurationatlasfederation.json to your own Atlas Data Federation configuration and save


# Step 3 
Change the values from archive_final.py with your own information ( client, prefix and initials) and save

# Step 4 
Run archive_final.py  ( python3 archive_final.py )


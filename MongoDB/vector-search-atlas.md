#

## Define the Vector Search Index

Define the Vector Search Index in a JSON file:

> Define the data and collection you want to index. Designate the type as vectorSearch and create a name that allows you to easily identify the purpose of the index. Finally, define the fields being indexed, and specify the type, number of dimensions, and similarity.

```json
{
  "database": "sample_mflix",
  "collectionName": "movies",
  "type": "vectorSearch",
  "name": "movies_vector_index",
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": 1536,
      "similarity": "cosine"
    }
  ]
}
```

## Create the Index

Use atlas clusters search indexes create to create the index using a JSON file like the example above. You’ll need to pass in the name of the cluster and the path to the file. Note that depending on how you authenticate, you may need to first specify the appropriate projectID

```.sh
atlas clusters search indexes create \
    --clusterName vector \
    --file index.json<?code>
```

### Confirmation

Successful creation of the index should return a confirmation message like this:

`Index movies_vector_index created.`

## Checking Your Indexes

> To check on the status of an index (or multiple indexes) you can use the `atlas clusters search indexes list` command. You’ll need to specify the names of the cluster, database, and collection for the index. In this example, we are requesting that the output be formatted in JSON.

```.sh
atlas clusters search indexes list \
    --clusterName vector \
    --db test_mflix \
    --collection movies \
    --output json
```

This will return an array which will include information on each index within the specified collection.

```.bson
[
  {
    "collectionName": "movies",
    "database": "test_mflix",
    "indexID": "66720dec75b489672353910b",
    "name": "movies_vector_index",
    "status": "STEADY",
    "type": "vectorSearch",
    "fields": [
      {
        "numDimensions": 1536,
        "path": "embedding",
        "similarity": "cosine",
        "type": "vector"
      }
    ]
  }
]
```

## Looking Up a Specific Index

To see information for a specific index, you can use the atlas clusters search indexes describe command and pass in the index ID, like so:

```
atlas clusters search indexes describe <id_placeholder> \
    --clusterName vector \
    --output json
```

This will return information about the index specified. Note that this is a single document, and not an array.

```.bson
{
  "collectionName": "movies",
  "database": "test_mflix",
  "indexID": "66720dec75b489672353910b",
  "name": "movies_vector_index",
  "status": "STEADY",
  "type": "vectorSearch",
  "fields": [
    {
      "numDimensions": 1536,
      "path": "embedding",
      "similarity": "cosine",
      "type": "vector"
    }
  ]
}
```

## Updating an Existing Index

> Here, we’ve added a filter to the index definition JSON file:

```JSON
{
  "database": "test_mflix",
  "collectionName": "movies",
  "type": "vectorSearch",
  "name": "movies_vector_index",
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": 1536,
      "similarity": "cosine"
    },
    {
      "type": "filter",
      "path": "year"
    }
  ]
}
```

We can then use the atlas clusters search indexes update command to overwrite the existing index (specified via the indexID) with the new definition:

```.sh
atlas clusters search indexes update <id_placeholder> \
    --clusterName vector \
    --file index.json \
    --output json
```

The confirmation message will look like this:

```JSON
{
  "collectionName": "movies",
  "database": "test_mflix",
  "indexID": "66720dec75b489672353910b",
  "name": "movies_vector_index",
  "status": "IN_PROGRESS",
  "type": "vectorSearch",
  "fields": [
    {
      "numDimensions": 1536,
      "path": "embedding",
      "similarity": "cosine",
      "type": "vector"
    },
    {
      "path": "year",
      "type": "filter"
    }
  ]
}
```

> [!NOTE]
> The filter we added to the JSON definition file is now included in the index, and that the status is listed as “IN_PROGRESS”. This will change to “STEADY” when it is finished being rebuilt. Queries which would benefit from the index will continue to use the original version until the update is complete.

## Deleting an Index

To delete an index use the atlas clusters search indexes delete command. You’ll need to specify the indexID and the name of the cluster the index resides on.

```.sh
atlas clusters search indexes delete <id_placeholder> \
    --clusterName vector
```

After running the command, you’ll be prompted to enter `y` to confirm the deletion, and you will receive a confirmation message:

```
? Are you sure you want to delete: <id_placeholder> (y/N) y
Index '<id_placeholder>' deleted
```

You may confirm the deletion of the index by running the atlas clusters search indexes list command:

```.sh
atlas clusters search indexes list \
    --clusterName vector \
    --db test_mflix \
    --collection movies \
    --output json
```

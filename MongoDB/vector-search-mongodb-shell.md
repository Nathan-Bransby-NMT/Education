# Creating a Vector Search Index Using MongoDB Shell

Use the db.collection.createSearchIndex command to build an index on a collection. You must specify the type of index as vectorSearch, and you will need to define the fields you wish to index, including the type, number of dimensions, and similarity.

```Shell
db.movies.createSearchIndex(
  "movies_vector_index", 
  "vectorSearch", 
  {
    "fields": [
      {
        "type": "vector",
        "numDimensions": 1536,
        "path": "plot_embedding",
        "similarity": "cosine",
      }
    ],
  }
);
```

After running the command, you will receive a confirmation message with the name of the new index:

`movies_vector_index`

## Viewing an Existing Index

Use the db.collection.getSearchIndexes command and leave it blank in order to see all indexes on the specified collection:

```shell
db.movies.getSearchIndexes();
```

If you wish to specify a particular index, pass in the name of the index as an argument:

```shell
db.movies.getSearchIndexes("movies_vector_index");
```

This will return a lot of information about the index, including the status, which will let you know if the index is ready or still being prepared. It will also show the current definition of the index.
```shell
[
  {
    id: "6671e934b362ed3c6ad84512",
    name: "movies_vector_index",
    type: "vectorSearch",
    status: "READY",
    queryable: true,
    latestDefinitionVersion: { version: 0, createdAt: ISODate("2024-06-18T20:08:20.678Z") },
    latestDefinition: {
      fields: [
        {
          type: "vector",
          numDimensions: 1536,
          path: "plot_embedding",
          similarity: "cosine"
        },
      ],
    },
    statusDetail: [
      . . .
    ],
  },
];
```

Note the statusDetail array in the above example. This array contains an index status array for each node in the cluster.

```shell
[
  {
    . . .
    statusDetail: [
      {
        hostname: "atlas-11yyiw-shard-00-02",
        status: "READY",
        queryable: true,
        mainIndex: {
          status: "READY",
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2024-06-18T20:08:20.000Z"),
          },
          definition: { fields: [[Object]] },
        },
      },
      . . .
    ]
  },
];
```

## Editing an Existing Vector Search Index

Update the definition of an existing vector search index with the db.collection.updateSearchIndex command. In this example, we’ll add a filter on the year field.

```shell
db.movies.updateSearchIndex(
  "movies_vector_index", 
  {
    "fields": [
      {
        "type": "vector",
        "numDimensions": 1536,
        "path": "embedding",
        "similarity": "cosine",
      },
      {
        "type": "filter",
        "path": "year",
      }
    ],
  }
);
```

Using `db.movies.getSearchIndexes("movies_vector_index")`, we can confirm that the update was successful:

```shell
[
  {
    id: "6671e934b362ed3c6ad84512",
    name: "movies_vector_index",
    type: "vectorSearch",
    status: "READY",
    queryable: true,
    latestDefinitionVersion: { version: 1, createdAt: ISODate("2024-06-18T20:08:25.348Z") },
    latestDefinition: {
      fields: [
        {
          type: "vector",
          numDimensions: 1536,
          path: "plot_embedding",
          similarity: "cosine"
        },
     { type: 'filter', path: 'year' }
      ],
    },
    statusDetail: [
      . . .
    ],
  },
];
```

## Deleting a Vector Search Index

Delete a vector search index with the db.collection.dropSearchIndex command and pass the name of the vector along as an argument:

```shell
db.movies.dropSearchIndex("movies_vector_index");
```

Running this command will not produce any feedback from the console, so to confirm that the deletion was successful, you can use the db.collection.getSearchIndexes command:

```shell
db.movies.getSearchIndexes("movies_vector_index");
```

This will return the information we’re accustomed to seeing when we run this command. In this case, we can see that the status is listed as “DELETING”, so we know the deletion was successful. We can also run getSearchIndexes again later without specifying an index name, and see that it is no longer present on the collection.

```shell
[
  {
    id: "6671e934b362ed3c6ad84512",
    name: "movies_vector_index",
    type: "vectorSearch",
    status: "DELETING",
    queryable: true,
    latestDefinitionVersion: { version: 1, createdAt: ISODate("2024-06-18T20:08:25.348Z") },
    latestDefinition: {
      fields: [
        {
          type: "vector",
          numDimensions: 1536,
          path: "plot_embedding",
          similarity: "cosine"
        },
     { type: 'filter', path: 'year' }
      ],
    },
    statusDetail: [
      . . .
    ],
  },
];
```
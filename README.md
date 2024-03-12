# map-reduce

## Steps to run

1. `./build.sh`
2. `./count.sh`

### How to cleanup?

`./clean.sh`

## About the project

- Uses map-reduce to count the number of words in a set of text files
- Uses a single container, which uses an environment variable to run a mapper or a reducer
- Creates 9 mappers, each of which exposes a FastAPI endpoint, which when queried writes out `data/counts/{i}.json`
- The reducer queries each of the mappers on the FastAPI endpoints, and creates `data/counts/total_count.json`, which is the sum of all `data/counts/{i}.json`

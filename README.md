# winsysfind
Windows System File Finder scans your disk to index all files and provides a browser text search with instantaneous search results as you type
* Under 20 seconds for 100 GB on M.2

# Roadmap
## **Indexer** _creates a list of the files on the system_
 - Switch to [trie](https://en.wikipedia.org/wiki/Trie) data structure
    - Significant index file/memory footprint reduction
    - Potential speed improvements on finds
 - Use [thread pooling](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor)
    - Improve index disk read performance (I/O bound)
 - Support additional disk drives, not just the primary or C:\
 - Fetch metadata for files, size, modified, etc. for finding filters
 - Support excluding files and folders
    - By name contains, endswith, startswith string

## **App** _provides a web interface for querying the index_
 - Add at least minimal CSS
 - Clickable paths
 - ~~Move HTML and JS to separate files~~
 - ~~Create a button for refreshing the index~~
    - ~~Preferably without blocking~~
 - Visualizations
    - Space taken by filename or grouped by type (extension)
 - Request results before total occurrence count and only if its greater

## **Finder** _iterates over the index with a search term and returns matches_
 - Support AND, OR, and NOT operators
 - Query by recently size, accessed, modified, created
    - ST_SIZE, ST_ATIME, ST_MTIME, ST_CTIME

##Overview##
All operations (search and sync) will be use all configured indexers when they run, with the exception of Womble's which supports sync only.

When searching, drone will request the first 100 results, if more than 90 successful results are returned it will request the next 100 results from the indexer, to a maximum of 1000 results. If the indexer doesn't support paging, we make every effort to avoid requesting additional results.

##Recent Releases Feed##
This is the indexer's latest TV releases, which usually contains 100 releases. By default drone fetches this feed every 15 minutes, configurable on Settings-> Indexers (with advanced settings visible).

##Episode Search##
Performs a search to each configured indexer with for a single episode. In the case of Missing's "Search Selected" it will trigger a search for each selected episode individually.

##Season Search##
When searching for a full season (from the Series' details page) drone will make a single call for the first page of results, if additional results are available them drone will request them as well.

##Series Search##
Each season is searched individually and follows the normal season searching as outlined above.
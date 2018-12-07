# tvdb_api_v2

[![Build Status](https://travis-ci.org/h3llrais3r/tvdb_api_v2.svg?branch=master)](https://travis-ci.org/h3llrais3r/tvdb_api_v2)
[![Coverage Status](https://coveralls.io/repos/github/h3llrais3r/tvdb_api_v2/badge.svg)](https://coveralls.io/github/h3llrais3r/tvdb_api_v2)
[![Requirements Status](https://requires.io/github/h3llrais3r/tvdb_api_v2/requirements.svg?branch=master)](https://requires.io/github/h3llrais3r/tvdb_api_v2/requirements/?branch=master)
[![License](https://img.shields.io/github/license/h3llrais3r/tvdb_api_v2.svg)](https://github.com/h3llrais3r/tvdb_api_v2/blob/master/LICENSE)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.2.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

**See requirements.txt for details**

- certifi
- six
- python-dateutil
- setuptools
- urllib3

## Implemented methods

### Authentication api
- login
- refresh_token
- clear_token

### Search api
- search_series_by_name
- search_series_by_imdb_id

### Series api
- get_series
- get_series_episodes
- get_series_episode
- get_series_episode_by_absolute_number
- get_series_images_count
- get_series_images
- get_series_highest_rated_image

### Episodes api
- get_episode

### Updates api
- get_updates

## Documentation for our client wrapper (tvdb_client)

```python
from tvdb_api_v2.client import TvdbClient

# create instance with your api key
client = TvdbClient(api_key='yourtvdbapikey', user_agent='youruseragent')
# login to authenticate
client.login()
# execute desired method (you can choose from the implemented methods listed above)
client.search_series_by_name('yourseriesname')
...
```

## Documentation for API Endpoints

**Check this if you want to use the library without using the provided client**

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**login_post**](docs/AuthenticationApi.md#login_post) | **POST** /login | 
*AuthenticationApi* | [**refresh_token_get**](docs/AuthenticationApi.md#refresh_token_get) | **GET** /refresh_token | 
*EpisodesApi* | [**episodes_id_get**](docs/EpisodesApi.md#episodes_id_get) | **GET** /episodes/{id} | 
*LanguagesApi* | [**languages_get**](docs/LanguagesApi.md#languages_get) | **GET** /languages | 
*LanguagesApi* | [**languages_id_get**](docs/LanguagesApi.md#languages_id_get) | **GET** /languages/{id} | 
*SearchApi* | [**search_series_get**](docs/SearchApi.md#search_series_get) | **GET** /search/series | 
*SearchApi* | [**search_series_params_get**](docs/SearchApi.md#search_series_params_get) | **GET** /search/series/params | 
*SeriesApi* | [**series_id_actors_get**](docs/SeriesApi.md#series_id_actors_get) | **GET** /series/{id}/actors | 
*SeriesApi* | [**series_id_episodes_get**](docs/SeriesApi.md#series_id_episodes_get) | **GET** /series/{id}/episodes | 
*SeriesApi* | [**series_id_episodes_query_get**](docs/SeriesApi.md#series_id_episodes_query_get) | **GET** /series/{id}/episodes/query | 
*SeriesApi* | [**series_id_episodes_query_params_get**](docs/SeriesApi.md#series_id_episodes_query_params_get) | **GET** /series/{id}/episodes/query/params | 
*SeriesApi* | [**series_id_episodes_summary_get**](docs/SeriesApi.md#series_id_episodes_summary_get) | **GET** /series/{id}/episodes/summary | 
*SeriesApi* | [**series_id_filter_get**](docs/SeriesApi.md#series_id_filter_get) | **GET** /series/{id}/filter | 
*SeriesApi* | [**series_id_filter_params_get**](docs/SeriesApi.md#series_id_filter_params_get) | **GET** /series/{id}/filter/params | 
*SeriesApi* | [**series_id_get**](docs/SeriesApi.md#series_id_get) | **GET** /series/{id} | 
*SeriesApi* | [**series_id_head**](docs/SeriesApi.md#series_id_head) | **HEAD** /series/{id} | 
*SeriesApi* | [**series_id_images_get**](docs/SeriesApi.md#series_id_images_get) | **GET** /series/{id}/images | 
*SeriesApi* | [**series_id_images_query_get**](docs/SeriesApi.md#series_id_images_query_get) | **GET** /series/{id}/images/query | 
*SeriesApi* | [**series_id_images_query_params_get**](docs/SeriesApi.md#series_id_images_query_params_get) | **GET** /series/{id}/images/query/params | 
*UpdatesApi* | [**updated_query_get**](docs/UpdatesApi.md#updated_query_get) | **GET** /updated/query | 
*UpdatesApi* | [**updated_query_params_get**](docs/UpdatesApi.md#updated_query_params_get) | **GET** /updated/query/params | 
*UsersApi* | [**user_favorites_get**](docs/UsersApi.md#user_favorites_get) | **GET** /user/favorites | 
*UsersApi* | [**user_favorites_id_delete**](docs/UsersApi.md#user_favorites_id_delete) | **DELETE** /user/favorites/{id} | 
*UsersApi* | [**user_favorites_id_put**](docs/UsersApi.md#user_favorites_id_put) | **PUT** /user/favorites/{id} | 
*UsersApi* | [**user_get**](docs/UsersApi.md#user_get) | **GET** /user | 
*UsersApi* | [**user_ratings_get**](docs/UsersApi.md#user_ratings_get) | **GET** /user/ratings | 
*UsersApi* | [**user_ratings_item_type_item_id_delete**](docs/UsersApi.md#user_ratings_item_type_item_id_delete) | **DELETE** /user/ratings/{itemType}/{itemId} | 
*UsersApi* | [**user_ratings_item_type_item_id_item_rating_put**](docs/UsersApi.md#user_ratings_item_type_item_id_item_rating_put) | **PUT** /user/ratings/{itemType}/{itemId}/{itemRating} | 
*UsersApi* | [**user_ratings_query_get**](docs/UsersApi.md#user_ratings_query_get) | **GET** /user/ratings/query | 
*UsersApi* | [**user_ratings_query_params_get**](docs/UsersApi.md#user_ratings_query_params_get) | **GET** /user/ratings/query/params | 

## Documentation For Models

 - [Auth](docs/Auth.md)
 - [BasicEpisode](docs/BasicEpisode.md)
 - [Conflict](docs/Conflict.md)
 - [Episode](docs/Episode.md)
 - [EpisodeDataQueryParams](docs/EpisodeDataQueryParams.md)
 - [EpisodeLanguageInfo](docs/EpisodeLanguageInfo.md)
 - [EpisodeRecordData](docs/EpisodeRecordData.md)
 - [FilterKeys](docs/FilterKeys.md)
 - [JSONErrors](docs/JSONErrors.md)
 - [Language](docs/Language.md)
 - [LanguageData](docs/LanguageData.md)
 - [Links](docs/Links.md)
 - [NotAuthorized](docs/NotAuthorized.md)
 - [NotFound](docs/NotFound.md)
 - [Series](docs/Series.md)
 - [SeriesActors](docs/SeriesActors.md)
 - [SeriesActorsData](docs/SeriesActorsData.md)
 - [SeriesData](docs/SeriesData.md)
 - [SeriesEpisodes](docs/SeriesEpisodes.md)
 - [SeriesEpisodesQuery](docs/SeriesEpisodesQuery.md)
 - [SeriesEpisodesQueryParams](docs/SeriesEpisodesQueryParams.md)
 - [SeriesEpisodesSummary](docs/SeriesEpisodesSummary.md)
 - [SeriesImageQueryResult](docs/SeriesImageQueryResult.md)
 - [SeriesImageQueryResultRatingsInfo](docs/SeriesImageQueryResultRatingsInfo.md)
 - [SeriesImageQueryResults](docs/SeriesImageQueryResults.md)
 - [SeriesImagesCount](docs/SeriesImagesCount.md)
 - [SeriesImagesCounts](docs/SeriesImagesCounts.md)
 - [SeriesImagesQueryParam](docs/SeriesImagesQueryParam.md)
 - [SeriesImagesQueryParams](docs/SeriesImagesQueryParams.md)
 - [SeriesSearchResult](docs/SeriesSearchResult.md)
 - [SeriesSearchResults](docs/SeriesSearchResults.md)
 - [Token](docs/Token.md)
 - [Update](docs/Update.md)
 - [UpdateData](docs/UpdateData.md)
 - [UpdateDataQueryParams](docs/UpdateDataQueryParams.md)
 - [User](docs/User.md)
 - [UserData](docs/UserData.md)
 - [UserFavorites](docs/UserFavorites.md)
 - [UserFavoritesData](docs/UserFavoritesData.md)
 - [UserRatings](docs/UserRatings.md)
 - [UserRatingsData](docs/UserRatingsData.md)
 - [UserRatingsDataNoLinks](docs/UserRatingsDataNoLinks.md)
 - [UserRatingsDataNoLinksEmptyArray](docs/UserRatingsDataNoLinksEmptyArray.md)
 - [UserRatingsQueryParams](docs/UserRatingsQueryParams.md)

## Documentation For Authorization

## jwtToken

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

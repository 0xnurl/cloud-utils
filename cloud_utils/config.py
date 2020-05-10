import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

VERSIONS_FILE_PATH = os.getenv("VERSIONS_FILE_PATH", ".versions.json")
AUTO_UPDATING_CACHE = os.getenv("AUTO_UPDATING_CACHE")
BUCKET_NAME = os.getenv("BUCKET_NAME", "nlu-cache")

EXTERNAL_API_CACHE_REDIS_HOST = os.getenv("EXTERNAL_API_CACHE_REDIS_HOST", "10.0.16.12")
EXTERNAL_API_CACHE_REDIS_PASSWORD = os.getenv("EXTERNAL_API_CACHE_REDIS_PASSWORD")

MONGODB_URI = os.getenv("FUNCTION_RECORDINGS_MONGODB_URI")
FUNCTION_RECORDINGS_ENABLE = bool(os.getenv("FUNCTION_RECORDINGS_ENABLE")) or False
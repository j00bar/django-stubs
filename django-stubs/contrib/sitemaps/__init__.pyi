from datetime import datetime
from typing import Any, Dict, Generic, Iterable, List, Mapping, Optional, Sequence, TypeVar, Union

from django.contrib.sites.models import Site
from django.contrib.sites.requests import RequestSite
from django.core.paginator import Paginator
from django.db.models.base import Model
from django.db.models.query import QuerySet

PING_URL: str

class SitemapNotFound(Exception): ...

def ping_google(sitemap_url: Optional[str] = ..., ping_url: str = ..., sitemap_uses_https: bool = ...) -> None: ...

_ItemT = TypeVar("_ItemT")

class Sitemap(Generic[_ItemT]):
    limit: int = ...
    protocol: Optional[str] = ...
    i18n: bool = ...
    languages: Optional[Sequence[str]] = ...
    alternates: bool = ...
    x_default: bool = ...
    def items(self) -> Iterable[_ItemT]: ...
    def location(self, item: _ItemT) -> str: ...
    @property
    def paginator(self) -> Paginator: ...
    def get_urls(
        self, page: Union[int, str] = ..., site: Optional[Union[Site, RequestSite]] = ..., protocol: Optional[str] = ...
    ) -> List[Dict[str, Any]]: ...
    def get_latest_lastmod(self) -> Optional[datetime]: ...

_ModelT = TypeVar("_ModelT", bound=Model)

class GenericSitemap(Sitemap[_ModelT]):
    priority: Optional[float] = ...
    changefreq: Optional[str] = ...
    queryset: QuerySet[_ModelT] = ...
    date_field: Optional[str] = ...
    protocol: Optional[str] = ...
    def __init__(
        self,
        info_dict: Mapping[str, Union[datetime, QuerySet[_ModelT], str]],
        priority: Optional[float] = ...,
        changefreq: Optional[str] = ...,
        protocol: Optional[str] = ...,
    ) -> None: ...
    def items(self) -> QuerySet[_ModelT]: ...
    def lastmod(self, item: _ModelT) -> Optional[datetime]: ...
    def get_latest_lastmod(self) -> Optional[datetime]: ...

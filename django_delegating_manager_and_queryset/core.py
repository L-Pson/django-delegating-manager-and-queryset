from django.db import models
from typing import (
    Any,
    Dict, 
    Generic, 
    Iterable, 
    Iterator, 
    List,
    Optional, 
    Tuple, 
    TYPE_CHECKING,
    TypeVar, 
)

# Type variables
TQS = TypeVar("TQS", bound=models.QuerySet)
MT  = TypeVar("MT") 

class DelegatingQuerySet(models.QuerySet, Generic[MT]):
    if TYPE_CHECKING:
        def get(self, *args: Any, **kwargs: Any) -> MT: ...  # type: ignore
        def first(self) -> Optional[MT]: ...  # type: ignore
        def last(self) -> Optional[MT]: ...  # type: ignore
        def earliest(self, field_name: Optional[str] = None) -> MT: ...  # type: ignore
        def latest(self, field_name: Optional[str] = None) -> MT: ...  # type: ignore
        def create(self, **kwargs: Any) -> MT: ...  # type: ignore
        def bulk_create( # type: ignore
            self,
            objs: Iterable[MT],
            batch_size: Optional[int] = None,
            ignore_conflicts: bool = False
        ) -> List[MT]: ...  
        def get_or_create( # type: ignore
            self,
            defaults: Optional[Dict[str, Any]] = None,
            **kwargs: Any
        ) -> Tuple[MT, bool]: ...  
        def update_or_create( # type: ignore
            self,
            defaults: Optional[Dict[str, Any]] = None,
            **kwargs: Any
        ) -> Tuple[MT, bool]: ...  
        def in_bulk(
            self,
            id_list: Optional[Iterable[Any]] = None,
            *,
            field_name: str = "pk"
        ) -> Dict[Any, MT]: ...  # type: ignore
        def iterator(self, chunk_size: int = 2000) -> Iterator[MT]: ...  
        def __iter__(self) -> Iterator[MT]: ... # type: ignore

class DelegatingManager(models.Manager, Generic[TQS]):
    if TYPE_CHECKING:
        def get_queryset(self) -> TQS: ...
        def all(self) -> TQS: ... # type: ignore
        def filter(self, *args: Any, **kwargs: Any) -> TQS: ... # type: ignore
        def exclude(self, *args: Any, **kwargs: Any) -> TQS: ... # type: ignore
        def annotate(self, *args: Any, **kwargs: Any) -> TQS: ... # type: ignore
        def order_by(self, *fields: str) -> TQS: ... # type: ignore
        def reverse(self) -> TQS: ... # type: ignore
        def distinct(self, *fields: str) -> TQS: ... # type: ignore
        def values(self, *fields: str, **expressions: Any) -> TQS: ... # type: ignore
        def values_list(self, *fields: str, flat: bool = False) -> TQS: ... # type: ignore
        def none(self) -> TQS: ... # type: ignore
        def union(self, *other_qs: TQS, all: bool = False) -> TQS: ... # type: ignore
        def intersection(self, *other_qs: TQS) -> TQS: ... # type: ignore
        def difference(self, *other_qs: TQS) -> TQS: ... # type: ignore
        def select_related(self, *fields: str) -> TQS: ... # type: ignore
        def prefetch_related(self, *lookups: Any) -> TQS: ... # type: ignore
        def select_for_update( # type: ignore
            self,
            nowait: bool = False,
            skip_locked: bool = False,
            of: Iterable[Any] = (),
            no_key: bool = False
        ) -> TQS: ...
        def only(self, *fields: str) -> TQS: ... # type: ignore
        def defer(self, *fields: str) -> TQS: ... # type: ignore
        def using(self, alias: Optional[str]) -> TQS: ... # type: ignore
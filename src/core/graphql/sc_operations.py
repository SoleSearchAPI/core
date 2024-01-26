import sgqlc.types
import sgqlc.operation
import sc_schema

_schema = sc_schema
_schema_root = _schema.sc_schema

__all__ = ('Operations',)


def query_get_sneakers():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='GetSneakers', variables=dict(limit=sgqlc.types.Arg(_schema.Int), skip=sgqlc.types.Arg(_schema.Int)))
    _op_sneaker_models = _op.sneaker_models(limit=sgqlc.types.Variable('limit'), skip=sgqlc.types.Variable('skip'))
    _op_sneaker_models.name()
    _op_sneaker_models.date()
    _op_sneaker_models.images()
    _op_sneaker_models.order_priority()
    _op_sneaker_models.is_deleted()
    _op_sneaker_models._id()
    _op_sneaker_models.updated_at()
    _op_sneaker_models.created_at()
    _op_sneaker_models__release = _op_sneaker_models._release()
    _op_sneaker_models__release.title()
    _op_sneaker_models__release.description()
    _op_sneaker_models__release.date()
    _op_sneaker_models__release.colorway()
    _op_sneaker_models__release.price()
    _op_sneaker_models__release_brand = _op_sneaker_models__release.brand()
    _op_sneaker_models__release_brand.title()
    _op_sneaker_models__release_catalog = _op_sneaker_models__release.catalog()
    _op_sneaker_models__release_catalog.name()
    _op_sneaker_models__release.nickname()
    _op_sneaker_models__release.image_urls()
    _op_sneaker_models__release.resell_urls()
    _op_sneaker_models__release_resellsizes = _op_sneaker_models__release.resellsizes()
    _op_sneaker_models__release_resellsizes.uri()
    _op_sneaker_models__release_resellsizes.low_price()
    _op_sneaker_models__release_resellsizes.high_price()
    _op_sneaker_models__release_resellsizes.currency_unit()
    _op_sneaker_models__release_resellsizes.size_type()
    _op_sneaker_models__release_resellsizes_sizes = _op_sneaker_models__release_resellsizes.sizes()
    _op_sneaker_models__release_resellsizes_sizes.size()
    _op_sneaker_models__release_resellsizes_sizes.price()
    _op_sneaker_models__release_buy_links = _op_sneaker_models__release.buy_links()
    _op_sneaker_models__release_buy_links.title()
    _op_sneaker_models__release_buy_links.link()
    return _op


class Query:
    get_sneakers = query_get_sneakers()


class Operations:
    query = Query

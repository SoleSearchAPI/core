import sgqlc.operation
import sgqlc.types

import core.graphql.sc_schema as sc_schema

_schema = sc_schema
_schema_root = _schema.sc_schema

__all__ = ("Operations",)


def query_get_catalogs():
    _op = sgqlc.operation.Operation(
        _schema_root.query_type,
        name="GetCatalogs",
        variables=dict(
            limit=sgqlc.types.Arg(_schema.Int), skip=sgqlc.types.Arg(_schema.Int)
        ),
    )
    _op_sneakers = _op.sneakers(
        limit=sgqlc.types.Variable("limit"), skip=sgqlc.types.Variable("skip")
    )
    _op_sneakers._id()
    _op_sneakers.name()
    _op_sneakers.description()
    _op_sneakers_brand = _op_sneakers.brand()
    _op_sneakers_brand.title()
    _op_sneakers.date()
    _op_sneakers_colorways = _op_sneakers.colorways()
    _op_sneakers_colorways.image()
    _op_sneakers_colorways_links = _op_sneakers_colorways.links()
    _op_sneakers_colorways_links.url()
    _op_sneakers_colorways_links.title()
    _op_sneakers_colorways.nickname()
    _op_sneakers.image()
    _op_sneakers.updated_at()
    _op_sneakers.created_at()
    _op_sneakers__release = _op_sneakers._release()
    _op_sneakers__release.date()
    _op_sneakers__release.price()
    _op_sneakers__release.resell_urls()
    _op_sneakers__release.image_urls()
    _op_sneakers__release.nickname()
    _op_sneakers__release_buy_links = _op_sneakers__release.buy_links()
    _op_sneakers__release_buy_links.link()
    _op_sneakers__release_buy_links.title()
    return _op


class Query:
    get_catalogs = query_get_catalogs()


class Operations:
    query = Query

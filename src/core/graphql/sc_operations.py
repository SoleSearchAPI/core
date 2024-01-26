import sgqlc.operation
import sgqlc.types

import core.graphql.sc_schema as sc_schema

_schema = sc_schema
_schema_root = _schema.sc_schema

__all__ = ("Operations",)


def query_get_sneakers():
    _op = sgqlc.operation.Operation(
        _schema_root.query_type,
        name="GetSneakers",
        variables=dict(
            sortFilter=sgqlc.types.Arg(_schema.JSON),
            perPage=sgqlc.types.Arg(_schema.Int),
            page=sgqlc.types.Arg(_schema.Int),
        ),
    )
    _op_release_pagination = _op.release_pagination(
        sort=sgqlc.types.Variable("sortFilter"),
        per_page=sgqlc.types.Variable("perPage"),
        page=sgqlc.types.Variable("page"),
    )
    _op_release_pagination.count()
    _op_release_pagination_page_info = _op_release_pagination.page_info()
    _op_release_pagination_page_info.current_page()
    _op_release_pagination_page_info.page_count()
    _op_release_pagination_page_info.has_next_page()
    _op_release_pagination_items = _op_release_pagination.items()
    _op_release_pagination_items._id()
    _op_release_pagination_items.title()
    _op_release_pagination_items.description()
    _op_release_pagination_items.date()
    _op_release_pagination_items.colorway()
    _op_release_pagination_items.price()
    _op_release_pagination_items_brand = _op_release_pagination_items.brand()
    _op_release_pagination_items_brand.title()
    _op_release_pagination_items_catalog = _op_release_pagination_items.catalog()
    _op_release_pagination_items_catalog.name()
    _op_release_pagination_items_raffle_links = (
        _op_release_pagination_items.raffle_links()
    )
    _op_release_pagination_items_raffle_links.raffle_id()
    _op_release_pagination_items_raffle_links.link()
    _op_release_pagination_items_raffles = _op_release_pagination_items.raffles()
    _op_release_pagination_items_raffles.link()
    _op_release_pagination_items_raffles_raffle_website = (
        _op_release_pagination_items_raffles.raffle_website()
    )
    _op_release_pagination_items_raffles_raffle_website.name()
    _op_release_pagination_items_raffles_raffle_website.logo()
    _op_release_pagination_items.nickname()
    _op_release_pagination_items.image_urls()
    _op_release_pagination_items.resell_urls()
    _op_release_pagination_items_resellsizes = (
        _op_release_pagination_items.resellsizes()
    )
    _op_release_pagination_items_resellsizes.uri()
    _op_release_pagination_items_resellsizes.low_price()
    _op_release_pagination_items_resellsizes.high_price()
    _op_release_pagination_items_resellsizes.currency_unit()
    _op_release_pagination_items_resellsizes.size_type()
    _op_release_pagination_items_resellsizes_sizes = (
        _op_release_pagination_items_resellsizes.sizes()
    )
    _op_release_pagination_items_resellsizes_sizes.size()
    _op_release_pagination_items_resellsizes_sizes.price()
    _op_release_pagination_items_buy_links = _op_release_pagination_items.buy_links()
    _op_release_pagination_items_buy_links.title()
    _op_release_pagination_items_buy_links.link()
    return _op


class Query:
    get_sneakers = query_get_sneakers()


class Operations:
    query = Query

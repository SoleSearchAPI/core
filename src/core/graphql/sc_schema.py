import sgqlc.types
import sgqlc.types.datetime

sc_schema = sgqlc.types.Schema()


########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

Date = sgqlc.types.datetime.Date


class DropFeedType(sgqlc.types.Enum):
    __schema__ = sc_schema
    __choices__ = ("RAFFLE", "RESTOCK", "SHOCK_DROP", "SNKRS_PASS")


class EnumCommentSubject_type(sgqlc.types.Enum):
    __schema__ = sc_schema
    __choices__ = ("Article", "Post", "Release")


Float = sgqlc.types.Float

Int = sgqlc.types.Int


class JSON(sgqlc.types.Scalar):
    __schema__ = sc_schema


class MongoID(sgqlc.types.Scalar):
    __schema__ = sc_schema


String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################


########################################################################
# Output Objects and Interfaces
########################################################################
class Article(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "title",
        "content",
        "date",
        "image",
        "link",
        "source",
        "tag",
        "catalog",
        "sneaker_model",
        "featured",
        "featured_order_priority",
        "_id",
        "updated_at",
        "created_at",
        "comments",
        "related",
    )
    title = sgqlc.types.Field(String, graphql_name="title")
    content = sgqlc.types.Field(String, graphql_name="content")
    date = sgqlc.types.Field(JSON, graphql_name="date")
    image = sgqlc.types.Field(String, graphql_name="image")
    link = sgqlc.types.Field(String, graphql_name="link")
    source = sgqlc.types.Field(String, graphql_name="source")
    tag = sgqlc.types.Field(
        "ModelTag",
        graphql_name="tag",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    catalog = sgqlc.types.Field(
        "Sneaker",
        graphql_name="catalog",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    sneaker_model = sgqlc.types.Field(
        "SneakerModel",
        graphql_name="sneakerModel",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    featured = sgqlc.types.Field(Boolean, graphql_name="featured")
    featured_order_priority = sgqlc.types.Field(
        Float, graphql_name="featuredOrderPriority"
    )
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")
    comments = sgqlc.types.Field(
        "CommentPagination",
        graphql_name="comments",
        args=sgqlc.types.ArgDict(
            (
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    related = sgqlc.types.Field(
        sgqlc.types.list_of("Release"),
        graphql_name="related",
        args=sgqlc.types.ArgDict(
            (("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),)
        ),
    )


class ArticlePagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(Article), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null("PaginationInfo"), graphql_name="pageInfo"
    )


class Comment(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "comment",
        "author",
        "subject_id",
        "subject_type",
        "message",
        "timestamp",
        "_id",
        "_comment",
        "_commentlike",
        "likes",
        "is_liked",
    )
    comment = sgqlc.types.Field(
        "Comment",
        graphql_name="comment",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    author = sgqlc.types.Field(
        "User",
        graphql_name="author",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    subject_id = sgqlc.types.Field(String, graphql_name="subject_id")
    subject_type = sgqlc.types.Field(
        EnumCommentSubject_type, graphql_name="subject_type"
    )
    message = sgqlc.types.Field(String, graphql_name="message")
    timestamp = sgqlc.types.Field(Float, graphql_name="timestamp")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")
    _comment = sgqlc.types.Field(
        sgqlc.types.list_of("Comment"),
        graphql_name="_comment",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _commentlike = sgqlc.types.Field(
        sgqlc.types.list_of("CommentLike"),
        graphql_name="_commentlike",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    likes = sgqlc.types.Field(
        "CommentLikePagination",
        graphql_name="likes",
        args=sgqlc.types.ArgDict(
            (
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    is_liked = sgqlc.types.Field(Boolean, graphql_name="isLiked")


class CommentLike(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("user", "comment", "timestamp", "is_deleted", "_id")
    user = sgqlc.types.Field(
        "User",
        graphql_name="user",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    comment = sgqlc.types.Field(
        Comment,
        graphql_name="comment",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    timestamp = sgqlc.types.Field(Float, graphql_name="timestamp")
    is_deleted = sgqlc.types.Field(Boolean, graphql_name="isDeleted")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")


class CommentLikePagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(CommentLike), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null("PaginationInfo"), graphql_name="pageInfo"
    )


class CommentPagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(Comment), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null("PaginationInfo"), graphql_name="pageInfo"
    )


class DropFeed(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("type", "_id", "updated_at", "created_at")
    type = sgqlc.types.Field(String, graphql_name="type")
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")


class DropFeedRaffle(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "title",
        "url",
        "image_url",
        "closes",
        "raffle_type",
        "store",
        "type",
        "_id",
        "updated_at",
        "created_at",
    )
    title = sgqlc.types.Field(String, graphql_name="title")
    url = sgqlc.types.Field(String, graphql_name="url")
    image_url = sgqlc.types.Field(String, graphql_name="imageUrl")
    closes = sgqlc.types.Field(String, graphql_name="closes")
    raffle_type = sgqlc.types.Field(String, graphql_name="raffleType")
    store = sgqlc.types.Field("DropFeedRaffleStore", graphql_name="store")
    type = sgqlc.types.Field(String, graphql_name="type")
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")


class DropFeedRaffleStore(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("title", "image_url")
    title = sgqlc.types.Field(String, graphql_name="title")
    image_url = sgqlc.types.Field(String, graphql_name="imageUrl")


class DropFeedRestock(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "title",
        "url",
        "image_url",
        "site",
        "sizes",
        "type",
        "_id",
        "updated_at",
        "created_at",
    )
    title = sgqlc.types.Field(String, graphql_name="title")
    url = sgqlc.types.Field(String, graphql_name="url")
    image_url = sgqlc.types.Field(String, graphql_name="imageUrl")
    site = sgqlc.types.Field(String, graphql_name="site")
    sizes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="sizes")
    type = sgqlc.types.Field(String, graphql_name="type")
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")


class DropFeedShockDrop(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("content", "type", "_id", "updated_at", "created_at")
    content = sgqlc.types.Field(String, graphql_name="content")
    type = sgqlc.types.Field(String, graphql_name="type")
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")


class DropFeedSnkrsPass(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "title",
        "url",
        "image_url",
        "type",
        "_id",
        "updated_at",
        "created_at",
    )
    title = sgqlc.types.Field(String, graphql_name="title")
    url = sgqlc.types.Field(String, graphql_name="url")
    image_url = sgqlc.types.Field(String, graphql_name="imageUrl")
    type = sgqlc.types.Field(String, graphql_name="type")
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")


class Image(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("author", "url", "is_deleted", "_id")
    author = sgqlc.types.Field(
        "User",
        graphql_name="author",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    url = sgqlc.types.Field("ImageUrl", graphql_name="url")
    is_deleted = sgqlc.types.Field(Boolean, graphql_name="isDeleted")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")


class ImageUrl(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("original", "sm", "md", "lg", "xl")
    original = sgqlc.types.Field(String, graphql_name="original")
    sm = sgqlc.types.Field(String, graphql_name="sm")
    md = sgqlc.types.Field(String, graphql_name="md")
    lg = sgqlc.types.Field(String, graphql_name="lg")
    xl = sgqlc.types.Field(String, graphql_name="xl")


class Keyword(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("value", "last_cleaned_at", "_id")
    value = sgqlc.types.Field(String, graphql_name="value")
    last_cleaned_at = sgqlc.types.Field(Float, graphql_name="last_cleaned_at")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")


class KeywordPagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(Keyword), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null("PaginationInfo"), graphql_name="pageInfo"
    )


class ModelBrand(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("title", "_id", "_sneaker", "_release", "sneakers")
    title = sgqlc.types.Field(String, graphql_name="title")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")
    _sneaker = sgqlc.types.Field(
        sgqlc.types.list_of("Sneaker"),
        graphql_name="_sneaker",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
                (
                    "updated_since",
                    sgqlc.types.Arg(Date, graphql_name="updatedSince", default=None),
                ),
            )
        ),
    )
    _release = sgqlc.types.Field(
        sgqlc.types.list_of("Release"),
        graphql_name="_release",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
                (
                    "updated_since",
                    sgqlc.types.Arg(Date, graphql_name="updatedSince", default=None),
                ),
            )
        ),
    )
    sneakers = sgqlc.types.Field(
        "SneakerPagination",
        graphql_name="sneakers",
        args=sgqlc.types.ArgDict(
            (
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )


class ModelTag(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("title", "views", "_id", "_article", "_release", "_posttag")
    title = sgqlc.types.Field(String, graphql_name="title")
    views = sgqlc.types.Field(Float, graphql_name="views")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")
    _article = sgqlc.types.Field(
        sgqlc.types.list_of(Article),
        graphql_name="_article",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _release = sgqlc.types.Field(
        sgqlc.types.list_of("Release"),
        graphql_name="_release",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
                (
                    "updated_since",
                    sgqlc.types.Arg(Date, graphql_name="updatedSince", default=None),
                ),
            )
        ),
    )
    _posttag = sgqlc.types.Field(
        sgqlc.types.list_of("PostTag"),
        graphql_name="_posttag",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )


class Mutation(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "update_user",
        "delete_user",
        "restore_user",
        "create_image",
        "update_image",
        "delete_image",
        "restore_image",
        "create_raffle",
        "update_raffle",
        "delete_raffle",
        "restore_raffle",
        "create_sneaker",
        "update_sneaker",
        "delete_sneaker",
        "restore_sneaker",
        "create_article",
        "update_article",
        "delete_article",
        "restore_article",
        "create_release",
        "update_release",
        "delete_release",
        "restore_release",
        "create_comment",
        "update_comment",
        "delete_comment",
        "create_sneaker_model",
        "update_sneaker_model",
        "delete_sneaker_model",
        "restore_sneaker_model",
        "create_post_tag",
        "update_post_tag",
        "delete_post_tag",
        "restore_post_tag",
        "create_post",
        "update_post",
        "delete_post",
        "create_notification",
        "update_notification",
        "delete_notification",
        "restore_notification",
        "create_model_brand",
        "update_model_brand",
        "delete_model_brand",
        "restore_model_brand",
        "create_model_tag",
        "update_model_tag",
        "delete_model_tag",
        "restore_model_tag",
        "create_keyword",
        "update_keyword",
        "delete_keyword",
        "restore_keyword",
        "create_drop_feed",
        "update_drop_feed",
        "delete_drop_feed",
        "restore_drop_feed",
        "create_drop_feed_raffle",
        "update_drop_feed_raffle",
        "delete_drop_feed_raffle",
        "restore_drop_feed_raffle",
        "create_drop_feed_restock",
        "update_drop_feed_restock",
        "delete_drop_feed_restock",
        "restore_drop_feed_restock",
        "create_drop_feed_shock_drop",
        "update_drop_feed_shock_drop",
        "delete_drop_feed_shock_drop",
        "restore_drop_feed_shock_drop",
        "create_drop_feed_snkrs_pass",
        "update_drop_feed_snkrs_pass",
        "delete_drop_feed_snkrs_pass",
        "restore_drop_feed_snkrs_pass",
        "auth",
        "auth_with_role",
        "update_user_password",
        "restore_password_by_email",
        "restore_password_confirm",
        "register_user",
        "set_admin",
        "dismiss_admin",
        "set_editor",
        "dismiss_editor",
        "update_self",
        "delete_self",
        "set_device_token",
        "set_purchased",
        "action_confirm",
        "sneaker_add_view",
        "favorite",
        "unfavorite",
        "follow",
        "follows",
        "unfollow",
        "popular_add_view",
        "like",
        "dislike",
        "like_comment",
        "dislike_comment",
        "add_firebase_comment",
        "set_drop_feed_notification_settings",
    )
    update_user = sgqlc.types.Field(
        "User",
        graphql_name="updateUser",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_user = sgqlc.types.Field(
        JSON,
        graphql_name="deleteUser",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_user = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreUser",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_image = sgqlc.types.Field(
        Image,
        graphql_name="createImage",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_image = sgqlc.types.Field(
        Image,
        graphql_name="updateImage",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_image = sgqlc.types.Field(
        JSON,
        graphql_name="deleteImage",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_image = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreImage",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_raffle = sgqlc.types.Field(
        "Raffle",
        graphql_name="createRaffle",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_raffle = sgqlc.types.Field(
        "Raffle",
        graphql_name="updateRaffle",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_raffle = sgqlc.types.Field(
        JSON,
        graphql_name="deleteRaffle",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_raffle = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreRaffle",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_sneaker = sgqlc.types.Field(
        "Sneaker",
        graphql_name="createSneaker",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_sneaker = sgqlc.types.Field(
        "Sneaker",
        graphql_name="updateSneaker",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_sneaker = sgqlc.types.Field(
        JSON,
        graphql_name="deleteSneaker",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_sneaker = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreSneaker",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_article = sgqlc.types.Field(
        Article,
        graphql_name="createArticle",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_article = sgqlc.types.Field(
        Article,
        graphql_name="updateArticle",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_article = sgqlc.types.Field(
        JSON,
        graphql_name="deleteArticle",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_article = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreArticle",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_release = sgqlc.types.Field(
        "Release",
        graphql_name="createRelease",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_release = sgqlc.types.Field(
        "Release",
        graphql_name="updateRelease",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_release = sgqlc.types.Field(
        JSON,
        graphql_name="deleteRelease",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_release = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreRelease",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_comment = sgqlc.types.Field(
        Comment,
        graphql_name="createComment",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_comment = sgqlc.types.Field(
        Comment,
        graphql_name="updateComment",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_comment = sgqlc.types.Field(
        JSON,
        graphql_name="deleteComment",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_sneaker_model = sgqlc.types.Field(
        "SneakerModel",
        graphql_name="createSneakerModel",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_sneaker_model = sgqlc.types.Field(
        "SneakerModel",
        graphql_name="updateSneakerModel",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_sneaker_model = sgqlc.types.Field(
        JSON,
        graphql_name="deleteSneakerModel",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_sneaker_model = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreSneakerModel",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_post_tag = sgqlc.types.Field(
        "PostTag",
        graphql_name="createPostTag",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_post_tag = sgqlc.types.Field(
        "PostTag",
        graphql_name="updatePostTag",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_post_tag = sgqlc.types.Field(
        JSON,
        graphql_name="deletePostTag",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_post_tag = sgqlc.types.Field(
        Boolean,
        graphql_name="restorePostTag",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_post = sgqlc.types.Field(
        "Post",
        graphql_name="createPost",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_post = sgqlc.types.Field(
        "Post",
        graphql_name="updatePost",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_post = sgqlc.types.Field(
        JSON,
        graphql_name="deletePost",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_notification = sgqlc.types.Field(
        "Notification",
        graphql_name="createNotification",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_notification = sgqlc.types.Field(
        "Notification",
        graphql_name="updateNotification",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_notification = sgqlc.types.Field(
        JSON,
        graphql_name="deleteNotification",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_notification = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreNotification",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_model_brand = sgqlc.types.Field(
        ModelBrand,
        graphql_name="createModelBrand",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_model_brand = sgqlc.types.Field(
        ModelBrand,
        graphql_name="updateModelBrand",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_model_brand = sgqlc.types.Field(
        JSON,
        graphql_name="deleteModelBrand",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_model_brand = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreModelBrand",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_model_tag = sgqlc.types.Field(
        ModelTag,
        graphql_name="createModelTag",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_model_tag = sgqlc.types.Field(
        ModelTag,
        graphql_name="updateModelTag",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_model_tag = sgqlc.types.Field(
        JSON,
        graphql_name="deleteModelTag",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_model_tag = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreModelTag",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_keyword = sgqlc.types.Field(
        Keyword,
        graphql_name="createKeyword",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_keyword = sgqlc.types.Field(
        Keyword,
        graphql_name="updateKeyword",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_keyword = sgqlc.types.Field(
        JSON,
        graphql_name="deleteKeyword",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_keyword = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreKeyword",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_drop_feed = sgqlc.types.Field(
        DropFeed,
        graphql_name="createDropFeed",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_drop_feed = sgqlc.types.Field(
        DropFeed,
        graphql_name="updateDropFeed",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_drop_feed = sgqlc.types.Field(
        JSON,
        graphql_name="deleteDropFeed",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_drop_feed = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreDropFeed",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_drop_feed_raffle = sgqlc.types.Field(
        DropFeedRaffle,
        graphql_name="createDropFeedRaffle",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_drop_feed_raffle = sgqlc.types.Field(
        DropFeedRaffle,
        graphql_name="updateDropFeedRaffle",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_drop_feed_raffle = sgqlc.types.Field(
        JSON,
        graphql_name="deleteDropFeedRaffle",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_drop_feed_raffle = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreDropFeedRaffle",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_drop_feed_restock = sgqlc.types.Field(
        DropFeedRestock,
        graphql_name="createDropFeedRestock",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_drop_feed_restock = sgqlc.types.Field(
        DropFeedRestock,
        graphql_name="updateDropFeedRestock",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_drop_feed_restock = sgqlc.types.Field(
        JSON,
        graphql_name="deleteDropFeedRestock",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_drop_feed_restock = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreDropFeedRestock",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_drop_feed_shock_drop = sgqlc.types.Field(
        DropFeedShockDrop,
        graphql_name="createDropFeedShockDrop",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_drop_feed_shock_drop = sgqlc.types.Field(
        DropFeedShockDrop,
        graphql_name="updateDropFeedShockDrop",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_drop_feed_shock_drop = sgqlc.types.Field(
        JSON,
        graphql_name="deleteDropFeedShockDrop",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_drop_feed_shock_drop = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreDropFeedShockDrop",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    create_drop_feed_snkrs_pass = sgqlc.types.Field(
        DropFeedSnkrsPass,
        graphql_name="createDropFeedSnkrsPass",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    update_drop_feed_snkrs_pass = sgqlc.types.Field(
        DropFeedSnkrsPass,
        graphql_name="updateDropFeedSnkrsPass",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),
            )
        ),
    )
    delete_drop_feed_snkrs_pass = sgqlc.types.Field(
        JSON,
        graphql_name="deleteDropFeedSnkrsPass",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    restore_drop_feed_snkrs_pass = sgqlc.types.Field(
        Boolean,
        graphql_name="restoreDropFeedSnkrsPass",
        args=sgqlc.types.ArgDict(
            (("query", sgqlc.types.Arg(JSON, graphql_name="query", default=None)),)
        ),
    )
    auth = sgqlc.types.Field(
        JSON,
        graphql_name="auth",
        args=sgqlc.types.ArgDict(
            (
                ("email", sgqlc.types.Arg(String, graphql_name="email", default=None)),
                (
                    "password",
                    sgqlc.types.Arg(String, graphql_name="password", default=None),
                ),
            )
        ),
    )
    auth_with_role = sgqlc.types.Field(
        JSON,
        graphql_name="authWithRole",
        args=sgqlc.types.ArgDict(
            (
                ("email", sgqlc.types.Arg(String, graphql_name="email", default=None)),
                (
                    "password",
                    sgqlc.types.Arg(String, graphql_name="password", default=None),
                ),
            )
        ),
    )
    update_user_password = sgqlc.types.Field(
        Boolean,
        graphql_name="updateUserPassword",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                (
                    "oldpassword",
                    sgqlc.types.Arg(String, graphql_name="oldpassword", default=None),
                ),
                (
                    "newpassword",
                    sgqlc.types.Arg(String, graphql_name="newpassword", default=None),
                ),
            )
        ),
    )
    restore_password_by_email = sgqlc.types.Field(
        Boolean,
        graphql_name="restorePasswordByEmail",
        args=sgqlc.types.ArgDict(
            (("email", sgqlc.types.Arg(String, graphql_name="email", default=None)),)
        ),
    )
    restore_password_confirm = sgqlc.types.Field(
        Boolean,
        graphql_name="restorePasswordConfirm",
        args=sgqlc.types.ArgDict(
            (
                ("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),
                ("data", sgqlc.types.Arg(JSON, graphql_name="data", default=None)),
            )
        ),
    )
    register_user = sgqlc.types.Field(
        JSON,
        graphql_name="registerUser",
        args=sgqlc.types.ArgDict(
            (("record", sgqlc.types.Arg(JSON, graphql_name="record", default=None)),)
        ),
    )
    set_admin = sgqlc.types.Field(
        Boolean,
        graphql_name="setAdmin",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    dismiss_admin = sgqlc.types.Field(
        Boolean,
        graphql_name="dismissAdmin",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    set_editor = sgqlc.types.Field(
        Boolean,
        graphql_name="setEditor",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    dismiss_editor = sgqlc.types.Field(
        Boolean,
        graphql_name="dismissEditor",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    update_self = sgqlc.types.Field(
        "User",
        graphql_name="updateSelf",
        args=sgqlc.types.ArgDict(
            (("update", sgqlc.types.Arg(JSON, graphql_name="update", default=None)),)
        ),
    )
    delete_self = sgqlc.types.Field(Boolean, graphql_name="deleteSelf")
    set_device_token = sgqlc.types.Field(
        Boolean,
        graphql_name="setDeviceToken",
        args=sgqlc.types.ArgDict(
            (("token", sgqlc.types.Arg(String, graphql_name="token", default=None)),)
        ),
    )
    set_purchased = sgqlc.types.Field(
        Boolean,
        graphql_name="setPurchased",
        args=sgqlc.types.ArgDict(
            (
                (
                    "purchased",
                    sgqlc.types.Arg(Boolean, graphql_name="purchased", default=None),
                ),
            )
        ),
    )
    action_confirm = sgqlc.types.Field(
        Boolean,
        graphql_name="actionConfirm",
        args=sgqlc.types.ArgDict(
            (
                ("token", sgqlc.types.Arg(String, graphql_name="token", default=None)),
                ("data", sgqlc.types.Arg(JSON, graphql_name="data", default=None)),
            )
        ),
    )
    sneaker_add_view = sgqlc.types.Field(
        Boolean,
        graphql_name="sneakerAddView",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    favorite = sgqlc.types.Field(
        Boolean,
        graphql_name="favorite",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    unfavorite = sgqlc.types.Field(
        Boolean,
        graphql_name="unfavorite",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    follow = sgqlc.types.Field(
        Boolean,
        graphql_name="follow",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    follows = sgqlc.types.Field(
        Boolean,
        graphql_name="follows",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String), graphql_name="ids", default=None
                    ),
                ),
            )
        ),
    )
    unfollow = sgqlc.types.Field(
        Boolean,
        graphql_name="unfollow",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    popular_add_view = sgqlc.types.Field(
        Boolean,
        graphql_name="popularAddView",
        args=sgqlc.types.ArgDict(
            (
                ("type", sgqlc.types.Arg(String, graphql_name="type", default=None)),
                ("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),
            )
        ),
    )
    like = sgqlc.types.Field(
        Boolean,
        graphql_name="like",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    dislike = sgqlc.types.Field(
        Boolean,
        graphql_name="dislike",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    like_comment = sgqlc.types.Field(
        Boolean,
        graphql_name="likeComment",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    dislike_comment = sgqlc.types.Field(
        Boolean,
        graphql_name="dislikeComment",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )
    add_firebase_comment = sgqlc.types.Field(
        Comment,
        graphql_name="addFirebaseComment",
        args=sgqlc.types.ArgDict(
            (
                ("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),
                ("type", sgqlc.types.Arg(String, graphql_name="type", default=None)),
                (
                    "author_id",
                    sgqlc.types.Arg(String, graphql_name="author_id", default=None),
                ),
                (
                    "message",
                    sgqlc.types.Arg(String, graphql_name="message", default=None),
                ),
            )
        ),
    )
    set_drop_feed_notification_settings = sgqlc.types.Field(
        sgqlc.types.list_of(DropFeedType),
        graphql_name="setDropFeedNotificationSettings",
        args=sgqlc.types.ArgDict(
            (
                (
                    "drop_feed_types",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(DropFeedType),
                        graphql_name="dropFeedTypes",
                        default=None,
                    ),
                ),
            )
        ),
    )


class Notification(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "user",
        "header",
        "message",
        "sender_name",
        "data",
        "timestamp",
        "_id",
    )
    user = sgqlc.types.Field(
        "User",
        graphql_name="user",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    header = sgqlc.types.Field(String, graphql_name="header")
    message = sgqlc.types.Field(String, graphql_name="message")
    sender_name = sgqlc.types.Field(String, graphql_name="senderName")
    data = sgqlc.types.Field(JSON, graphql_name="data")
    timestamp = sgqlc.types.Field(Float, graphql_name="timestamp")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")


class NotificationPagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(Notification), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null("PaginationInfo"), graphql_name="pageInfo"
    )


class PaginationInfo(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "current_page",
        "per_page",
        "page_count",
        "item_count",
        "has_next_page",
        "has_previous_page",
    )
    current_page = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="currentPage"
    )
    per_page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="perPage")
    page_count = sgqlc.types.Field(Int, graphql_name="pageCount")
    item_count = sgqlc.types.Field(Int, graphql_name="itemCount")
    has_next_page = sgqlc.types.Field(Boolean, graphql_name="hasNextPage")
    has_previous_page = sgqlc.types.Field(Boolean, graphql_name="hasPreviousPage")


class Post(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "content",
        "timestamp",
        "image",
        "author",
        "is_deleted",
        "_id",
        "updated_at",
        "created_at",
        "_posttag",
        "_postlike",
        "comments",
        "tags",
        "likes",
        "is_liked",
    )
    content = sgqlc.types.Field(String, graphql_name="content")
    timestamp = sgqlc.types.Field(Float, graphql_name="timestamp")
    image = sgqlc.types.Field(String, graphql_name="image")
    author = sgqlc.types.Field(
        "User",
        graphql_name="author",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    is_deleted = sgqlc.types.Field(Boolean, graphql_name="isDeleted")
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")
    _posttag = sgqlc.types.Field(
        sgqlc.types.list_of("PostTag"),
        graphql_name="_posttag",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _postlike = sgqlc.types.Field(
        sgqlc.types.list_of("PostLike"),
        graphql_name="_postlike",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    comments = sgqlc.types.Field(
        CommentPagination,
        graphql_name="comments",
        args=sgqlc.types.ArgDict(
            (
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    tags = sgqlc.types.Field(
        "PostTagPagination",
        graphql_name="tags",
        args=sgqlc.types.ArgDict(
            (
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    likes = sgqlc.types.Field(
        "PostLikePagination",
        graphql_name="likes",
        args=sgqlc.types.ArgDict(
            (
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    is_liked = sgqlc.types.Field(Boolean, graphql_name="isLiked")


class PostLike(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("user", "post", "timestamp", "is_deleted", "_id")
    user = sgqlc.types.Field(
        "User",
        graphql_name="user",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    post = sgqlc.types.Field(
        Post,
        graphql_name="post",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    timestamp = sgqlc.types.Field(Float, graphql_name="timestamp")
    is_deleted = sgqlc.types.Field(Boolean, graphql_name="isDeleted")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")


class PostLikePagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(PostLike), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PaginationInfo), graphql_name="pageInfo"
    )


class PostPagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(Post), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PaginationInfo), graphql_name="pageInfo"
    )


class PostTag(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("post", "tag", "_id")
    post = sgqlc.types.Field(
        Post,
        graphql_name="post",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    tag = sgqlc.types.Field(
        ModelTag,
        graphql_name="tag",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")


class PostTagPagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(PostTag), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PaginationInfo), graphql_name="pageInfo"
    )


class Query(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "user",
        "users",
        "image",
        "images",
        "raffle",
        "raffles",
        "sneaker",
        "sneakers",
        "sneaker_pagination",
        "article",
        "articles",
        "article_pagination",
        "release",
        "releases",
        "comment",
        "comments",
        "comment_pagination",
        "sneaker_model",
        "sneaker_models",
        "sneaker_model_pagination",
        "post_tag",
        "post_tags",
        "post_tag_pagination",
        "post",
        "posts",
        "post_pagination",
        "notification",
        "notifications",
        "notification_pagination",
        "model_brand",
        "model_brands",
        "model_tag",
        "model_tags",
        "keyword",
        "keywords",
        "keyword_pagination",
        "drop_feed",
        "drop_feeds",
        "drop_feed_raffle",
        "drop_feed_raffles",
        "drop_feed_restock",
        "drop_feed_restocks",
        "drop_feed_shock_drop",
        "drop_feed_shock_drops",
        "drop_feed_snkrs_pass",
        "drop_feed_snkrs_passs",
        "get_self_info",
        "self",
        "release_pagination",
        "search_release",
        "get_my_favorites",
        "get_my_follows",
        "get_popular",
        "get_popular_current",
        "get_popular_both",
        "post_by_tag_pagination",
        "notification_by_self_pagination",
        "get_drop_feeds",
        "get_drop_feed_notification_settings",
    )
    user = sgqlc.types.Field(
        "User",
        graphql_name="User",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    users = sgqlc.types.Field(
        sgqlc.types.list_of("User"),
        graphql_name="Users",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    image = sgqlc.types.Field(
        "Image",
        graphql_name="Image",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    images = sgqlc.types.Field(
        sgqlc.types.list_of("Image"),
        graphql_name="Images",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    raffle = sgqlc.types.Field(
        "Raffle",
        graphql_name="Raffle",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    raffles = sgqlc.types.Field(
        sgqlc.types.list_of("Raffle"),
        graphql_name="Raffles",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    sneaker = sgqlc.types.Field(
        "Sneaker",
        graphql_name="Sneaker",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    sneakers = sgqlc.types.Field(
        sgqlc.types.list_of("Sneaker"),
        graphql_name="Sneakers",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
                (
                    "updated_since",
                    sgqlc.types.Arg(Date, graphql_name="updatedSince", default=None),
                ),
            )
        ),
    )
    sneaker_pagination = sgqlc.types.Field(
        "SneakerPagination",
        graphql_name="SneakerPagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    article = sgqlc.types.Field(
        "Article",
        graphql_name="Article",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    articles = sgqlc.types.Field(
        sgqlc.types.list_of("Article"),
        graphql_name="Articles",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    article_pagination = sgqlc.types.Field(
        "ArticlePagination",
        graphql_name="ArticlePagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    release = sgqlc.types.Field(
        "Release",
        graphql_name="Release",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    releases = sgqlc.types.Field(
        sgqlc.types.list_of("Release"),
        graphql_name="Releases",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
                (
                    "updated_since",
                    sgqlc.types.Arg(Date, graphql_name="updatedSince", default=None),
                ),
            )
        ),
    )
    comment = sgqlc.types.Field(
        "Comment",
        graphql_name="Comment",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    comments = sgqlc.types.Field(
        sgqlc.types.list_of("Comment"),
        graphql_name="Comments",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    comment_pagination = sgqlc.types.Field(
        "CommentPagination",
        graphql_name="CommentPagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    sneaker_model = sgqlc.types.Field(
        "SneakerModel",
        graphql_name="SneakerModel",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    sneaker_models = sgqlc.types.Field(
        sgqlc.types.list_of("SneakerModel"),
        graphql_name="SneakerModels",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
                (
                    "updated_since",
                    sgqlc.types.Arg(Date, graphql_name="updatedSince", default=None),
                ),
            )
        ),
    )
    sneaker_model_pagination = sgqlc.types.Field(
        "SneakerModelPagination",
        graphql_name="SneakerModelPagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    post_tag = sgqlc.types.Field(
        "PostTag",
        graphql_name="PostTag",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    post_tags = sgqlc.types.Field(
        sgqlc.types.list_of("PostTag"),
        graphql_name="PostTags",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    post_tag_pagination = sgqlc.types.Field(
        "PostTagPagination",
        graphql_name="PostTagPagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    post = sgqlc.types.Field(
        "Post",
        graphql_name="Post",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    posts = sgqlc.types.Field(
        sgqlc.types.list_of("Post"),
        graphql_name="Posts",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    post_pagination = sgqlc.types.Field(
        "PostPagination",
        graphql_name="PostPagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    notification = sgqlc.types.Field(
        "Notification",
        graphql_name="Notification",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    notifications = sgqlc.types.Field(
        sgqlc.types.list_of("Notification"),
        graphql_name="Notifications",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    notification_pagination = sgqlc.types.Field(
        "NotificationPagination",
        graphql_name="NotificationPagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    model_brand = sgqlc.types.Field(
        "ModelBrand",
        graphql_name="ModelBrand",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    model_brands = sgqlc.types.Field(
        sgqlc.types.list_of("ModelBrand"),
        graphql_name="ModelBrands",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    model_tag = sgqlc.types.Field(
        "ModelTag",
        graphql_name="ModelTag",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    model_tags = sgqlc.types.Field(
        sgqlc.types.list_of("ModelTag"),
        graphql_name="ModelTags",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    keyword = sgqlc.types.Field(
        "Keyword",
        graphql_name="Keyword",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    keywords = sgqlc.types.Field(
        sgqlc.types.list_of("Keyword"),
        graphql_name="Keywords",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    keyword_pagination = sgqlc.types.Field(
        "KeywordPagination",
        graphql_name="KeywordPagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    drop_feed = sgqlc.types.Field(
        "DropFeed",
        graphql_name="DropFeed",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    drop_feeds = sgqlc.types.Field(
        sgqlc.types.list_of("DropFeed"),
        graphql_name="DropFeeds",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    drop_feed_raffle = sgqlc.types.Field(
        "DropFeedRaffle",
        graphql_name="DropFeedRaffle",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    drop_feed_raffles = sgqlc.types.Field(
        sgqlc.types.list_of("DropFeedRaffle"),
        graphql_name="DropFeedRaffles",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    drop_feed_restock = sgqlc.types.Field(
        "DropFeedRestock",
        graphql_name="DropFeedRestock",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    drop_feed_restocks = sgqlc.types.Field(
        sgqlc.types.list_of("DropFeedRestock"),
        graphql_name="DropFeedRestocks",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    drop_feed_shock_drop = sgqlc.types.Field(
        "DropFeedShockDrop",
        graphql_name="DropFeedShockDrop",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    drop_feed_shock_drops = sgqlc.types.Field(
        sgqlc.types.list_of("DropFeedShockDrop"),
        graphql_name="DropFeedShockDrops",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    drop_feed_snkrs_pass = sgqlc.types.Field(
        "DropFeedSnkrsPass",
        graphql_name="DropFeedSnkrsPass",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    drop_feed_snkrs_passs = sgqlc.types.Field(
        sgqlc.types.list_of("DropFeedSnkrsPass"),
        graphql_name="DropFeedSnkrsPasss",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    get_self_info = sgqlc.types.Field(JSON, graphql_name="getSelfInfo")
    self = sgqlc.types.Field("User", graphql_name="self")
    release_pagination = sgqlc.types.Field(
        "ReleasePagination",
        graphql_name="ReleasePagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    search_release = sgqlc.types.Field(
        sgqlc.types.list_of("Release"),
        graphql_name="searchRelease",
        args=sgqlc.types.ArgDict(
            (("text", sgqlc.types.Arg(String, graphql_name="text", default=None)),)
        ),
    )
    get_my_favorites = sgqlc.types.Field(
        sgqlc.types.list_of("Release"), graphql_name="getMyFavorites"
    )
    get_my_follows = sgqlc.types.Field(
        sgqlc.types.list_of("SneakerModel"), graphql_name="getMyFollows"
    )
    get_popular = sgqlc.types.Field(
        sgqlc.types.list_of("PopularUnion"),
        graphql_name="getPopular",
        args=sgqlc.types.ArgDict(
            (
                ("type", sgqlc.types.Arg(String, graphql_name="type", default=None)),
                ("year", sgqlc.types.Arg(Int, graphql_name="year", default=None)),
                ("month", sgqlc.types.Arg(Int, graphql_name="month", default=None)),
                ("week", sgqlc.types.Arg(Int, graphql_name="week", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
            )
        ),
    )
    get_popular_current = sgqlc.types.Field(
        sgqlc.types.list_of("PopularUnion"),
        graphql_name="getPopularCurrent",
        args=sgqlc.types.ArgDict(
            (
                ("type", sgqlc.types.Arg(String, graphql_name="type", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
            )
        ),
    )
    get_popular_both = sgqlc.types.Field(
        sgqlc.types.list_of("PopularUnion"),
        graphql_name="getPopularBoth",
        args=sgqlc.types.ArgDict(
            (
                ("year", sgqlc.types.Arg(Int, graphql_name="year", default=None)),
                ("month", sgqlc.types.Arg(Int, graphql_name="month", default=None)),
                ("week", sgqlc.types.Arg(Int, graphql_name="week", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
            )
        ),
    )
    post_by_tag_pagination = sgqlc.types.Field(
        "PostPagination",
        graphql_name="PostByTagPagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    notification_by_self_pagination = sgqlc.types.Field(
        "NotificationPagination",
        graphql_name="NotificationBySelfPagination",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    get_drop_feeds = sgqlc.types.Field(
        sgqlc.types.list_of("DropFeedUnion"),
        graphql_name="getDropFeeds",
        args=sgqlc.types.ArgDict(
            (
                (
                    "type",
                    sgqlc.types.Arg(DropFeedType, graphql_name="type", default=None),
                ),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
            )
        ),
    )
    get_drop_feed_notification_settings = sgqlc.types.Field(
        sgqlc.types.list_of(DropFeedType),
        graphql_name="getDropFeedNotificationSettings",
    )


class Raffle(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("name", "logo", "_id")
    name = sgqlc.types.Field(String, graphql_name="name")
    logo = sgqlc.types.Field(String, graphql_name="logo")
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")


class RaffleLink(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("link", "raffle_website")
    link = sgqlc.types.Field(String, graphql_name="link")
    raffle_website = sgqlc.types.Field(Raffle, graphql_name="raffleWebsite")


class Release(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "title",
        "description",
        "date",
        "colorway",
        "price",
        "brand",
        "tag",
        "catalog",
        "sneaker_model",
        "raffle_links",
        "nickname",
        "image_urls",
        "resell_urls",
        "resellsizes",
        "buy_links",
        "has_unknown_day",
        "order_priority",
        "search_string",
        "featured",
        "featured_order_priority",
        "is_deleted",
        "_id",
        "updated_at",
        "created_at",
        "_userfavorite",
        "comments",
        "raffles",
        "related",
        "is_favorite",
    )
    title = sgqlc.types.Field(String, graphql_name="title")
    description = sgqlc.types.Field(String, graphql_name="description")
    date = sgqlc.types.Field(String, graphql_name="date")
    colorway = sgqlc.types.Field(String, graphql_name="colorway")
    price = sgqlc.types.Field(JSON, graphql_name="price")
    brand = sgqlc.types.Field(
        ModelBrand,
        graphql_name="brand",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    tag = sgqlc.types.Field(
        ModelTag,
        graphql_name="tag",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    catalog = sgqlc.types.Field(
        "Sneaker",
        graphql_name="catalog",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    sneaker_model = sgqlc.types.Field(
        "SneakerModel",
        graphql_name="sneakerModel",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    raffle_links = sgqlc.types.Field(
        sgqlc.types.list_of("ReleaseRaffleLinks"), graphql_name="raffleLinks"
    )
    nickname = sgqlc.types.Field(String, graphql_name="nickname")
    image_urls = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="imageUrls"
    )
    resell_urls = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resellUrls"
    )
    resellsizes = sgqlc.types.Field(
        sgqlc.types.list_of("ReleaseResellsizes"), graphql_name="resellsizes"
    )
    buy_links = sgqlc.types.Field(
        sgqlc.types.list_of("ReleaseBuyLinks"), graphql_name="buyLinks"
    )
    has_unknown_day = sgqlc.types.Field(Boolean, graphql_name="hasUnknownDay")
    order_priority = sgqlc.types.Field(Float, graphql_name="orderPriority")
    search_string = sgqlc.types.Field(String, graphql_name="searchString")
    featured = sgqlc.types.Field(Boolean, graphql_name="featured")
    featured_order_priority = sgqlc.types.Field(
        Float, graphql_name="featuredOrderPriority"
    )
    is_deleted = sgqlc.types.Field(Boolean, graphql_name="isDeleted")
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")
    _userfavorite = sgqlc.types.Field(
        sgqlc.types.list_of("UserFavorite"),
        graphql_name="_userfavorite",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    comments = sgqlc.types.Field(
        CommentPagination,
        graphql_name="comments",
        args=sgqlc.types.ArgDict(
            (
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                (
                    "per_page",
                    sgqlc.types.Arg(Int, graphql_name="perPage", default=None),
                ),
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
            )
        ),
    )
    raffles = sgqlc.types.Field(sgqlc.types.list_of(RaffleLink), graphql_name="raffles")
    related = sgqlc.types.Field(
        sgqlc.types.list_of("Release"),
        graphql_name="related",
        args=sgqlc.types.ArgDict(
            (("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),)
        ),
    )
    is_favorite = sgqlc.types.Field(Boolean, graphql_name="isFavorite")


class ReleaseBuyLinks(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("link", "title", "_id")
    link = sgqlc.types.Field(String, graphql_name="link")
    title = sgqlc.types.Field(String, graphql_name="title")
    _id = sgqlc.types.Field(MongoID, graphql_name="_id")


class ReleasePagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(Release), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PaginationInfo), graphql_name="pageInfo"
    )


class ReleaseRaffleLinks(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("raffle_id", "link", "_id")
    raffle_id = sgqlc.types.Field(String, graphql_name="raffleId")
    link = sgqlc.types.Field(String, graphql_name="link")
    _id = sgqlc.types.Field(MongoID, graphql_name="_id")


class ReleaseResellsizes(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "uri",
        "low_price",
        "high_price",
        "currency_unit",
        "size_type",
        "sizes",
        "_id",
    )
    uri = sgqlc.types.Field(String, graphql_name="uri")
    low_price = sgqlc.types.Field(Float, graphql_name="lowPrice")
    high_price = sgqlc.types.Field(Float, graphql_name="highPrice")
    currency_unit = sgqlc.types.Field(String, graphql_name="currencyUnit")
    size_type = sgqlc.types.Field(String, graphql_name="sizeType")
    sizes = sgqlc.types.Field(
        sgqlc.types.list_of("ReleaseResellsizesSizes"), graphql_name="sizes"
    )
    _id = sgqlc.types.Field(MongoID, graphql_name="_id")


class ReleaseResellsizesSizes(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("size", "price", "_id")
    size = sgqlc.types.Field(Float, graphql_name="size")
    price = sgqlc.types.Field(Float, graphql_name="price")
    _id = sgqlc.types.Field(MongoID, graphql_name="_id")


class Sneaker(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "name",
        "description",
        "brand",
        "date",
        "colorways",
        "views",
        "is_deleted",
        "_id",
        "updated_at",
        "created_at",
        "_article",
        "_release",
        "image",
    )
    name = sgqlc.types.Field(String, graphql_name="name")
    description = sgqlc.types.Field(String, graphql_name="description")
    brand = sgqlc.types.Field(
        ModelBrand,
        graphql_name="brand",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    date = sgqlc.types.Field(JSON, graphql_name="date")
    colorways = sgqlc.types.Field(
        sgqlc.types.list_of("SneakerColorways"), graphql_name="colorways"
    )
    views = sgqlc.types.Field(Float, graphql_name="views")
    is_deleted = sgqlc.types.Field(Boolean, graphql_name="isDeleted")
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")
    _article = sgqlc.types.Field(
        sgqlc.types.list_of(Article),
        graphql_name="_article",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _release = sgqlc.types.Field(
        sgqlc.types.list_of(Release),
        graphql_name="_release",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
                (
                    "updated_since",
                    sgqlc.types.Arg(Date, graphql_name="updatedSince", default=None),
                ),
            )
        ),
    )
    image = sgqlc.types.Field(String, graphql_name="image")


class SneakerColorways(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("image", "links", "nickname", "_id")
    image = sgqlc.types.Field(String, graphql_name="image")
    links = sgqlc.types.Field(
        sgqlc.types.list_of("SneakerColorwaysLinks"), graphql_name="links"
    )
    nickname = sgqlc.types.Field(String, graphql_name="nickname")
    _id = sgqlc.types.Field(MongoID, graphql_name="_id")


class SneakerColorwaysLinks(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("url", "title", "_id")
    url = sgqlc.types.Field(String, graphql_name="url")
    title = sgqlc.types.Field(String, graphql_name="title")
    _id = sgqlc.types.Field(MongoID, graphql_name="_id")


class SneakerModel(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "name",
        "date",
        "images",
        "order_priority",
        "is_deleted",
        "_id",
        "updated_at",
        "created_at",
        "_article",
        "_release",
        "_userfollow",
    )
    name = sgqlc.types.Field(String, graphql_name="name")
    date = sgqlc.types.Field(JSON, graphql_name="date")
    images = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="images")
    order_priority = sgqlc.types.Field(Float, graphql_name="orderPriority")
    is_deleted = sgqlc.types.Field(Boolean, graphql_name="isDeleted")
    _id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")
    _article = sgqlc.types.Field(
        sgqlc.types.list_of(Article),
        graphql_name="_article",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _release = sgqlc.types.Field(
        sgqlc.types.list_of(Release),
        graphql_name="_release",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
                (
                    "updated_since",
                    sgqlc.types.Arg(Date, graphql_name="updatedSince", default=None),
                ),
            )
        ),
    )
    _userfollow = sgqlc.types.Field(
        sgqlc.types.list_of("UserFollow"),
        graphql_name="_userfollow",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )


class SneakerModelPagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(SneakerModel), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PaginationInfo), graphql_name="pageInfo"
    )


class SneakerPagination(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("count", "items", "page_info")
    count = sgqlc.types.Field(Int, graphql_name="count")
    items = sgqlc.types.Field(sgqlc.types.list_of(Sneaker), graphql_name="items")
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PaginationInfo), graphql_name="pageInfo"
    )


class User(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = (
        "username",
        "email",
        "image",
        "device_token",
        "last_signed_in_at",
        "badge",
        "currency",
        "role",
        "is_purchased",
        "is_deleted",
        "_id",
        "updated_at",
        "created_at",
        "_image",
        "_comment",
        "_userfavorite",
        "_userfollow",
        "_postlike",
        "_commentlike",
        "_post",
        "_notification",
        "favorites",
    )
    username = sgqlc.types.Field(String, graphql_name="username")
    email = sgqlc.types.Field(JSON, graphql_name="email")
    image = sgqlc.types.Field(String, graphql_name="image")
    device_token = sgqlc.types.Field(String, graphql_name="deviceToken")
    last_signed_in_at = sgqlc.types.Field(Float, graphql_name="lastSignedInAt")
    badge = sgqlc.types.Field(Float, graphql_name="badge")
    currency = sgqlc.types.Field(JSON, graphql_name="currency")
    role = sgqlc.types.Field(JSON, graphql_name="role")
    is_purchased = sgqlc.types.Field(Boolean, graphql_name="isPurchased")
    is_deleted = sgqlc.types.Field(Boolean, graphql_name="isDeleted")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")
    updated_at = sgqlc.types.Field(String, graphql_name="updatedAt")
    created_at = sgqlc.types.Field(String, graphql_name="createdAt")
    _image = sgqlc.types.Field(
        sgqlc.types.list_of(Image),
        graphql_name="_image",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _comment = sgqlc.types.Field(
        sgqlc.types.list_of(Comment),
        graphql_name="_comment",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _userfavorite = sgqlc.types.Field(
        sgqlc.types.list_of("UserFavorite"),
        graphql_name="_userfavorite",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _userfollow = sgqlc.types.Field(
        sgqlc.types.list_of("UserFollow"),
        graphql_name="_userfollow",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _postlike = sgqlc.types.Field(
        sgqlc.types.list_of(PostLike),
        graphql_name="_postlike",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _commentlike = sgqlc.types.Field(
        sgqlc.types.list_of(CommentLike),
        graphql_name="_commentlike",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _post = sgqlc.types.Field(
        sgqlc.types.list_of(Post),
        graphql_name="_post",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    _notification = sgqlc.types.Field(
        sgqlc.types.list_of(Notification),
        graphql_name="_notification",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("limit", sgqlc.types.Arg(Int, graphql_name="limit", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    favorites = sgqlc.types.Field(
        sgqlc.types.list_of(Release), graphql_name="favorites"
    )


class UserFavorite(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("user", "sneaker", "timestamp", "is_deleted", "_id")
    user = sgqlc.types.Field(
        User,
        graphql_name="user",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    sneaker = sgqlc.types.Field(
        Release,
        graphql_name="sneaker",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    timestamp = sgqlc.types.Field(Float, graphql_name="timestamp")
    is_deleted = sgqlc.types.Field(Boolean, graphql_name="isDeleted")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")


class UserFollow(sgqlc.types.Type):
    __schema__ = sc_schema
    __field_names__ = ("user", "sneaker", "timestamp", "is_deleted", "_id")
    user = sgqlc.types.Field(
        User,
        graphql_name="user",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    sneaker = sgqlc.types.Field(
        SneakerModel,
        graphql_name="sneaker",
        args=sgqlc.types.ArgDict(
            (
                ("filter", sgqlc.types.Arg(JSON, graphql_name="filter", default=None)),
                ("sort", sgqlc.types.Arg(JSON, graphql_name="sort", default=None)),
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=None)),
            )
        ),
    )
    timestamp = sgqlc.types.Field(Float, graphql_name="timestamp")
    is_deleted = sgqlc.types.Field(Boolean, graphql_name="isDeleted")
    _id = sgqlc.types.Field(sgqlc.types.non_null(MongoID), graphql_name="_id")


########################################################################
# Unions
########################################################################
class DropFeedUnion(sgqlc.types.Union):
    __schema__ = sc_schema
    __types__ = (DropFeedRaffle, DropFeedRestock, DropFeedShockDrop, DropFeedSnkrsPass)


class PopularUnion(sgqlc.types.Union):
    __schema__ = sc_schema
    __types__ = (Release, Article)


########################################################################
# Schema Entry Points
########################################################################
sc_schema.query_type = Query
sc_schema.mutation_type = Mutation
sc_schema.subscription_type = None

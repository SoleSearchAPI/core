CREATE TYPE "platform" AS ENUM (
  'retail',
  'stockx',
  'goat',
  'stadium_goods'
);

CREATE TYPE "audience" AS ENUM (
  'Unisex',
  'Men',
  'Women',
  'Youth',
  'Toddler',
  'Unknown'
);

CREATE TABLE "sneaker" (
  "id" integer PRIMARY KEY,
  "brand" text,
  "sku" text,
  "name" text,
  "colorway" text,
  "audience" audience,
  "release_date" timestamp,
  "description" text,
  "stockx_id" text,
  "stadium_goods_id" text,
  "source" platform,
  "date_added" timestamp,
  "last_scraped" timestamp
);

CREATE TABLE "link" (
  "id" integer PRIMARY KEY,
  "sneaker_id" integer NOT NULL,
  "platform" platform NOT NULL,
  "url" text NOT NULL
);

CREATE TABLE "price" (
  "sneaker_id" integer NOT NULL,
  "size_id" integer NOT NULL,
  "platform" platform,
  "amount" bigint NOT NULL,
  PRIMARY KEY ("sneaker_id", "size_id")
);

CREATE TABLE "image" (
  "id" integer PRIMARY KEY,
  "sneaker_id" integer NOT NULL,
  "platform" platform,
  "is_primary" boolean,
  "url" text NOT NULL
);

CREATE TABLE "size" (
  "id" integer PRIMARY KEY,
  "size" integer UNIQUE NOT NULL
);

CREATE TABLE "sneaker_size" (
  "sneaker_id" integer,
  "size_id" integer,
  PRIMARY KEY ("sneaker_id", "size_id")
);

CREATE TABLE "token" (
  "id" integer PRIMARY KEY,
  "platform" platform,
  "type" text,
  "value" text NOT NULL,
  "expires" timestamp
);

CREATE TABLE "sitemap_link" (
  "url" text PRIMARY KEY,
  "platform" platform,
  "last_seen" timestamp,
  "scraped" bool,
  "ignored" bool,
  "error" bool
);

CREATE TABLE "useragent" (
  "id" integer PRIMARY KEY,
  "useragent" text
);

ALTER TABLE "link" ADD FOREIGN KEY ("sneaker_id") REFERENCES "sneaker" ("id");

ALTER TABLE "price" ADD FOREIGN KEY ("sneaker_id") REFERENCES "sneaker" ("id");

ALTER TABLE "price" ADD FOREIGN KEY ("size_id") REFERENCES "size" ("id");

ALTER TABLE "image" ADD FOREIGN KEY ("sneaker_id") REFERENCES "sneaker" ("id");

ALTER TABLE "sneaker_size" ADD FOREIGN KEY ("sneaker_id") REFERENCES "sneaker" ("id");

ALTER TABLE "sneaker_size" ADD FOREIGN KEY ("size_id") REFERENCES "size" ("id");

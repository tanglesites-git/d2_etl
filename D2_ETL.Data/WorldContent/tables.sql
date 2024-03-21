drop table if exists WeaponPlug;
drop table if exists WeaponStat;
drop table if exists WeaponCuratedRoll;
drop table if exists Collectible;
drop table if exists EquipmentSlotType;
drop table if exists ItemCategory;
drop table if exists ItemTierType;
drop table if exists Lore;
drop table if exists Plugs;
drop table if exists Stat;
drop table if exists Weapon;

create table if not exists Collectible
(
    id            integer      not null,
    source_string varchar(150) not null,
    constraint pk_collectible_primary_key primary key (id)
);

create table if not exists EquipmentSlotType
(
    id          integer      not null,
    name        varchar(50)  not null,
    description varchar(100) not null,
    constraint pk_equipment_slot_type_primary_key primary key (id)
);

create table if not exists ItemTierType
(
    id   integer     not null,
    name varchar(50) not null,
    constraint pk_item_tier_type_primary_key primary key (id)
);

create table if not exists Lore
(
    id          integer      not null,
    name        varchar(50)  not null,
    description text         not null,
    subtitle    varchar(255) not null,
    constraint pk_lore_primary_key primary key (id)
);

create table if not exists Stat
(
    id          integer      not null,
    name        varchar(50)  not null,
    description varchar(100) not null,
    constraint pk_stat_primary_key primary key (id)
);

create table if not exists Weapon
(
    id                     integer      not null,
    name                   varchar(50)  not null,
    description            varchar(100) not null,
    icon                   varchar(255) not null,
    item_type_display_name varchar(50)  not null,
    flavorText             text         not null,
    screenshot             varchar(255) not null,
    watermark              varchar(255) not null,
    lore_id                integer      not null,
    tier_type_id           integer      not null,
    collectible_id         integer      not null,
    equipment_slot_type_id integer      not null,
    default_damage_type_id integer      not null,
    constraint fk_weapon_lore_id_lore_id foreign key (lore_id) references Lore (id),
    constraint fk_weapon_collectible_id_collectible_id foreign key (collectible_id) references Collectible (id),
    constraint fk_weapon_equipment_slot_type_id_equipment_slot_type_id foreign key (equipment_slot_type_id) references EquipmentSlotType (id),
    constraint fk_weapon_item_tier_type_id_item_tier_type_id foreign key (tier_type_id) references ItemTierType (id),
    constraint fk_weapon_stat_id_stat_id foreign key (default_damage_type_id) references Stat (id),
    constraint pk_weapon_primary_key primary key (id)
);

create table if not exists Plugs
(
    id                     integer      not null,
    name                   varchar(50)  not null,
    description            varchar(100) not null,
    icon                   varchar(255) not null,
    item_type_display_name varchar(50)  not null,
    tier_type_id           integer      not null,
    constraint fk_weapon_item_tier_type_id_item_tier_type_id foreign key (tier_type_id) references ItemTierType (id),
    constraint pk_weapon_primary_key primary key (id)
);

create table if not exists WeaponPlug
(
    weapon_id integer not null,
    plug_id   integer not null,
    constraint fk_weapon_plug_weapon_id_weapon_id foreign key (weapon_id) references Weapon (id),
    constraint fk_weapon_plug_plug_id_plug_id foreign key (plug_id) references Plugs (id),
    constraint pk_weapon_plug_primary_key primary key (weapon_id, plug_id)
);

create table if not exists WeaponStat
(
    weapon_id integer not null,
    stat_id   integer not null,
    constraint fk_weapon_stat_weapon_id_weapon_id foreign key (weapon_id) references Weapon (id),
    constraint fk_weapon_stat_stat_id_stat_id foreign key (stat_id) references Stat (id),
    constraint pk_weapon_stat_primary_key primary key (weapon_id, stat_id)
);

create table if not exists WeaponCuratedRoll
(
    weapon_id integer not null,
    curated_roll_id integer not null,
    constraint fk_weapon_curated_roll_weapon_id_weapon_id foreign key (weapon_id) references Weapon (id),
    constraint fk_weapon_curated_roll_curated_roll_id_curated_roll_id foreign key (curated_roll_id) references CuratedRoll (id),
    constraint pk_weapon_curated_roll_primary_key primary key (weapon_id, curated_roll_id)
);
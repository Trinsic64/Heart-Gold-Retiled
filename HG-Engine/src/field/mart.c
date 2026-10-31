#include "debug.h"
#include "types.h"

#include "constants/item.h"

#include "pokemon.h"
#include "save.h"
#include "script.h"

#ifdef MART_EXPANSION

struct MartItem {
    u16 item_id;
    u16 override_cost;
};

struct BadgeMartItems {
    u16 item_id;
    u8 required_badges;
};

// note: limited to 203 items (~34 pages)
const struct BadgeMartItems sBadgeMart[] = {
    { ITEM_POKE_BALL, 0 },
    { ITEM_GREAT_BALL, 3 },
    { ITEM_ULTRA_BALL, 5 },
    { ITEM_POTION, 0 },
    { ITEM_SUPER_POTION, 1 },
    { ITEM_HYPER_POTION, 5 },
    { ITEM_MAX_POTION, 7 },
    { ITEM_FULL_RESTORE, 8 },
    { ITEM_REVIVE, 3 },
    { ITEM_ANTIDOTE, 0 },
    { ITEM_PARALYZE_HEAL, 0 },
    { ITEM_AWAKENING, 1 },
    { ITEM_BURN_HEAL, 1 },
    { ITEM_ICE_HEAL, 1 },
    { ITEM_FULL_HEAL, 5 },
    { ITEM_ESCAPE_ROPE, 1 },
    { ITEM_REPEL, 1 },
    { ITEM_SUPER_REPEL, 3 },
    { ITEM_MAX_REPEL, 5 },
};

void LONG_CALL InitMartUI(void *taskManager, FieldSystem *fieldSystem, const u16 *items, int kind, int buySell, int decoWhich, const struct MartItem *priceOverrides);

u16 sCherrygroveCityMart[] = {
    ITEM_OVAL_STONE, ITEM_HEAL_BALL, ITEM_PREMIER_BALL, 0xFFFF
};

u16 sVioletCityMart[] = {
    ITEM_SUN_STONE, ITEM_HEAL_BALL, ITEM_NET_BALL, ITEM_LEVEL_BALL, 0xFFFF
};

u16 sAzaleaCityMart[] = {
    ITEM_LEAF_STONE, ITEM_HEAL_BALL, ITEM_NET_BALL,
    ITEM_FAST_BALL, ITEM_FRIEND_BALL, ITEM_HEAVY_BALL, ITEM_LEVEL_BALL,
    ITEM_LOVE_BALL, ITEM_LURE_BALL, ITEM_MOON_BALL, 0xFFFF
};

u16 sGoldenrodDepartmentUpper2F[] = {
    ITEM_SUN_STONE, ITEM_MOON_STONE, ITEM_FIRE_STONE, ITEM_THUNDER_STONE, ITEM_WATER_STONE, ITEM_LEAF_STONE, ITEM_SHINY_STONE, ITEM_DUSK_STONE, ITEM_DAWN_STONE, ITEM_OVAL_STONE, ITEM_ICE_STONE, 0xFFFF
};

u16 sGoldenrodDepartmentLower2F[] = {
    ITEM_RAZOR_CLAW, ITEM_RAZOR_FANG, ITEM_SWEET_APPLE, ITEM_TART_APPLE, ITEM_SYRUPY_APPLE, ITEM_CRACKED_POT, ITEM_CHIPPED_POT, ITEM_GALARICA_CUFF, ITEM_GALARICA_WREATH, ITEM_METAL_COAT, ITEM_BLACK_AUGURITE, ITEM_PEAT_BLOCK, 0xFFFF
};

u16 sGoldenrodDepartment3F[] = {
    ITEM_BERRY_SWEET, ITEM_LOVE_SWEET, ITEM_MALICIOUS_ARMOR, ITEM_AUSPICIOUS_ARMOR,
    ITEM_METAL_ALLOY, ITEM_SCROLL_OF_DARKNESS, ITEM_SCROLL_OF_WATERS,
    ITEM_ABILITY_CAPSULE, ITEM_ABILITY_PATCH, ITEM_GOLD_BOTTLE_CAP,
    ITEM_ABSOLITE, ITEM_FROSLASSITE, 0xFFFF
};

u16 sGoldenrodDepartment4F[] = {
    ITEM_PROTEIN, ITEM_IRON, ITEM_CALCIUM, ITEM_ZINC, ITEM_CARBOS, ITEM_HP_UP, 0xFFFF
};

u16 sGoldenrodDepartment5F[] = {
    ITEM_TM070, ITEM_TM017, ITEM_TM054, ITEM_TM083, ITEM_TM016, ITEM_TM033, ITEM_TM022, ITEM_TM052, ITEM_TM038, ITEM_TM025, ITEM_TM014, ITEM_TM015, 0xFFFF
};

u16 sGoldenrodHerbs[] = {
    ITEM_HEAL_POWDER, ITEM_ENERGY_POWDER, ITEM_ENERGY_ROOT, ITEM_REVIVAL_HERB, 0xFFFF
};

u16 sEcruteakMart[] = {
    ITEM_STRAWBERRY_SWEET, ITEM_BERRY_SWEET, ITEM_LOVE_SWEET, ITEM_STAR_SWEET, ITEM_CLOVER_SWEET, ITEM_FLOWER_SWEET, ITEM_RIBBON_SWEET, ITEM_KINGS_ROCK, ITEM_MISTY_SEED, ITEM_SMOKE_BALL, ITEM_HEAL_BALL, ITEM_NET_BALL, 0xFFFF
};

u16 sOlivineMart[] = {
    ITEM_METAL_COAT, ITEM_HEAL_BALL, ITEM_NET_BALL, ITEM_DIVE_BALL, ITEM_LURE_BALL, 0xFFFF
};

u16 sCianwoodPharmacy[] = {
    ITEM_POTION, ITEM_SUPER_POTION, ITEM_HYPER_POTION, ITEM_FULL_HEAL, ITEM_REVIVE, 0xFFFF
};

u16 sBlackthornAndBattleFrontierMart[] = {
    ITEM_DAWN_STONE, ITEM_NET_BALL, ITEM_DUSK_BALL, ITEM_TIMER_BALL, 0xFFFF
};

u16 sIndigoPlateau[] = {
    ITEM_ULTRA_BALL, ITEM_QUICK_BALL, ITEM_TIMER_BALL, ITEM_MAX_REPEL,
    ITEM_HYPER_POTION, ITEM_MAX_POTION, ITEM_FULL_RESTORE, ITEM_REVIVE, ITEM_FULL_HEAL, 0xFFFF
};

u16 sVermilionAndSafariMart[] = {
    ITEM_KINGS_ROCK, ITEM_NEST_BALL, ITEM_DUSK_BALL, ITEM_QUICK_BALL,
    ITEM_REPEAT_BALL, ITEM_TIMER_BALL, 0xFFFF
};

u16 sSaffronMart[] = {
    ITEM_SHINY_STONE, ITEM_DUSK_BALL, ITEM_QUICK_BALL, ITEM_LUXURY_BALL, 0xFFFF
};

u16 sLavenderMart[] = {
    ITEM_DUSK_STONE, ITEM_DUSK_BALL, ITEM_QUICK_BALL, 0xFFFF
};

u16 sCeruleanMart[] = {
    ITEM_WATER_STONE, ITEM_QUICK_BALL, ITEM_DIVE_BALL, ITEM_LURE_BALL, 0xFFFF
};

u16 sCeladonDepartmentUpper2F[] = {
    ITEM_SUN_STONE, ITEM_MOON_STONE, ITEM_FIRE_STONE, ITEM_THUNDER_STONE, ITEM_WATER_STONE, ITEM_LEAF_STONE, ITEM_SHINY_STONE, ITEM_DUSK_STONE, ITEM_DAWN_STONE, ITEM_OVAL_STONE, ITEM_ICE_STONE, 0xFFFF
};

u16 sCeladonDepartmentLower2F[] = {
    ITEM_RAZOR_CLAW, ITEM_RAZOR_FANG, ITEM_SWEET_APPLE, ITEM_TART_APPLE, ITEM_SYRUPY_APPLE, ITEM_CRACKED_POT, ITEM_CHIPPED_POT, ITEM_GALARICA_CUFF, ITEM_GALARICA_WREATH, ITEM_METAL_COAT, ITEM_BLACK_AUGURITE, ITEM_PEAT_BLOCK, 0xFFFF
};

u16 sCeladonDepartment3F[] = {
    ITEM_SCROLL_OF_DARKNESS, ITEM_SCROLL_OF_WATERS, ITEM_MALICIOUS_ARMOR,
    ITEM_AUSPICIOUS_ARMOR, ITEM_METAL_ALLOY, ITEM_ABILITY_CAPSULE,
    ITEM_ABILITY_PATCH, ITEM_GOLD_BOTTLE_CAP, ITEM_ABSOLITE,
    ITEM_FROSLASSITE, 0xFFFF
};

u16 sCeladonDepartment4F[] = {
    ITEM_STRAWBERRY_SWEET, ITEM_BERRY_SWEET, ITEM_LOVE_SWEET, ITEM_STAR_SWEET, ITEM_CLOVER_SWEET, ITEM_FLOWER_SWEET, ITEM_RIBBON_SWEET, 0xFFFF
};

u16 sCeladonDepartmentLeft5F[] = {
    ITEM_KINGS_ROCK, ITEM_METAL_COAT, ITEM_MISTY_SEED, ITEM_SMOKE_BALL, 0xFFFF
};

u16 sCeladonDepartmentRight5F[] = {
    ITEM_TART_APPLE, ITEM_SWEET_APPLE, ITEM_SYRUPY_APPLE, ITEM_CRACKED_POT, ITEM_CHIPPED_POT, 0xFFFF
};

u16 sFuschiaMart[] = {
    ITEM_BLACK_AUGURITE, ITEM_DUSK_BALL, ITEM_QUICK_BALL, ITEM_NET_BALL, ITEM_DIVE_BALL, 0xFFFF
};

u16 sPewterMart[] = {
    ITEM_METAL_ALLOY, ITEM_NEST_BALL, ITEM_QUICK_BALL, ITEM_HEAVY_BALL, 0xFFFF
};

u16 sViridianMart[] = {
    ITEM_FIRE_STONE, ITEM_NET_BALL, ITEM_HEAL_BALL, ITEM_REPEAT_BALL, 0xFFFF
};

u16 sMtMoonSquare[] = {
    ITEM_POKE_DOLL, ITEM_FRESH_WATER, ITEM_SODA_POP, ITEM_LEMONADE,
    ITEM_REPEL, ITEM_MOON_STONE, ITEM_MOON_BALL, 0xFFFF
};

u16 sMahoganyPreRocketHideout[] = {
    ITEM_TINY_MUSHROOM, ITEM_POKE_BALL, ITEM_POTION, 0xFFFF
};

u16 sMahoganyPostRocketHideout[] = {
    ITEM_GREAT_BALL, ITEM_TIMER_BALL, ITEM_SUPER_POTION, ITEM_HYPER_POTION,
    ITEM_ANTIDOTE, ITEM_PARALYZE_HEAL, ITEM_SUPER_REPEL, ITEM_REVIVE, ITEM_ICE_STONE, 0xFFFF
};

BOOL ScrCmd_MartBuy(SCRIPTCONTEXT *ctx)
{
    u16 unused UNUSED = ScriptGetVar(ctx);

    u16 items[NELEMS(sBadgeMart) + 1];
    u8 badgeCount = 0;
    u8 index = 0;
    u32 i;

    for (i = 0; i < 16; i++) {
        if (PlayerProfile_TestBadgeFlag(Sav2_PlayerData_GetProfileAddr(ctx->fsys->savedata), i) == TRUE) {
            badgeCount++;
        }
    }

    for (i = 0; i < NELEMS(sBadgeMart); i++) {
        if (badgeCount >= sBadgeMart[i].required_badges) {
            items[index] = sBadgeMart[i].item_id;
            index++;
        }
    }

    items[index] = 0xFFFF;
    InitMartUI(ctx->taskman, ctx->fsys, items, 0, 0, 0, 0); // this doesn't honor price overrides
    return TRUE;
}

#endif // MART_EXPANSION

#ifdef POKEATHLON_SHOP_EXPANSION

const struct MartItem sPokeathlonShop_Sunday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_KINGS_ROCK, 3000 },
    { ITEM_HEART_SCALE, 1000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Monday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_MOON_STONE, 3000 },
    { ITEM_RARE_CANDY, 2000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Tuesday[] = {
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_FIRE_STONE, 2500 },
    { ITEM_PP_UP, 1000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Wednesday[] = {
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_WATER_STONE, 2500 },
    { ITEM_HEART_SCALE, 1000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Thursday[] = {
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_THUNDER_STONE, 2500 },
    { ITEM_PP_UP, 1000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Friday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_METAL_COAT, 2500 },
    { ITEM_NUGGET, 500 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Saturday[] = {
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_LEAF_STONE, 2500 },
    { ITEM_RARE_CANDY, 2000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexSunday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_KINGS_ROCK, 3000 },
    { ITEM_HEART_SCALE, 1000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_NUGGET, 500 },
    { ITEM_SUN_STONE, 3000 },
    { ITEM_FIRE_STONE, 2500 },
    { ITEM_SHINY_STONE, 3000 },
    { ITEM_DAWN_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexMonday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_MOON_STONE, 3000 },
    { ITEM_RARE_CANDY, 2000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_KINGS_ROCK, 3000 },
    { ITEM_SUN_STONE, 3000 },
    { ITEM_WATER_STONE, 2500 },
    { ITEM_SHINY_STONE, 3000 },
    { ITEM_DUSK_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexTuesday[] = {
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_FIRE_STONE, 2500 },
    { ITEM_PP_UP, 1000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_METAL_COAT, 2500 },
    { ITEM_WATER_STONE, 2500 },
    { ITEM_LEAF_STONE, 2500 },
    { ITEM_DUSK_STONE, 3000 },
    { ITEM_DAWN_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexWednesday[] = {
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_WATER_STONE, 2500 },
    { ITEM_HEART_SCALE, 1000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_DRAGON_SCALE, 2500 },
    { ITEM_THUNDER_STONE, 2500 },
    { ITEM_MOON_STONE, 3000 },
    { ITEM_SHINY_STONE, 3000 },
    { ITEM_DAWN_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexThursday[] = {
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_THUNDER_STONE, 2500 },
    { ITEM_PP_UP, 1000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_KINGS_ROCK, 3000 },
    { ITEM_FIRE_STONE, 2500 },
    { ITEM_LEAF_STONE, 2500 },
    { ITEM_SHINY_STONE, 3000 },
    { ITEM_DUSK_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexFriday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_METAL_COAT, 2500 },
    { ITEM_NUGGET, 500 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_DRAGON_SCALE, 2500 },
    { ITEM_WATER_STONE, 2500 },
    { ITEM_SUN_STONE, 3000 },
    { ITEM_DUSK_STONE, 3000 },
    { ITEM_DAWN_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexSaturday[] = {
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_LEAF_STONE, 2500 },
    { ITEM_RARE_CANDY, 2000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_METAL_COAT, 2500 },
    { ITEM_THUNDER_STONE, 2500 },
    { ITEM_SHINY_STONE, 3000 },
    { ITEM_DUSK_STONE, 3000 },
    { ITEM_DAWN_STONE, 3000 },
    { 0xFFFF, 0 },
};

#endif // POKEATHLON_SHOP_EXPANSION

from Protocol.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand
from Protocol.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Protocol.Commands.Client.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from Protocol.Commands.Client.LogicPurchaseDoubleCoinsCommand import LogicPurchaseDoubleCoinsCommand
from Protocol.Commands.Client.LogicPurchaseHeroLvlUpMaterialCommand import LogicPurchaseHeroLvlUpMaterialCommand
from Protocol.Commands.Client.LogicPurchaseBrawlPassCommand import LogicPurchaseBrawlPassCommand
from Protocol.Commands.Client.LogicPurchaseOfferCommand import LogicPurchaseOfferCommand
from Protocol.Commands.Client.LogicGatchaCommand import LogicGatchaCommand
from Protocol.Commands.Client.LogicLevelUpCommand import LogicLevelUpCommand
from Protocol.Commands.Client.LogicBrawlPassTokensCommand import LogicBrawlPassTokensCommand
from Protocol.Commands.Client.LogicClaimRankUpRewardCommand import LogicClaimRankUpRewardCommand

commands = {
	500: LogicGatchaCommand,
	505: LogicSetPlayerThumbnailCommand,
	506: LogicSelectSkinCommand,
	509: LogicPurchaseDoubleCoinsCommand,
	519: LogicPurchaseOfferCommand,
	520: LogicLevelUpCommand,
	521: LogicPurchaseHeroLvlUpMaterialCommand,
	527: LogicSetPlayerNameColorCommand,
	534: LogicPurchaseBrawlPassCommand,
	536: LogicBrawlPassTokensCommand,
	517: LogicClaimRankUpRewardCommand,

}

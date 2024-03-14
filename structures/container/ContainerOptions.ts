import type { ZoloStyles } from '../ZoloStyles';

export class ContainerOptions {
	variationStatus: boolean;
	isBlockRootParent: boolean;
	uniqueId: string;
	FlexDirectionZRPAlign: string;
	parentClasses: string[]; // contains css classs
	zoloStyles: ZoloStyles;
	zolo_advBtnPaddingTop?: string; // number
	zolo_advBtnPaddingBottom?: string; // number
	zolo_advBtnPaddingIsLinked?: boolean;
}

import type { ZoloStyles } from '../ZoloStyles';

export class AccordionOptions {
  variationStatus: boolean;
  isBlockRootParent: boolean;
  uniqueId: string;
  parentClasses: string[]; // contains css classs
  zoloStyles: ZoloStyles;
  zolo_advBtnPaddingTop?: string; // number
  zolo_advBtnPaddingBottom?: string; // number
  zolo_advBtnPaddingIsLinked?: boolean;
}

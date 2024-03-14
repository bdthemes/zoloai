import type { AccordionOptions } from './AccordionOptions';
import type { ZoloAccordionChild } from './ZoloAccordionChild';
import { genUniqueId } from '../lib/nanoId';

export class ZoloAccordion {
	readonly commentOpening: string = '<!-- wp:zolo/accordion ';
	readonly commentClosing: string = ' -->';
	readonly closing: string = '<!-- /wp:zolo/accordion -->';

	private uniqueId: string;
	public numberOfChildren: number;
	public accordionSettings: AccordionOptions;
	public childs: ZoloAccordionChild[];

	private accordionHTML: string;

	constructor(childs?: number | undefined) {
		this.uniqueId = genUniqueId(8);
		this.numberOfChildren = childs || 3;
	}

	getInstance(): string {
		return `${this.commentClosing} ${JSON.stringify(this.accordionSettings)} ${this.commentClosing} 
      ${this.childs.map((child) => child.getInstance()).join('')}
    `;
	}
}

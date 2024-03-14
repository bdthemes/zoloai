import type { ZoloStyles } from '../ZoloStyles';

export class ZoloAccordionChild {
	readonly opening: string = '<!-- wp:zolo/accordion-child ';
	readonly commentClosing: string = ' -->';
	public child: ChildOptions;
	readonly closing: string = '<!-- /wp:zolo/accordion-child -->';

	// biome-ignore lint/complexity/noUselessConstructor: <explanation>
	constructor() {
		// use this later
	}

	getInstance(): string {
		return this.opening + JSON.stringify(this.child) + this.commentClosing;
	}
}

class ChildOptions {
	title: string;
	uniqueId: string;
	parentClasses: string[]; // contains css classs
	zoloStyles: ZoloStyles;
}

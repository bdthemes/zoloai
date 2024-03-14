import containerDefault from '../defaults/container.default';
import type { ContainerOptions } from './ContainerOptions';
import { genUniqueId } from '../lib/nanoId';

export class ZoloContainer {
	readonly commentOpening: string = '<!-- wp:zolo/container ';
	readonly commentClosing: string = ' -->';
	readonly closing: string = '<!-- /wp:zolo/container -->';

	private uniqueId: string;
	private containerSettings: ContainerOptions;

	public constainerHTML: string;

	constructor(child: string) {
		this.uniqueId = genUniqueId(8);
		this.containerSettings = containerDefault(this.uniqueId);

		this.constainerHTML = `
      <div class="wp-block-zolo-container container-${this.uniqueId} alignfull zolo-root-container frontend zolo-editor parent-container-${this.uniqueId}">
        <div class="zolo-container-inner-blocks-wrap">
          ${child}
        </div>
      </div>
    `;
	}

	getContainer(): string {
		return (
			`${this.commentOpening +
			this.containerSettings +
			this.commentClosing}\n${this.constainerHTML}\n${this.closing}`
		);
	}
}

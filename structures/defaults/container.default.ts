import { ContainerOptions } from '../container/ContainerOptions';

export default (uniqueid: string): ContainerOptions => {
  return {
    variationStatus: true,
    isBlockRootParent: true,
    uniqueId: `container-${uniqueid}`,
    FlexDirectionZRPAlign: 'column',
    parentClasses: [`zolo-editor parent-container-${uniqueid}`],
    zoloStyles: {
      desktop: `.container-${uniqueid}.block-editor-block-list__block.wp-block-zolo-container \u003e .zolo-container-inner-blocks-wrap,.wp-block-zolo-container.zolo-root-container.alignfull.container-${uniqueid} \u003e .zolo-container-inner-blocks-wrap { max-width:1200px }.is-root-container \u003e .block-editor-block-list__block .block-editor-block-list__block#block-e05ed572-c50a-4883-9252-38e5a67403ea,.wp-block-zolo-container.zolo-root-container.frontend .container-${uniqueid} { max-width:100%; width:100% }.container-${uniqueid}.wp-block-zolo-container \u003e .zolo-container-inner-blocks-wrap \u003e .block-editor-inner-blocks \u003e .block-editor-block-list__layout,.container-${uniqueid}.wp-block-zolo-container.zolo-root-container.alignfull \u003e .zolo-container-inner-blocks-wrap { gap:20px; flex-direction:column; flex-wrap:nowrap; justify-content:center; align-items:center }.parent-container-${uniqueid} { transition:all 0.3s ease-in-out }.parent-container-${uniqueid}:after { transition:all 0.3s ease-in-out }`,
      tab: `.is-root-container \u003e .block-editor-block-list__block .block-editor-block-list__block#block-e05ed572-c50a-4883-9252-38e5a67403ea,.wp-block-zolo-container.zolo-root-container.frontend .container-${uniqueid} { width:100% }`,
      mobile: `.is-root-container \u003e .block-editor-block-list__block .block-editor-block-list__block#block-e05ed572-c50a-4883-9252-38e5a67403ea,.wp-block-zolo-container.zolo-root-container.frontend .container-${uniqueid} { width:100% }`,
      customCss: '',
    },
  };
};

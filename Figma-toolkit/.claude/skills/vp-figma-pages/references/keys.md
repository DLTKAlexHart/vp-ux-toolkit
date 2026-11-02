# Library keys (2026-11-02)

Keys are stable across publishes, but change if a component is deleted and rebuilt. A key that fails to import means the library was not republished, or the component was rebuilt: look it up again with `search_design_system` and fix this file.

The library is listed in consumer files as "vp-kit - Component Library". Keys below were confirmed importing from a fresh Design file on 2026-11-02 (Banner, Nav rail, Nav item, Utility rail, Button).

Import patterns (run in the consumer file):

```js
const set  = await figma.importComponentSetByKeyAsync(KEY);   // type "set"
const comp = await figma.importComponentByKeyAsync(KEY);      // type "component"
const style = await figma.importStyleByKeyAsync(KEY);         // text and effect styles
const v = set.children.find(c => c.name === 'Type=Primary, State=Default') || set.defaultVariant;
const inst = v.createInstance();
```

## Components

| Name | Type | Key |
|---|---|---|
| Button | set | 51f7bbd5c7f1f5950ce72e6190e758411c07cfd3 |
| Checkbox | set | e21fe3f3dda532cff0223ee7eaf6e43cf1eb303f |
| Radio | set | 25213c06dc86e7f61698e5b5e73ecde0ee15b275 |
| Toggle | set | e356094844107afb6fd5ca47c2d2b883207ccb51 |
| Field | set | 333844cd6060203d104f621e0f88e7a1fc077796 |
| Display field | set | 304fbcff1b839da7e7fff810b1a3a76a2065def7 |
| Status | set | 8aad334e59ad2fe7ed0b4de3a83d5d384689126f |
| Status square | set | dbe886fc141c1a66e84b822b77c20f279bd373d1 |
| Chip | set | d587480fe7e37253693f1f16c854d821fb880295 |
| Message | set | 1fb8014f28fd73ba943a4f5d306fa607bc306e81 |
| Info bubble | set | 07f6f7b7a3af89a65849d58aaf8a16b0de0614f6 |
| Tab | set | 626880a2e4652918d6ac67603b9a0f047d0dcc6b |
| Search | component | c4dddc566b4efbfed10a6e4ca99af7f00557f9eb |
| Menu item | set | 8cf4d472ebd10a6671b9a4f0b9a84d3d7bea86ee |
| Menu | component | 64d32c6a112c3d6aeb144fd06277fb58e4750dd7 |
| Dialog | set | 97a8fbab5dd5a8422eb834607f2226a996904f1f |
| Grid cell | set | 57a72d599c3a4c96070a45a79220c8b8f63642a9 |
| Grid section | set | 01c4e99032a694dbddd5e94796a1ad73b615cd3f |
| Action bar | component | 51e4979f8ff5a32990354634447bfee0f0fa69da |
| KV pair | set | 1eb474a9d0ad0357d21895a62c1e1238c30a371c |
| Panel | component | 8859396cc4208ef80a91bcbbb314f142beb89282 |
| Section title | set | 807489fff55031fdbe0cf81b7e1f94936e00bd62 |
| Banner | set | 3183b80e44553ca5b7ea991548eac1a0d72c5a1e |
| Nav item | set | 24972060b0302e0eaa3d901524d1ceeb94364534 |
| Utility item | set | 05455cb074e797f0604e59a55ad5f0dbada44d04 |
| Flyout item | set | 64a973843a2c3de43d3ba0a979daacbd8c79b21b |
| Nav rail | set | 3a667a93b80e8a767d88ddc6f0b1bacbc255503f |
| Nav flyout | component | 4e1d2a9342ac7c61bb549926ee3dac3b83fdae9b |
| Utility rail | set | 74be0a5d7030f20039a614722e9ebde28ad47031 |
| Settings sidenav item | set | d7caffaebd5a55d1b933af500a45bea9214926d4 |
| Settings sidenav | component | 22079251d04c1e966c2f939b4505870c70b812e5 |
| Hub toolbar | set | 05c57342bb5eec5cd78fcfa3c235953b882f90dd |
| List toolbar | component | 2e4ac3ae5e965c1384d14f43c628dde58adc6632 |
| Record header | component | 807ea621d25a078db92c1caad15abfeabf94c6d8 |
| Record sidebar | component | a03da5d6498dbca2d32774809fe6f939863abd8e |
| Filter popup | component | 856cae4d620c03bcff9cfdc5b9d8484d1a4fdcc4 |
| Badge dot | set | 5d39eaa1db67747a624a8664067d2be6e56eff60 |
| Divider | component | a00101c5c8b9ec01a4adb737353585a06803ee30 |
| Page header | component | 53898bfc65e6b071990738c237e1ac0cd412a44e |
| Grid toolbar | component | a9aef335b6e34200739c888feba7382728353bbe |
| Stage text | set | 6a0474241b5496bbbeb78a07ba662624d53973c1 |

## Text styles

| Name | Key |
|---|---|
| Heading/Record name | 92c2dac70b634021bf4e59c40d59cf154c236a1b |
| Heading/Page title | d581dbecc88e90baa961f0cec014791bd25bba2c |
| Heading/Dialog title | 772373460c7a0ffb9f92b4dfd11f41eeb61afa8d |
| Heading/H2 | c48318c3202338463822ad11b02fc451133239a3 |
| Heading/Section title | 349571d585f24224bbe2035367858c83415222aa |
| Heading/Panel title | 2430e9f06900fc5371a0c4b0d9d3c664c7b3d961 |
| Heading/Confirm title | 6b3fe1967ece9c486db831b4ed23cc6de44f0e13 |
| Heading/H3 | 2d91549d4f534699bcc410f46b23e11a8fb1e35d |
| Heading/Grid section title | b806ac95565b960a42f6b4e9224ea65490711db8 |
| Heading/H4 | 40206d6c927a9dfef434f098d5c8861cec2fc276 |
| Body/Base | d1f2daef907f5f8988f25ee42db9cbbb5237a636 |
| Body/Value | 39b5d9979f502d667c9e9d0bb776159cd1b0b5b3 |
| Body/Small | 6d5251c4872b3f0c28367d42757b21d2531a9ead |
| Body/Small medium | 9c67fac4eab20c02cc12f6388792a26511350114 |
| Body/Caption | c468aad67d2881dcb15ee445d8605578c11eeb71 |
| Body/Status | 7778aaf13ff70d462ce2638afcfdfd20a047c9e2 |
| Body/Note | e4e95cbcf916e15873cfe6a4827a3e90357464e9 |
| Body/Caption italic | df2106737b177ecfe2f73b615c2f359778437d53 |
| Label/Field | e5a05350913d4308b40c107e63904ccfd71bc833 |
| Label/Input | 400af0e6848567285ed91b6af2b9a7f9f0d9a682 |
| Label/Section | 7c718784e96f64a71b43aa736f91a69c4bf2a77d |
| Label/Sidebar | 5bbdcb46ad7eed54913b18fde6d0a8eef79e6b3d |
| Label/Avatar | ae8f1c90a28210ea5f190a3c707654ed2dc6d828 |
| Label/Micro | aad192dc483947c7b047f346eeb3b516974ec3c8 |
| Label/Key (uppercase) | 48c2e060f2d21c1879e34aa5409013c526cef339 |
| Label/Overline | 804e82d71bf3b674df07b3c3877ce54f98db6595 |
| Label/Sort | 4ce03a8e219bae620c028d0ac1284a7d5b96219d |
| Button/Default | 3383830925c604795768f43307a61b525a4bfdf9 |
| Button/Small | 7b6de5fa14898dfc7f95d3f876cda0458eac6230 |
| Button/Add | 1d2953d3f63821a33487da0986f67424b3e3587a |
| Button/Mini | 5f7df00b69b924350a2a067b1a1ae9a8a0f1444c |
| Tab/Default | ffc787b479cbf0efac4671e761cd89fd9b4c9454 |
| Grid/Cell | 2c0159fc86649302a9510686bad96268b7c37481 |
| Grid/Header | 9cde398eaa950d135e1c1b020c6b4a93ef9c5e1b |

## Effect styles

| Name | Key |
|---|---|
| Shadow/dialog | dbfc33f3f587a061ae95027bd1a240f678ef8550 |
| Shadow/drop-target | 8ab35b628b1b9802e63c825333a6a4a58bae5e90 |
| Shadow/focus | d6dc87e8f83c33896164b0d1fafd707d65cbb4f1 |
| Shadow/image | b876f871571eb43258b6c28c9fa5bdb0e503635a |
| Shadow/nav | ed8c0349ed32c0a9a8bdb29d6ea4306131106b44 |
| Shadow/nav-toolbar | 77be7f59091f283cfd01f5bd4b7dd1384910a6d4 |
| Shadow/popup | 4e60f1aeb7f4feadca1f81087d306ea8c49fd017 |
| Shadow/side-toolbar | 8a4ec0537cb7b94fc110cd32b90f371cd04ac009 |
| Shadow/tab | fc2dc1ea4d04b55a06ac86b9d2751e3ad9b0913e |
| Shadow/thumb | 2d2f22b5ea1130206c6fa6df4f8a62131a17d055 |
| Shadow/tile | 89f802f905a895889209a0d9a1bd9edd06d0fc4b |
| Shadow/tooltip | 904acf383dccce60b82a3b65b22c02f78a47f1db |

## Brand (import with importComponentByKeyAsync, except Logo/Deltek which is a set)

| Name | Key |
|---|---|
| Logo/Dela | 2f004474e8a4986fe675a5e6c5949cb8317f77c5 |
| Logo/Dela mono | 313cde63473219a3d5569f4dcfc29496d32b7dab |
| Logo/Deltek (set) | e2140c2e761a882e9993fc31aa4fde5d2d40b88d |
| Logo/Vantagepoint short | 0fc2959dac8963557d3afd2ed9c796cbdc297055 |
| Logo/Deltek Vantagepoint | 2e0a2adb96f7323ec1620169d1b51bb359d3ff93 |

## Icons (components, instance and swap by key)

| Name | Key |
|---|---|
| Icon/search | 356b52bc756958ac56c1189488df430cdf997c20 |
| Icon/bell | b1931badb9afe1ebae175bd2b9919891cbbdab28 |
| Icon/help | c784170812290936b3475b81cefd21b6efd8de3c |
| Icon/settings | 4c6ecff5fe6db840e0682eb070f134b9223781ee |
| Icon/menu | 796faf165d5d0045315b224f1730c742cfb2c405 |
| Icon/dashboard | dbd32212e3c34284b6fbc66a1ae49ba78cd6b60c |
| Icon/folder | 5eacbf4da41c2fa609fa427b99d50330c8980fc5 |
| Icon/users | 8a43975d281b4ec4c8bf701e7e49cb82c229d9d1 |
| Icon/building | 826ef384d135a3b5fe76bd3b6d5b07dec05f9ad6 |
| Icon/clock | 5da8b6d142a073d5187bcf0b821236c2b941f450 |
| Icon/dollar | 2bf4f8e3ba94d2f93c4eb6bf0324af7fc9265ab0 |
| Icon/chart | cb0488e97a751b479e149f3154e1044a1df4903d |
| Icon/plus | cae521d0f6e2dc6fa3a688a93a1fb9cd21cab7be |
| Icon/chevron-down | d21831210c4008974cffa3777a60896d49cd4a6d |
| Icon/chevron-right | d9f56397151a2e91b181e325c4a10a6e72293a4d |
| Icon/dots | 9fd7924a414c1aa22bb736f71eb38691906f6743 |
| Icon/x | 97083cc42f8b450ec9267a736d0559777e84da41 |
| Icon/filter | fe9c789a9eee1cd2baeb1e2373ab9ffbbfa4e7c6 |
| Icon/columns | 8813c6cc00827e35e8ebd449ef357338fcbc8350 |
| Icon/download | 5eab128f22f96f9b1f688f8b56899f622c02eab5 |
| Icon/pencil | 1d4ea9ffb2884f3b04830a9b522c2b385989f1b7 |
| Icon/star | c0b295ca856d4fd7fd9ef0cd15af0ae038247af5 |
| Icon/arrow-left | 608c93bb146a9a738350b039951e6aae019553cb |
| Icon/calendar | aec931e99d01e0378fd911b3ee60eaa35eece63c |
| Icon/check | 75917b47518a97a74ac743deec032d6af2ea25bf |
| Icon/briefcase | ca99f7e9b5c48317a11ed3bab1cc8384e91fdaf0 |
| Icon/pin | 9e1b426a565bc039fdbca57e2bdf704b7ec21f8e |

## Reference templates (in the library file, not importable)

Template / Hub record 23:269, Hub record (Dark) 24:459, List view 31:752, Settings form 33:1012, all on the `Templates` page. Use them to read structure with `get_metadata` or `get_design_context`; build real pages from instances.

## Dashboard additions (2026-11-02, from this repo's dashboard shell additions)

Note 2026-11-02: Nav rail and Utility rail now have only the Floating variant. Purpose panel was never published (not needed; the AI purpose feature is out of scope), ignore any older reference. Slot children (Dash card Body, Dashpart widget Grid) have composite ids like `I10:623;61:157;10:724` that do not survive between calls: find them by name from the page root.

Import sets with importComponentSetByKeyAsync and plain components with importComponentByKeyAsync. These keys are from the unpublished file state: re-check after publishing.

| Name | Type | Key |
|---|---|---|
| Widget cell | set | cf76c6bea46ae9d4bd09d1dfaa1991ebe34cad8c |
| Widget tool | set | b3b78ca70421be5ee5175ab4432db6086e61e404 |
| KPI tile | set | 128a64be15e18acf588c067ed2ff87feb5a5ebb2 |
| Dashpart widget | comp | 2b8285dc327d599fa5bac10bc511366bf07beeab |
| Suggest pill | set | f9f101eb7f84de3f68007ce735771b27fc30b23f |
| Dela draft card | set | 146a86f5f8910754b7a4ee4f194e2398b05413b5 |
| Purpose panel | set | 81a415a0b4b7f612dbd1ef12595efcc4b6c0f692 |
| Dela pane button | set | 3a8f2de39c535cb344a6dd14fb72a14384c97018 |
| Dela message | set | dcb1640fd451cf5df19d2386e6c0a907d566113d |
| Dela composer | set | a008662c4d00d041a308197458ea2bf9b377a580 |
| Dela pane | comp | 88e51164dd0170f42e93745a4a8a9d951e16137c |
| Dela citation | set | 7655cca65f765751c50bea1ff79744c10f967234 |
| Dela pill | set | 00a13dad29bda44908e09663f89f322f3083c7ef |
| Dela tag | comp | d2072ddd573f559e9fa271399a3b60932176481a |
| Dela card heading | comp | 74b352e43e77e2c85a16a614aeb38642979db5ba |
| Dela card item | comp | a6151c2260f098338f7897295ff4b0741f0ba8eb |
| Dela card | comp | c180264256e8ef7b39156667aca770937a67adf0 |
| App header | comp | 73842f366af8a4264e0339e4c8f4553cfd757552 |
| Dash toolbar button | set | 9cf913a3db0ada1f7bd666998bd36d75e0b38807 |
| Dash toolbar | comp | f2d14da3c0bbd83196051698408990bc3d635089 |
| Dash card | comp | b3065f912ee2960d0ab6e7a9917e800909ea1e74 |

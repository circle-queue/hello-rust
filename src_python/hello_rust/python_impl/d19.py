import itertools
from typing import Literal, NamedTuple


class Condition(NamedTuple):
    attr: str  # E.g. 'a'
    check: str  # e.g. ' < 1716'
    ok_dst: str  # e.g. 'R' or 'A'

    @classmethod
    def from_str(cls, s: str) -> (str, list["Condition"]):
        name, conds = s.split("{")

        conditions = []
        for cond in conds.strip("}").split(","):
            check, _, ok_dst = cond.rpartition(":")
            if check:
                conditions.append(cls(check[0], check[1:], ok_dst))
            else:
                # No check, so "check" is actually our next stop
                conditions.append(cls("a", "!= None", ok_dst))
        return name, conditions


def solve1(input: list[str]) -> str:
    parts = [
        eval(line.replace("{", "dict(").replace("}", ")"))
        for line in input
        if line.startswith("{")
    ]
    id_to_rules: dict[str, list[Condition]] = dict(
        [Condition.from_str(line) for line in input if not line.startswith("{")]
    )

    total = 0
    for part in parts:
        rule_id = "in"
        while rule_id not in ("R", "A"):
            rules = id_to_rules[rule_id]
            for rule in rules:
                if not eval(f"{part[rule.attr]}{rule.check}"):
                    continue
                rule_id = rule.ok_dst
                break
        if rule_id == "A":
            total += sum(part.values())

    return str(total)


def solve2(input: list[str]) -> str:
    # input = """in{A}""".splitlines()
    id_to_rules: dict[str, list[Condition]] = dict(
        [Condition.from_str(line) for line in input if not line.startswith("{")]
    )

    complete_paths = []
    condition_q = [(Condition("", "", "in"),)]
    while condition_q:
        path = condition_q.pop()
        rule_id = path[-1].ok_dst

        if rule_id == "A":
            complete_paths.append(path)
        if rule_id in "AR":
            continue

        rules = id_to_rules[rule_id]
        inverse_rules = ()  # The previous must fail for the next to succeed
        for rule in rules:
            condition_q.append(path + inverse_rules + (rule,))

            if rule.check[0] == "<":
                new_check = f">{int(rule.check[1:]) - 1}"
            elif rule.check[0] == ">":
                new_check = f"<{int(rule.check[1:]) + 1}"
            elif rule.check[0] == "!":
                new_check = rule.check
            else:
                raise NotImplementedError(rule.check)
            inverse_rules += (Condition(rule.attr, new_check, rule.ok_dst),)

    path_conditions = []
    for path in complete_paths:
        path
        basic_rules = tuple(
            [Condition(char, cond, "") for char in "amsx" for cond in (">0", "<4001")]
        )
        path = tuple([cond for cond in path if "!=" not in cond.check])
        ordered_conditions = sorted(path[1:] + basic_rules)
        char_conditions = {}
        for group, conditions in itertools.groupby(
            ordered_conditions, lambda c: (c.attr, c.check[0])
        ):
            check_values = [int(c.check.strip("><")) for c in conditions]
            if group[-1] == ">":
                char_conditions[group] = max(check_values)
            elif group[-1] == "<":
                char_conditions[group] = min(check_values)
            else:
                raise NotImplementedError()
        path_conditions.append(char_conditions)

    path_ranges = [
        {char: range(range_[char, ">"] + 1, range_[char, "<"]) for (char, _) in range_}
        for range_ in path_conditions
    ]

    total_comb = 0
    for ranges in path_ranges:
        combinations = 1
        for range_ in ranges.values():
            combinations *= len(range_)
        total_comb += combinations

    return str(total_comb)


sample_input2 = sample_input1 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}
{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}""".splitlines()

full_input1 = full_input2 = """fxr{x>387:R,a<752:R,s>1381:fb,sn}
dds{m<1139:jr,s<1864:jct,R}
dt{m<2896:vr,xt}
sz{s<1606:cnp,R}
zzb{m<3467:rnc,s>3815:R,qqs}
kh{m<3815:A,s>592:R,A}
jj{x<2953:sfj,m>549:R,A}
qzl{x>2819:gvl,s<3517:xz,s<3728:htx,fsq}
xz{a<1471:gxc,mp}
dlv{s>1732:A,x>704:tzs,fq}
jh{m>1781:R,R}
tzn{x<275:R,m>3397:R,kcv}
vdl{s<1312:ppg,s<1688:bd,m>1062:jmk,zbh}
zm{m<2770:vb,thf}
dxd{a>3268:R,m<3138:R,s>515:R,A}
mrv{a<3117:A,R}
ngd{m<796:A,x>809:A,x>685:R,A}
fzd{s>1412:qcj,A}
xtl{m<2980:kjb,m<3130:dxn,R}
fsg{s>1661:rm,zmt}
zt{m<3631:A,a>993:A,m<3685:R,R}
bn{s>2462:A,R}
znn{s<2343:mb,kzn}
hgd{s<2100:cx,A}
bgk{x<3493:R,dl}
kq{x<1598:crq,m>3282:brb,a>1327:A,A}
mvb{x>1700:A,R}
dfg{a>1208:brc,m<952:hmk,tmk}
pcb{m>710:zrc,x>2685:A,tdg}
bqq{m>1206:ckf,s<3406:nkt,m<739:fqg,fch}
xrg{a>1435:R,x>3728:A,x<3711:knr,zhj}
gd{s<639:R,x>800:R,m>3655:A,A}
ds{s<3740:zqv,x<3251:R,a>1748:lb,fl}
ff{s>3133:A,m>2918:R,m>2744:A,A}
klt{s<780:A,x<2427:R,a>1562:A,A}
hs{x>2064:R,A}
qcj{s<1497:A,s<1512:A,R}
kc{s<1570:A,R}
lzr{a<2023:R,A}
mms{s>2760:A,m<916:zb,mq}
kks{s>1321:df,x>1286:mfj,hgx}
dh{x<2779:A,m>572:R,R}
bc{s>2724:R,a<262:R,R}
hn{s>2717:R,m>3726:fkv,m>3413:sq,R}
cx{s>778:A,m>1497:R,A}
gvn{a<3079:R,m<3064:R,A}
lsm{a<3319:lz,m<929:xc,R}
jv{m<276:A,R}
nmr{x<3119:cl,xqj}
hnj{m<554:zx,s>2350:A,x<3578:cxl,rbh}
tr{s<179:A,A}
zr{s<2483:A,A}
fn{x<3543:A,R}
jpz{s<253:A,m<272:A,x>2789:A,A}
hq{s<1702:mqn,x<3035:cqm,m>866:sj,lzr}
lz{a>2980:R,s<3374:A,m<1157:A,R}
hrx{a>869:R,m<2843:A,s<2361:R,A}
sjd{s>3443:A,a<3057:nvj,x<740:A,A}
xb{x>920:lpj,a<523:A,x<382:A,A}
pxh{s>526:A,A}
qd{x>1997:R,s>2030:R,x>1917:A,R}
xl{a<192:rv,vdr}
jbx{a>3649:R,mvb}
vh{a>1478:R,m<3088:A,A}
nd{x>2524:A,m<1268:R,A}
zrc{a>1035:A,A}
hjk{s>1250:dnn,a>1163:ndf,m>1379:zcv,rjb}
bp{s>1723:mxk,hjp}
nvj{s<2798:R,m<1158:R,s>3174:A,R}
rxx{x<2792:A,s>351:R,R}
kdj{m>2780:A,A}
tzs{s>844:R,R}
fr{m>3789:R,a>1717:R,m>3644:R,R}
bvq{x<3598:qxz,x>3763:npf,x<3701:cc,xrg}
clj{s<3489:qt,a>1043:R,s<3828:R,A}
brb{s>809:R,R}
fnd{a>1376:R,m>2369:A,R}
xhx{a>1184:R,s<2676:R,m<3079:R,A}
zrk{x<451:nb,A}
dhg{s<3172:A,a>1399:R,x<2368:A,A}
tg{x<1271:nk,zdg}
mm{s>2916:gg,rxj}
hpx{a>862:A,m<787:vsv,a<807:cfh,xpb}
fts{x<2853:dds,m>1519:sx,s<1369:dhz,mms}
sdk{s<1095:A,s<1756:R,A}
tmk{x<3193:R,s>3521:A,A}
drj{m>1575:hpd,x>605:hgd,s<1335:kgm,fg}
jlt{m>2719:R,m<2606:R,x>325:R,R}
vsq{x<1755:A,s<2371:R,A}
pc{a>2493:rg,a>2002:gq,bp}
svq{m>2556:A,x>2672:A,s<2453:R,R}
sqh{a<1445:js,s>1591:R,s>1477:R,A}
grb{s>2580:lsm,a<3313:rt,hk}
rqg{s<3949:A,A}
zpd{s>794:A,x<2667:A,R}
rqt{a>1658:mx,a<777:dxq,s<2616:hjk,pkm}
gtb{s>3730:R,s<3589:A,s<3676:A,A}
zlh{x<1712:R,a>427:R,x<1771:sdk,cm}
td{m>3499:A,m>3414:gt,a<494:A,kgq}
dgt{a>825:ct,pxh}
km{s>654:nqs,nmn}
ppg{m>1247:A,A}
slk{x>2763:A,x<2485:R,s<966:R,R}
trv{x>539:sjd,x<264:cfd,a>2787:bqq,lpr}
snv{s>305:A,x<556:A,s<183:R,A}
gg{s<3016:A,s<3084:A,R}
dns{m>3482:fzd,xvg}
sq{x<2606:A,a>322:A,x<2839:A,A}
pvk{s>1304:A,m<2685:A,R}
rxq{m>2599:qg,m<2492:bq,zq}
pn{a<589:R,m>1655:A,a>992:R,A}
lv{m<3175:vf,a<3191:vt,x<751:cn,jbx}
ct{s<558:snv,a<1249:dzx,jvt}
dzx{m<2863:R,a>1097:A,A}
js{m<512:A,A}
fpr{a<986:R,x<2658:R,A}
gz{a<1509:A,x<3783:A,R}
zjm{a>1035:A,m<3225:A,A}
xsm{a<1660:R,a<1844:R,x>2014:A,A}
mls{m>424:ln,zrk}
grj{x>1079:A,A}
kn{s>142:R,a<1016:R,A}
mxk{a<1780:A,a>1859:R,m>3461:A,R}
vn{s<1454:sl,R}
njz{m<1859:R,A}
dzk{x>3558:kcd,nf}
zsk{a>476:A,x>530:ngd,x>267:cfl,A}
zd{m>616:R,s>838:ddb,A}
qxk{m>2824:qkg,qx}
nrr{m>1084:A,s>971:R,s>789:A,A}
hm{m>3025:vfv,nz}
lpj{m>3793:R,s>1805:A,R}
mf{x<2463:R,s<3847:zjt,rqg}
gvj{s>223:zkv,x<3876:kn,a>1010:R,dr}
fbs{x<3091:qdb,mxf}
psz{m>3320:fpr,m>3250:R,x<2725:tq,R}
jhj{m>3760:A,m>3731:A,A}
gt{m<3463:R,x<722:A,R}
hx{m>886:A,m>732:A,A}
kg{x>3062:jsh,R}
bxh{m>1510:A,a>677:A,m>1488:R,R}
vfv{s>3630:A,a<1123:A,m<3122:R,R}
tv{s>2870:pmp,m>1164:qj,bc}
bnz{s>2128:ktr,vdl}
cjd{m>2809:R,R}
rf{a<1243:R,m>2603:R,A}
mfs{x>3237:A,A}
xh{m>3128:R,s<3715:R,A}
jp{a>2848:fhg,s>2879:A,R}
rh{s<180:xst,a>1234:xsm,qnj}
ndh{x>3590:A,A}
qxz{m>1434:xr,s<417:jds,x>3320:A,ffq}
sdj{a>703:R,s>233:A,m>1528:A,A}
csm{x>2471:R,s>3581:A,R}
ps{x>2328:A,A}
mnl{s<3342:xjb,x>2880:zn,hg}
sg{s>3292:vl,vsz}
nc{s>863:R,A}
fv{a>724:R,a<329:R,A}
qr{a>985:R,x>2015:R,x>1932:R,A}
rdl{s<1344:A,s>2529:mj,s>2040:A,R}
xc{m<479:R,m>684:R,a<3738:A,R}
zbh{m<549:R,a<2124:R,a<3008:xx,vgc}
md{s>824:A,s>535:A,A}
vs{a<3669:R,s<2516:R,m>3794:A,R}
zj{a>3051:R,R}
mqn{m>1072:mfs,a>2014:A,m>664:jrv,nsk}
fkv{m>3849:A,s<2506:A,R}
lxq{a>1465:R,s<3588:A,x>2736:R,A}
zrn{m<2517:qjr,s<2143:gc,zs}
kx{x<2618:gcr,a>458:rrm,slm}
crq{m<3432:R,m>3631:R,R}
ntx{m<153:A,a>1706:A,A}
llr{x>1921:A,a>1003:R,R}
hcr{s>3586:R,x<2442:R,A}
hzs{a>3176:R,R}
jkv{m<3505:R,s<3505:A,R}
xk{m>2872:A,s>1806:R,m>2825:R,R}
fq{x>604:A,x>560:A,A}
mhr{s<533:R,m<3751:R,m<3850:R,A}
rbh{a<507:R,A}
tnl{a<962:R,m>1767:A,R}
qtk{m<1445:A,s>1979:A,x>1611:A,A}
gvl{s<3240:dbz,x>3507:nx,a<1452:kg,vj}
xj{m>1276:A,m>739:A,a<2261:A,A}
tlp{x>2776:R,x>2418:A,m<2983:A,A}
tq{s>3596:R,a<1059:R,R}
zz{x>362:tk,a<688:R,A}
rt{m<1209:A,a>3063:hzs,a>2949:A,R}
kcv{a<3269:R,x>395:R,R}
ddb{x>3833:R,a>970:R,m>251:R,A}
hk{m>1324:njz,A}
sm{s<2928:A,x<2433:A,R}
vr{s<2227:qsq,x>3540:qc,A}
tn{s<3175:R,s<3690:A,a>908:R,R}
ln{s<3229:A,s>3702:fv,cj}
hql{m<2948:lh,m<3270:vlh,nmr}
txr{a<949:chl,xcv}
zdg{s<880:qq,mrv}
mb{m>2828:md,x>3659:mhl,R}
slm{s<3600:R,a>231:txt,R}
in{x>2187:rqt,zrn}
cdj{m>3680:A,A}
zn{x<3349:R,s>3779:A,R}
nh{m>3074:A,s>3081:nfz,s>2486:jlt,hrx}
nxh{s<467:rh,sp}
ml{x<3377:R,a>1817:R,R}
pj{a>1449:A,fnd}
xkx{m>478:gx,s<1114:kb,R}
tf{x<2576:lmr,m>3034:R,qmn}
dr{a<958:A,A}
gbz{x>3659:R,A}
cj{s<3426:A,A}
tfj{s<3594:R,s>3615:R,x>2437:R,A}
ckf{a>3590:R,x>438:A,s<3110:R,A}
rkv{s<958:A,x>2427:R,A}
gs{a<322:A,m<1834:A,A}
pv{s<1719:R,a>185:R,A}
kd{m>3623:R,a>3055:A,A}
vt{x<774:A,m>3551:mrs,R}
dzl{m>1548:R,m<832:A,R}
dbz{m>2501:hp,m>1237:fn,x<3271:R,A}
vl{s>3563:A,R}
sp{x>2041:jjj,m>3338:pd,a>672:R,ns}
mcc{a>843:kfc,m<3321:xtl,m<3672:td,xb}
sgv{x<2402:qgn,a<1075:A,csm}
bst{a>1595:jjx,nh}
dnn{a<1179:fbs,ck}
lm{m>1644:R,m>950:R,m>453:A,R}
jds{x>3345:R,A}
xr{x>3440:A,x>3338:A,m>2689:R,A}
sl{s<1413:R,m>3475:A,s<1439:A,R}
htb{s>3626:A,s<3564:dpm,a<1533:smk,tfj}
hh{m>3184:pz,x<1598:hth,s<1273:R,kdj}
df{s<1339:R,a>712:R,A}
fl{m<373:R,m<825:R,A}
cqs{m>3246:hn,a>438:mmj,s>2690:mm,bdg}
cm{m>3143:A,a<271:R,A}
lnp{s<2823:R,a>1198:R,A}
dpm{x<2406:A,R}
rnc{x<1260:A,A}
kf{x<2523:A,gsc}
st{a<984:A,x>3040:R,A}
grh{a<968:vsq,x<1710:R,x>1980:pft,A}
mxf{m>2589:R,s<1878:A,A}
tlr{x>212:R,m<1300:lmz,x>134:R,A}
pmp{s>2984:R,x<2750:R,A}
kgm{s>684:bxh,sdj}
nz{s>3680:A,x<2711:R,A}
hj{m>468:R,a>1334:A,jpz}
nsk{s<606:R,R}
gc{a>1942:tg,x>1452:cvq,s<1213:kps,rlm}
rjb{x>3046:rcm,bzs}
nn{a>893:A,R}
dpt{s>3560:R,qhc}
vkn{s>3622:A,a<976:R,R}
kl{s>3176:R,A}
zmt{m<3605:fck,a<750:A,A}
bd{s>1443:R,xj}
jjx{s<3339:lfz,s>3750:srf,A}
rkt{s>1835:A,x>2035:R,m<3485:A,R}
nhc{x>2569:R,R}
mrs{x>1458:A,x<1018:A,A}
bq{x>2850:A,x>2439:A,R}
rxn{s>2537:R,x>2737:R,a<289:A,A}
nzg{m<636:R,a>790:A,A}
rpj{s<1966:A,s>2074:A,x>2072:A,R}
xf{s<815:msz,m<1861:sz,hcq}
qx{m<2037:bf,m<2524:R,A}
rxj{s<2816:R,x<2803:A,A}
zf{x<2538:jc,m<3187:hm,psz}
vv{a<1290:nrr,m>1076:slk,a>1321:hx,A}
px{x>115:R,A}
jr{m<598:R,x>2591:R,A}
kjb{a<384:A,a>621:A,R}
hz{s<2399:ffj,trv}
vf{x<945:A,bn}
lf{m>1109:hsd,s<2503:sh,s<3454:jj,ds}
hsd{s<1932:A,x<3025:ch,A}
jtr{s<142:R,a>1018:cr,qss}
vg{m<3527:A,m<3758:R,a<349:R,R}
jrv{a>1928:R,x<3118:A,a>1902:R,A}
qdb{x>2536:tnl,jrn}
rz{m>3013:pc,rxq}
jnd{a<699:R,s>1253:A,a>1511:R,A}
xcv{m<3557:A,a>1498:fr,m>3708:kh,gd}
nr{s>498:dh,x>2708:R,s>242:A,A}
vlh{s>2857:R,a<981:R,s>2724:zk,xhx}
qkg{a<943:nbb,zjm}
pzg{m>3036:gp,pk}
qvg{m<3693:sk,s<3471:pvg,jcb}
jc{a>1089:A,xh}
vch{a<1432:zpd,m<2773:km,s>505:fhn,kf}
xzk{m>2079:A,x<470:R,A}
rlm{s>1542:mcc,x<662:pzg,x>1156:lgp,dns}
dfc{m>2382:R,A}
pvc{s<2759:A,s>3572:A,m<1375:R,R}
vb{s>1675:qr,m<2628:A,x<1961:pvk,hs}
vgc{s>1902:R,A}
knn{x>2559:A,s<2146:R,m<3157:R,R}
pls{a>1057:A,R}
sfj{x>2695:A,R}
cvq{x<1846:tj,s<1069:nxh,m>3148:fsg,zm}
npf{a>1493:A,a<1330:A,a<1421:A,R}
qgn{x<2318:R,m<2680:A,m>2804:R,R}
ck{s>2096:pdc,x>3055:bx,m>1372:tf,sqh}
fck{s<1426:R,A}
bk{s>2778:R,m>844:R,A}
drx{x<2517:sgv,dpt}
pq{s<642:R,R}
zcv{s<576:vrs,qxk}
mj{m>1761:A,m<1570:A,m>1692:A,A}
dfk{m<3042:R,R}
knr{a>1293:R,R}
szf{x<370:R,R}
hjp{a<1852:A,R}
qf{x<753:bst,sg}
nmn{a<1510:A,m<2097:A,s>242:R,R}
zq{x>2996:A,a<3146:lts,svq}
smk{s>3585:A,A}
ph{s>677:A,a>963:mv,s<316:nn,A}
vrs{s<292:jtr,vdk}
vzq{x<445:A,A}
dxz{m<675:R,R}
hgx{m<3378:R,x<1215:R,A}
kzn{x<3718:fxt,x>3812:A,a<649:nzc,A}
zgq{a>1606:R,m>3298:A,A}
sh{a>1766:ml,m>411:A,x>3272:ndh,ntx}
jmk{m>1801:dmh,a<2515:R,qtk}
qc{x>3775:R,a<254:R,A}
vz{a<1402:A,R}
kps{m<3310:dgt,txr}
chl{x<880:cdj,m>3584:mhr,grj}
hnt{m>2869:A,A}
vrq{m<391:A,s>728:A,x<3519:R,R}
xvg{a>799:A,x<882:hnt,xqq}
kfd{s<3625:R,s<3792:R,a>1104:R,R}
lgc{m<859:llr,R}
hlc{a>1087:A,a<562:R,R}
kfc{a<1396:A,s<1784:A,tsc}
cr{x<3091:R,R}
bdg{m>2790:rxn,A}
nfz{x<462:R,x<620:A,A}
tc{a<597:A,A}
sr{a>1117:dfg,a<915:lcl,mnl}
cn{m>3623:vs,x>327:stz,A}
qq{a<2978:hxd,a>3368:R,a<3205:gvn,dxd}
vj{m<1523:A,mcq}
tsc{x>688:A,A}
vsz{x>1670:R,m<3429:mdc,xn}
clt{x>3309:R,x<3040:R,A}
fxt{x<3470:R,a>608:R,a>547:R,R}
htx{x>2607:gvq,m<1444:htb,pj}
fjs{m<2300:A,m<2373:A,px}
nbb{a<878:A,R}
rrm{a<652:R,pvj}
dxn{a<400:R,A}
fhn{a>1534:zgq,m<3262:dgx,m>3663:R,nc}
gj{s<3492:A,m>2866:R,R}
lcl{a>848:qv,x<2916:zcp,kz}
rrz{m<1945:R,s>358:R,A}
sj{s<3166:njn,hf}
thf{s<1521:A,m>2938:dfk,a<1001:xk,bs}
lts{a<2459:R,m<2530:A,x<2496:A,R}
fsq{m<1600:mf,dmj}
dxg{s>2375:mls,cp}
qz{m<2151:lqj,x>537:dlv,x>300:fxr,fjs}
sf{s<541:hj,a>1380:bt,m<538:mfb,vv}
tdg{a<1031:A,R}
pft{x<2060:R,a<1308:R,s<2438:R,A}
rmd{x>2881:lk,qvg}
cfh{x<3792:R,R}
srf{a>2141:A,x<268:A,R}
qj{m<1485:R,s>2769:A,A}
qvx{s<3612:gj,bgk}
msz{m>1978:tlp,rxx}
pkm{a>1336:qzl,m<2346:sr,m>3445:rmd,pkh}
jrn{m<1804:R,m<2588:R,A}
nqs{s>1016:A,A}
rtx{m<1176:R,m<1507:bcn,a>292:vjm,zr}
lgp{s>1365:vn,s>1283:kks,jnd}
cl{m>3382:A,A}
jct{m<1542:R,s>897:A,m>1926:R,A}
gp{m<3394:R,s>1431:A,szf}
nf{a>545:A,a>415:A,R}
bx{m<1737:A,vh}
mdc{s<2717:R,x>1320:A,A}
gth{m<900:A,R}
jjj{s<668:A,m<3223:A,x>2117:R,A}
qqs{x>1370:R,x<634:A,s<3751:R,A}
cfd{m>1163:tt,m<540:jv,x<125:A,R}
hcl{m<2815:A,A}
fz{s>2594:tv,rtx}
zkv{m>688:R,m>414:R,m>222:A,A}
tk{a>654:A,A}
fb{a>1065:A,A}
cxl{a<593:A,a>657:R,m<880:A,R}
xn{m<3765:R,a>1121:A,A}
vdk{m>2574:R,s>477:st,rrz}
zs{a>2464:nl,qf}
xqq{s>1384:A,a<354:A,m>3046:A,R}
nzc{a<598:A,s<3148:R,R}
pct{s>2183:R,a<1518:R,A}
nl{s>3041:fvr,lv}
sk{s>3236:kfd,R}
lmr{m<2601:R,a>1422:A,m>3266:R,R}
zsj{s<2295:xf,s>3148:kx,m>1925:cqs,fz}
rv{x<3564:A,s>2553:A,R}
cqb{m>1544:A,m<1535:A,s>2351:A,R}
qnj{a<592:R,a<853:R,R}
gsc{a<1578:A,R}
dhz{m>953:R,vrq}
ffq{a>1434:R,a>1308:R,R}
zqv{x>2889:R,R}
pk{s>1393:hcl,m<2713:R,x<325:hlc,R}
mhl{s<1312:A,m>2356:R,A}
qhc{a>1046:A,m<2557:A,A}
vsv{a>830:R,R}
mcq{a>1556:A,s<3584:A,m<3077:R,A}
ss{s>785:A,s>309:R,a<991:A,tr}
xpb{m<1158:A,a>840:R,s<277:A,A}
gcr{s<3558:gs,R}
rg{a>3475:A,s>2442:R,R}
rcm{x<3644:ph,s>454:zd,a<918:hpx,gvj}
zb{x<3303:A,s>2217:R,x<3658:R,A}
kdp{x<362:tlr,gmc}
ktr{a>1904:jp,x<1408:pvc,s<2789:grh,lgc}
gxc{x>2599:A,m<2068:dhg,m<3120:vz,rzd}
hg{a>1032:hcr,x>2532:A,m>1001:R,vkn}
cqm{x>2686:A,s<2691:R,R}
txt{s>3799:A,x<2877:R,R}
rm{a<1221:rpj,s>1945:qd,rkt}
zk{m>3150:R,x<3068:A,A}
jsh{s>3499:R,R}
zx{s>2688:R,m>212:A,R}
bt{x>2795:R,s<912:klt,s>1027:dxz,rkv}
lfz{x>354:A,A}
qsq{x>3672:R,m<2539:A,A}
hth{s<894:A,a>1762:R,R}
sx{x<3576:clt,A}
xst{m<3436:A,R}
fx{s>3411:gtb,x<3262:zt,A}
kb{s<576:A,A}
stz{x<538:R,A}
cfl{a<288:R,A}
nx{s>3743:A,s>3424:lm,s>3354:vc,gz}
vc{m<2127:R,A}
kz{a<802:R,x>3343:R,s<3157:R,A}
cp{m<550:zz,s>1058:vzq,zsk}
ptn{a<330:xl,m>1216:rdl,s<1500:dzk,hnj}
qbn{m>1670:R,s<444:A,x<3665:R,R}
qv{a<882:dzl,m<1431:gth,a<900:vk,tn}
pd{x>1973:R,R}
fvr{s<3633:jxd,zzb}
hp{x<3528:R,a>1546:A,x>3734:A,R}
dxq{x>3246:jcs,zsj}
lqj{m>1939:xzk,R}
qjr{x>955:bnz,a>1343:hz,m<1178:dxg,qqq}
dmf{m>1992:A,a<1865:R,A}
rzd{s<2980:R,s<3176:A,R}
jn{a>2806:grb,a>2170:fts,a<1863:lf,hq}
lk{m>3740:clj,fx}
lh{s>3014:A,a<1066:A,x>3035:rf,lnp}
pdc{x<3382:R,s>2340:R,a<1441:A,pct}
hxd{m>3095:A,A}
qmn{s<1644:R,A}
xqj{s<3059:R,A}
mmj{x>2544:pbq,s>2822:rq,m>2713:ps,tc}
mq{a>2494:R,R}
pkh{s<3318:hql,x>2874:qvx,m<2884:drx,zf}
cc{m<2619:qbn,m>3237:ls,a>1363:R,gbz}
bs{m<2841:A,s>1819:A,A}
rq{a<611:R,a>685:R,R}
ffj{m>1170:mbv,xkx}
lmz{m<1255:A,s>1599:A,s<833:R,R}
mfj{m<3463:R,m>3773:R,x<1389:A,R}
ns{a<309:A,x>1942:R,A}
gx{x>485:R,x>184:A,a>2713:R,A}
xt{x>3687:pv,A}
bdr{m<3074:A,R}
lb{x<3626:A,A}
hcq{m<3054:kc,vg}
zhj{m<2308:R,s>657:A,A}
zjt{m<811:R,A}
kcd{x>3716:A,x<3658:A,R}
xjb{x<3023:nd,s<2914:bk,a>1026:pls,A}
pvj{s<3618:A,R}
njn{a<2025:A,A}
bzs{x<2498:ss,a>925:pcb,nr}
lpr{a>2156:A,a>1708:A,A}
qt{s<2992:R,A}
brc{a>1274:A,m<1235:A,A}
tj{a<1086:zlh,a>1462:hh,kq}
mp{s>3203:A,m<2433:R,sm}
fch{m<902:A,m>1042:R,R}
tt{s<3117:R,a<2593:A,m<1794:R,R}
mfb{s>899:A,R}
ls{a>1464:R,s>707:A,s<275:A,R}
hf{x<3413:R,s>3585:A,m>1596:A,R}
jxd{s>3256:jkv,m>3335:kd,ff}
gmc{a<826:A,R}
hmk{a>1154:A,A}
fjb{m<1554:R,s>3071:R,R}
qqq{m>1695:qz,m>1456:drj,kdp}
fg{m<1522:A,a>520:cqb,s>2397:fjb,A}
qg{a<2533:cjd,s>2230:R,a<3328:zj,R}
dgx{m<3008:R,R}
zcp{a>806:R,m<1282:nzg,A}
bf{m<1701:R,s<947:A,a<915:R,R}
vjm{s>2448:R,x<2795:R,A}
jvt{s<984:R,R}
nkt{m<465:A,R}
jcs{m<2095:ptn,a<511:dt,znn}
pz{a>1750:R,A}
sn{s<885:A,x<335:R,R}
dmj{m>3082:A,s>3831:A,dfc}
jcb{s>3713:A,nhc}
xx{x<1726:R,s<1933:R,A}
hpd{s>1881:A,m<1645:R,m>1662:pq,pn}
xp{x<3212:R,x<3735:R,m<3680:A,R}
fhg{x>1483:A,a>3298:R,A}
mx{m<2349:jn,rz}
qss{m>3082:R,s>205:A,R}
nb{a>633:R,R}
mv{m>674:A,A}
vk{x<2918:R,A}
bcn{a<407:R,s<2493:A,R}
pbq{m<2422:A,A}
dl{s>3818:R,a>1030:A,A}
dmh{a<2446:R,s<1865:A,x<1709:A,R}
ndf{x>3135:bvq,m<1374:sf,vch}
mbv{a>2892:jh,x<629:dmf,R}
cnp{s>1241:R,A}
fqg{s<3752:A,x>380:R,A}
kgq{x<654:R,m<3379:R,A}
ch{m>1843:A,m>1397:R,R}
gvq{m<2229:A,lxq}
gq{m>3374:xp,x>3269:A,a<2230:R,knn}
pvg{x<2553:kl,m>3879:A,jhj}
vdr{s>1460:A,A}
nk{x<497:tzn,bdr}
{x=1344,m=7,a=841,s=655}
{x=349,m=44,a=343,s=2649}
{x=746,m=22,a=1245,s=147}
{x=1293,m=341,a=231,s=38}
{x=1730,m=1036,a=212,s=309}
{x=14,m=1402,a=1521,s=1297}
{x=583,m=618,a=1081,s=831}
{x=2278,m=1047,a=857,s=1119}
{x=87,m=1659,a=175,s=376}
{x=149,m=524,a=1025,s=669}
{x=1208,m=709,a=494,s=1877}
{x=1791,m=1443,a=767,s=491}
{x=571,m=3666,a=675,s=613}
{x=1038,m=1625,a=418,s=240}
{x=1365,m=2734,a=385,s=867}
{x=2713,m=127,a=2637,s=428}
{x=714,m=976,a=2819,s=520}
{x=395,m=462,a=799,s=369}
{x=2421,m=2679,a=81,s=2634}
{x=542,m=1258,a=54,s=2221}
{x=1628,m=125,a=767,s=934}
{x=1329,m=58,a=1566,s=1925}
{x=37,m=230,a=489,s=2915}
{x=2842,m=1518,a=200,s=514}
{x=1144,m=55,a=2330,s=6}
{x=302,m=347,a=1906,s=2678}
{x=94,m=1910,a=1554,s=2994}
{x=2266,m=853,a=1224,s=468}
{x=58,m=36,a=1316,s=1623}
{x=42,m=690,a=742,s=3281}
{x=389,m=757,a=469,s=511}
{x=1402,m=136,a=1401,s=2003}
{x=911,m=1732,a=1039,s=2192}
{x=1468,m=1436,a=322,s=1027}
{x=363,m=1849,a=404,s=1642}
{x=2474,m=1690,a=1435,s=1554}
{x=1600,m=2719,a=441,s=208}
{x=229,m=587,a=355,s=307}
{x=668,m=1438,a=203,s=47}
{x=2002,m=576,a=650,s=2785}
{x=2040,m=735,a=517,s=2140}
{x=1586,m=337,a=924,s=528}
{x=971,m=641,a=79,s=138}
{x=2262,m=708,a=2570,s=630}
{x=159,m=1081,a=2184,s=109}
{x=1966,m=43,a=57,s=2215}
{x=2219,m=2151,a=609,s=614}
{x=897,m=212,a=2484,s=650}
{x=131,m=569,a=1297,s=606}
{x=1890,m=1920,a=757,s=417}
{x=2953,m=702,a=3238,s=1299}
{x=111,m=191,a=3139,s=361}
{x=99,m=149,a=18,s=281}
{x=232,m=170,a=942,s=2884}
{x=1998,m=423,a=684,s=37}
{x=2591,m=2,a=149,s=1553}
{x=1538,m=359,a=774,s=280}
{x=1062,m=243,a=38,s=1991}
{x=729,m=1491,a=169,s=810}
{x=304,m=3158,a=2124,s=1770}
{x=203,m=139,a=885,s=58}
{x=62,m=419,a=83,s=1739}
{x=1046,m=448,a=112,s=2881}
{x=133,m=897,a=658,s=2968}
{x=1150,m=1829,a=1683,s=2455}
{x=2215,m=1609,a=525,s=1292}
{x=7,m=820,a=300,s=72}
{x=159,m=2927,a=337,s=301}
{x=1237,m=470,a=1637,s=2072}
{x=1898,m=168,a=2929,s=775}
{x=216,m=2823,a=108,s=51}
{x=1508,m=803,a=63,s=62}
{x=930,m=90,a=220,s=187}
{x=1112,m=78,a=1668,s=725}
{x=570,m=1180,a=2015,s=1112}
{x=1943,m=378,a=2345,s=2763}
{x=2427,m=258,a=600,s=441}
{x=2317,m=708,a=1108,s=183}
{x=169,m=153,a=1666,s=1157}
{x=721,m=1581,a=1487,s=1527}
{x=321,m=3244,a=1751,s=67}
{x=1691,m=2264,a=86,s=46}
{x=1561,m=494,a=152,s=1832}
{x=383,m=2150,a=20,s=1507}
{x=311,m=1190,a=679,s=744}
{x=600,m=865,a=1200,s=445}
{x=2019,m=80,a=886,s=80}
{x=1031,m=1503,a=390,s=27}
{x=122,m=3010,a=947,s=2248}
{x=1075,m=2302,a=620,s=1920}
{x=390,m=653,a=837,s=415}
{x=46,m=1948,a=116,s=1161}
{x=1385,m=603,a=903,s=272}
{x=1320,m=169,a=393,s=165}
{x=1338,m=505,a=25,s=233}
{x=220,m=1431,a=216,s=1804}
{x=246,m=2975,a=1265,s=108}
{x=652,m=1410,a=1054,s=614}
{x=232,m=2082,a=2317,s=1503}
{x=1697,m=225,a=24,s=313}
{x=140,m=885,a=2597,s=1326}
{x=789,m=1925,a=228,s=518}
{x=456,m=902,a=81,s=1581}
{x=2241,m=2249,a=629,s=1443}
{x=30,m=289,a=909,s=542}
{x=455,m=33,a=547,s=396}
{x=629,m=471,a=1246,s=647}
{x=1,m=1178,a=33,s=320}
{x=358,m=1131,a=2958,s=773}
{x=21,m=449,a=1148,s=1841}
{x=1282,m=759,a=662,s=1436}
{x=1668,m=466,a=997,s=3275}
{x=150,m=3273,a=2261,s=1610}
{x=2334,m=1559,a=1846,s=1977}
{x=1388,m=321,a=1549,s=312}
{x=1936,m=84,a=2290,s=1447}
{x=877,m=1088,a=1209,s=286}
{x=905,m=1204,a=540,s=2556}
{x=505,m=1002,a=1827,s=1102}
{x=250,m=881,a=1345,s=1985}
{x=843,m=40,a=1618,s=1871}
{x=485,m=1375,a=598,s=67}
{x=40,m=1653,a=414,s=389}
{x=598,m=320,a=202,s=2110}
{x=1161,m=1336,a=1170,s=632}
{x=487,m=227,a=234,s=2130}
{x=157,m=654,a=1779,s=1091}
{x=372,m=1982,a=238,s=131}
{x=2305,m=1274,a=1266,s=2316}
{x=280,m=13,a=3000,s=2368}
{x=2114,m=3767,a=900,s=992}
{x=2981,m=1005,a=1574,s=735}
{x=2103,m=690,a=1271,s=2328}
{x=175,m=1216,a=152,s=215}
{x=39,m=1554,a=1293,s=3521}
{x=1504,m=1077,a=517,s=619}
{x=2679,m=770,a=2796,s=967}
{x=1,m=1854,a=853,s=8}
{x=1538,m=1407,a=873,s=1696}
{x=85,m=2806,a=1525,s=426}
{x=312,m=1626,a=471,s=81}
{x=1428,m=656,a=485,s=1373}
{x=204,m=430,a=2401,s=744}
{x=2908,m=333,a=1120,s=72}
{x=142,m=382,a=1228,s=12}
{x=1132,m=2874,a=290,s=1321}
{x=1048,m=1243,a=722,s=1280}
{x=1502,m=278,a=905,s=210}
{x=2785,m=676,a=423,s=2215}
{x=1081,m=211,a=334,s=803}
{x=910,m=20,a=621,s=378}
{x=48,m=1739,a=324,s=1457}
{x=567,m=905,a=1612,s=491}
{x=2625,m=1047,a=631,s=521}
{x=1877,m=1100,a=2296,s=994}
{x=610,m=369,a=781,s=126}
{x=2296,m=3098,a=759,s=627}
{x=2390,m=1107,a=699,s=408}
{x=187,m=2415,a=1346,s=493}
{x=972,m=73,a=724,s=928}
{x=1043,m=118,a=64,s=653}
{x=620,m=537,a=2541,s=150}
{x=918,m=160,a=53,s=230}
{x=313,m=655,a=2019,s=128}
{x=1373,m=615,a=1832,s=1137}
{x=191,m=1495,a=476,s=267}
{x=646,m=458,a=2324,s=26}
{x=58,m=157,a=2613,s=781}
{x=272,m=294,a=2026,s=1422}
{x=7,m=313,a=213,s=789}
{x=352,m=75,a=2648,s=437}
{x=193,m=1677,a=160,s=1863}
{x=1188,m=832,a=757,s=334}
{x=563,m=312,a=1435,s=20}
{x=940,m=558,a=954,s=557}
{x=567,m=899,a=829,s=2068}
{x=657,m=168,a=204,s=1320}
{x=2212,m=2918,a=461,s=428}
{x=149,m=898,a=6,s=981}
{x=363,m=1021,a=852,s=2766}
{x=18,m=131,a=290,s=534}
{x=1502,m=37,a=1440,s=579}
{x=87,m=86,a=495,s=1699}
{x=668,m=1952,a=742,s=902}
{x=300,m=1201,a=835,s=385}
{x=2798,m=206,a=1230,s=548}
{x=577,m=718,a=31,s=2703}
{x=33,m=1952,a=360,s=827}
{x=1320,m=2522,a=15,s=810}
{x=288,m=505,a=308,s=2551}
{x=1850,m=2090,a=3001,s=313}
{x=814,m=185,a=792,s=320}
{x=675,m=1278,a=3606,s=2682}
{x=85,m=120,a=2269,s=1983}
{x=86,m=159,a=1858,s=2377}
{x=2523,m=797,a=2783,s=1324}
{x=270,m=600,a=62,s=39}
{x=650,m=1989,a=1351,s=470}
{x=1533,m=297,a=3,s=2810}
{x=3115,m=1584,a=357,s=1250}""".splitlines()

if __name__ == "__main__":
    input = sample_input1
    input = full_input1

    print(solve1(input))
    print(solve2(input))
    # print(solve1(input))
    # print(solve2(input))

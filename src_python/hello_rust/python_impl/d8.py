import heapq
import itertools
import math
from typing import NamedTuple

from tqdm.auto import tqdm


def parse_input(input: list[str]) -> tuple[list, dict]:
    [turns, *rules] = input

    G = {}
    for line in rules:
        src, dst = line.split(" = ")
        dst_left, dst_right = [d.strip("()") for d in dst.split(", ")]
        G[src] = (dst_left, dst_right)

    turns = [0 if turn == "L" else 1 for turn in turns]
    return turns, dict(G)


def solve1(input: list[str]) -> str:
    turns, G = parse_input(input)

    now = "AAA"
    for i, turn in enumerate(itertools.cycle(turns), start=1):
        now = G[now][turn]
        if now == "ZZZ":
            break
    return str(i)


def solve2_a(input: list[str]) -> str:
    """Fully naieve. Too slow"""
    turns, G = parse_input(input)

    ghost_pos = [k for k in G if k.endswith("A")]
    for i, turn in tqdm(enumerate(itertools.cycle(turns), start=1)):
        ghost_pos = [G[now][turn] for now in ghost_pos]
        if all([now[-1] == "Z" for now in ghost_pos]):
            break
    return str(i)


class GhostZCycle(NamedTuple):
    z_time: int
    cycle_len: int


def solve2(input: list[str]) -> str:
    turns, G = parse_input(input)

    ghost_starts = [k for k in G if k.endswith("A")]
    z_cycles: list[GhostZCycle] = []
    for ghost_start in ghost_starts:
        seen = {}
        now = ghost_start

        for i, (way_id, way) in enumerate(itertools.cycle(enumerate(turns)), start=1):
            now = G[now][way]
            k = (now, way_id)
            if k in seen:
                # We entered a cycle
                break
            seen[k] = i

        cycle = list(seen.items())[seen[k] - 1 :]  # -1 since we started the time at 1
        zs = {(key, way_id): time for (key, way_id), time in cycle if key.endswith("Z")}

        assert len(zs) == 1  # There's only a single Z in each cycle, easy!
        _, first_z_time = zs.popitem()

        z_cycles.append(GhostZCycle(z_time=first_z_time, cycle_len=len(cycle)))

    # Turns out you can just do LCM (least common multiple) of all the cycle lengths...
    # https://www.reddit.com/r/adventofcode/comments/18df7px/2023_day_8_solutions/
    lcm_solution = math.lcm(*[c.cycle_len for c in z_cycles])
    return str(lcm_solution)

    # This solves it in 1H
    heapq.heapify(z_cycles)
    with tqdm(total=lcm_solution) as pbar:
        while True:
            cycle = heapq.heappop(z_cycles)
            pbar.update(cycle.z_time - pbar.n)
            heapq.heappush(
                z_cycles,
                GhostZCycle(
                    z_time=cycle.z_time + cycle.cycle_len,
                    cycle_len=cycle.cycle_len,
                ),
            )

            if min(z_cycles).z_time == max(z_cycles).z_time:
                break
    return str(z_cycles[0].z_time)


sample_input1 = [
    "RL",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]
sample_input1_1 = [
    "LLR",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]
sample_input2 = [
    "LR",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)",
]


full_input1 = full_input2 = [
    "LRRLLRLRRRLRRRLRRLRRRLRRLRRRLRRLRRRLRLRRRLRRRLRRRLRLRRLRRRLRRRLRRLRRLRRLRLLLRRRLRRRLRLRLRRLLRRRLRRLRRRLRLRRLRRRLRRRLLRLRLLRRRLRRRLLRRRLRRRLRRRLRRLRRRLLLRRRLRLLLRLRLRLLRLRLLLRRLRRLLRRLRRRLRRLRRLRLRRLLRRLRLRRLLLRRRLLRRRLLRLRLLRRRLRLLRRLRLRRLRLRRRLLRRRLLRRLRLRRLRRLLRLRLRRRLRLRRRR",
    "GLJ = (QQV, JTL)",
    "JSJ = (DKN, GQN)",
    "MGD = (BPL, LQC)",
    "VSK = (SPH, DDH)",
    "TSB = (MKP, TKX)",
    "HPD = (GKG, XMX)",
    "BLZ = (HGN, KRR)",
    "BMQ = (JXC, HFC)",
    "GDG = (BVJ, NBL)",
    "LST = (PVJ, DPR)",
    "QQQ = (RLV, SNJ)",
    "TMV = (XGV, KCL)",
    "NPZ = (JRD, NHL)",
    "DDH = (NDR, XPN)",
    "SFQ = (TKD, SQH)",
    "RNK = (TJN, NFX)",
    "FRS = (SCJ, FDV)",
    "RST = (BSQ, MHQ)",
    "DSM = (FRX, DMN)",
    "GBN = (VBL, XRK)",
    "GLH = (KNN, PKP)",
    "JRD = (LDP, RNH)",
    "SPV = (JNR, FRK)",
    "PMD = (FXP, BKL)",
    "MDV = (MGD, FHM)",
    "MGG = (KMN, QPL)",
    "FNX = (FKG, NLT)",
    "FPH = (QXS, PBR)",
    "DKP = (QFT, QQQ)",
    "XVH = (PVP, GBJ)",
    "SSP = (BHD, KRM)",
    "JVR = (RHB, LDJ)",
    "HCX = (RNK, LGT)",
    "LRX = (SFN, GXD)",
    "DXN = (NQX, KNL)",
    "GNT = (GHV, DKG)",
    "QVF = (NJN, FSN)",
    "QHQ = (FXN, PNP)",
    "CHX = (DHN, BQB)",
    "GQD = (TLQ, XXG)",
    "RMF = (RVF, KKR)",
    "JHN = (NRG, RCC)",
    "MBG = (XPV, MSB)",
    "XJN = (SQT, XXJ)",
    "JNR = (VTP, XSF)",
    "NXD = (DKP, MKJ)",
    "LSS = (KHS, BSV)",
    "SQH = (BLH, VCG)",
    "TLM = (DCG, BQL)",
    "HTG = (TLF, KRB)",
    "GGM = (KLV, PTG)",
    "PVJ = (BHR, TRH)",
    "PRP = (QLC, JPQ)",
    "CVC = (KVJ, FTM)",
    "RMH = (RPD, FFK)",
    "MRL = (KFK, LJK)",
    "VMG = (LSX, FPH)",
    "DKQ = (XSM, CXK)",
    "QBD = (BGB, GPS)",
    "RFV = (QCG, NJD)",
    "FDN = (QFL, DXN)",
    "RMV = (NCJ, PMZ)",
    "BCJ = (MDD, TMG)",
    "BMB = (GLH, MKK)",
    "DLQ = (JKX, VGS)",
    "NBL = (GFQ, PRQ)",
    "NVG = (SCS, JTS)",
    "CBX = (MXQ, QSM)",
    "HFJ = (NXX, VRX)",
    "FMQ = (KDV, HFJ)",
    "DSK = (BND, GFJ)",
    "TRM = (MMX, BTG)",
    "XKS = (GXD, SFN)",
    "LDJ = (TFQ, CJK)",
    "LFP = (TFS, LST)",
    "PQS = (PJR, SMD)",
    "MTA = (JPD, MVX)",
    "FMM = (GPC, BVB)",
    "NJD = (JMG, DPL)",
    "VQJ = (KRM, BHD)",
    "PXP = (BPB, JJK)",
    "JDM = (HHQ, JXD)",
    "BJK = (SRN, DRL)",
    "MRS = (RPT, SQF)",
    "RCC = (DRD, SPP)",
    "XPG = (XRK, VBL)",
    "JLR = (LJQ, XDP)",
    "KLV = (SKX, SKX)",
    "JBB = (LRB, RRT)",
    "NDP = (KMS, DDJ)",
    "XML = (TPD, VKQ)",
    "TPM = (PKJ, PGR)",
    "DGQ = (JFK, TMB)",
    "XTL = (MPK, CTL)",
    "VSH = (BNH, HJR)",
    "PVG = (SPV, KCS)",
    "CCQ = (LQB, VTK)",
    "PLS = (HPS, CVC)",
    "GMQ = (CTG, QHQ)",
    "PNP = (VSK, JCV)",
    "JPD = (KKV, FQP)",
    "PRL = (KRB, TLF)",
    "NMT = (HXL, NHV)",
    "DLP = (KXR, BXQ)",
    "NFG = (DSR, HNX)",
    "BPB = (BTM, MGR)",
    "JPL = (NMT, QMD)",
    "HJG = (XJD, HHX)",
    "BBK = (VVF, SBN)",
    "GQL = (XNX, CKR)",
    "BND = (SQB, KFG)",
    "VRF = (JKS, LGG)",
    "PXG = (QMD, NMT)",
    "FKG = (GBS, JLR)",
    "NCJ = (NFG, CQH)",
    "CVM = (LFD, NPZ)",
    "GQN = (SMM, PQH)",
    "LJQ = (LXQ, KVG)",
    "PFK = (HHQ, JXD)",
    "KLQ = (JNB, DKQ)",
    "QRP = (SCB, HCM)",
    "LRB = (RMD, KLN)",
    "XPP = (GMK, LKL)",
    "LFD = (NHL, JRD)",
    "TVK = (TMV, TJF)",
    "MQD = (HTG, PRL)",
    "MKJ = (QQQ, QFT)",
    "QLF = (CHX, XSR)",
    "MPP = (XMK, QFP)",
    "HQQ = (PCS, PDC)",
    "NXX = (BTN, KBJ)",
    "JBQ = (GGH, FJL)",
    "BGB = (JSF, MNP)",
    "BRD = (VMF, NTR)",
    "HCM = (RHX, KJG)",
    "NKP = (GHV, DKG)",
    "XJK = (TRS, DGQ)",
    "GPS = (MNP, JSF)",
    "NCM = (VMJ, CSC)",
    "LSX = (PBR, QXS)",
    "VLF = (MTL, GVK)",
    "XFT = (XGS, CRL)",
    "HLR = (FMM, QLH)",
    "FFR = (XXX, BGX)",
    "MRB = (XJD, HHX)",
    "TVS = (MTL, GVK)",
    "KNL = (KDN, HQQ)",
    "PNV = (SQF, RPT)",
    "HVB = (BBB, LLG)",
    "RGX = (RLK, MSX)",
    "MKB = (HNP, NGM)",
    "FKL = (XMK, QFP)",
    "LXQ = (GNB, TQH)",
    "CQF = (NGF, NQF)",
    "BSV = (KFX, HNH)",
    "SVQ = (PXP, XQM)",
    "BHD = (XVH, GDN)",
    "QQB = (PCB, PCB)",
    "DCG = (GRH, RGX)",
    "RRT = (KLN, RMD)",
    "KDN = (PDC, PCS)",
    "RHJ = (VTK, LQB)",
    "LVR = (VSH, QGS)",
    "NHT = (LQS, DMB)",
    "PBR = (TCF, JCC)",
    "GBJ = (MLT, XNB)",
    "BJB = (XPR, MBG)",
    "PQH = (MCH, LMB)",
    "MPM = (BSV, KHS)",
    "SGB = (TKF, PMD)",
    "XQM = (JJK, BPB)",
    "TLQ = (FGM, CRC)",
    "FXP = (BCJ, TDR)",
    "VDG = (VMJ, CSC)",
    "XGV = (LHS, LTS)",
    "JKP = (PXG, JPL)",
    "KFQ = (TSB, RNB)",
    "NHL = (LDP, RNH)",
    "TRS = (JFK, TMB)",
    "PMM = (RHC, KMQ)",
    "QMB = (PPJ, CNG)",
    "MKH = (DDJ, KMS)",
    "NCG = (XXX, BGX)",
    "DBG = (SND, HMN)",
    "GVK = (TQD, JHN)",
    "KKM = (KKL, PBT)",
    "HLP = (JPQ, QLC)",
    "GPH = (JKG, DKK)",
    "XQP = (GLH, MKK)",
    "HRF = (BGB, GPS)",
    "BXQ = (BDH, GQT)",
    "NDR = (KKM, LRR)",
    "HQR = (RGL, RMX)",
    "PCS = (DTB, LDS)",
    "LQB = (GMQ, HRQ)",
    "KKR = (KTV, CMB)",
    "NGM = (KFQ, BQJ)",
    "KLN = (XFT, JRL)",
    "HRR = (RHJ, CCQ)",
    "XSF = (CKX, PLS)",
    "BTG = (GDG, JDS)",
    "PBT = (NVG, DVP)",
    "CPP = (VSH, QGS)",
    "MLN = (VGS, JKX)",
    "JRF = (SKN, RMF)",
    "KHS = (KFX, HNH)",
    "DDP = (QJG, XKJ)",
    "FGM = (TVK, TNS)",
    "QJH = (XSL, QXP)",
    "TNX = (NBV, KLQ)",
    "JVC = (FBR, PFT)",
    "XPV = (TLM, PPK)",
    "PCK = (KBG, TGJ)",
    "HRS = (VKM, JVF)",
    "DKK = (NHT, ZZZ)",
    "TJN = (KTL, QLF)",
    "THT = (JJQ, LRJ)",
    "JNB = (CXK, XSM)",
    "CRL = (VXT, TBG)",
    "RVF = (CMB, KTV)",
    "GQT = (PBB, CVM)",
    "QGF = (MGT, SKV)",
    "SCJ = (CQF, KRQ)",
    "SCM = (DPB, PMM)",
    "KNN = (XLQ, VPB)",
    "PPK = (BQL, DCG)",
    "LPP = (HJG, MRB)",
    "RRM = (RXT, PBZ)",
    "DCT = (FTF, HVB)",
    "PQP = (PBQ, HVR)",
    "NTV = (SCM, GKN)",
    "XXX = (LSS, MPM)",
    "BKP = (LXL, LXL)",
    "BLH = (QLV, SFJ)",
    "SPH = (NDR, XPN)",
    "CVF = (KDV, HFJ)",
    "XDK = (RHJ, CCQ)",
    "NQQ = (NTT, FVL)",
    "TQF = (XCV, NDX)",
    "VRX = (BTN, KBJ)",
    "KFX = (XLN, FDN)",
    "DMN = (TPT, JRQ)",
    "VVF = (TPQ, CDH)",
    "XPN = (LRR, KKM)",
    "LQC = (TMX, LHQ)",
    "XXT = (TLR, DDP)",
    "PBB = (LFD, LFD)",
    "GKF = (CHM, XTL)",
    "SNJ = (NSR, KVD)",
    "FKS = (PPL, PSM)",
    "BJZ = (MVX, JPD)",
    "JSF = (GQD, GQP)",
    "BFM = (QXR, MVF)",
    "QSD = (JHV, JKP)",
    "XSR = (DHN, BQB)",
    "SVM = (PKJ, PGR)",
    "XXJ = (HGF, MPG)",
    "KRB = (QMB, VNX)",
    "XJD = (SFQ, SGF)",
    "HGN = (KBF, LXS)",
    "TKF = (FXP, BKL)",
    "KHB = (TPJ, CGD)",
    "JFK = (JJX, DMH)",
    "PMT = (HGC, HJQ)",
    "NBV = (DKQ, JNB)",
    "FMN = (BJB, HSV)",
    "HPS = (KVJ, KVJ)",
    "GLT = (LXL, NFN)",
    "PSM = (PMT, CKP)",
    "RSM = (JRF, PDB)",
    "KVD = (PFK, JDM)",
    "CSQ = (HJG, MRB)",
    "PKJ = (HDR, TJQ)",
    "LRJ = (JSJ, BFS)",
    "KFG = (KKT, CQR)",
    "TPD = (THT, KBB)",
    "KBB = (LRJ, JJQ)",
    "XGS = (VXT, TBG)",
    "RHX = (XJK, QND)",
    "QPL = (DDN, STH)",
    "BQB = (XJC, SBH)",
    "KCL = (LHS, LTS)",
    "XPH = (KXR, BXQ)",
    "QNA = (NHL, JRD)",
    "KVJ = (KHJ, KHJ)",
    "QJP = (RNK, LGT)",
    "QFL = (KNL, NQX)",
    "KFP = (HLR, LCV)",
    "QLV = (PMX, BJK)",
    "TLR = (QJG, XKJ)",
    "NLQ = (XML, BDS)",
    "JXD = (MQD, GBH)",
    "LXP = (HRR, XDK)",
    "DJS = (GLJ, RNF)",
    "FLS = (FMB, MRL)",
    "HXL = (BXS, FDM)",
    "NQX = (KDN, HQQ)",
    "PGR = (TJQ, HDR)",
    "CGD = (DGS, VKN)",
    "KRQ = (NQF, NGF)",
    "JSB = (PNQ, DHV)",
    "MBJ = (JCK, QRP)",
    "MXQ = (DRG, DSM)",
    "HMN = (CBP, CPG)",
    "JTL = (RST, SPD)",
    "DKG = (GQK, XMQ)",
    "NJN = (TVS, VLF)",
    "LTS = (JCB, TQF)",
    "XNP = (JVF, VKM)",
    "RTG = (XXJ, SQT)",
    "KNT = (LRB, RRT)",
    "SFL = (LXP, CDN)",
    "GXD = (MMT, CNX)",
    "SMC = (XTL, CHM)",
    "JCB = (XCV, NDX)",
    "DQT = (RBJ, QGF)",
    "TFR = (MKH, NDP)",
    "HTP = (CSQ, LPP)",
    "JKM = (VVK, SHX)",
    "LGG = (RPH, NTV)",
    "NSR = (JDM, PFK)",
    "QFT = (SNJ, RLV)",
    "SQF = (GRG, RSX)",
    "SFD = (FFK, RPD)",
    "SCD = (SNC, LGQ)",
    "CXK = (VDN, SQM)",
    "LDP = (NLQ, DGV)",
    "CDN = (XDK, HRR)",
    "HFC = (QBD, HRF)",
    "LGT = (NFX, TJN)",
    "VKM = (QJP, HCX)",
    "HGF = (SCD, TKT)",
    "VGS = (SGB, VXD)",
    "MGL = (FTN, LBF)",
    "FDM = (DLQ, MLN)",
    "FTP = (HJL, JQG)",
    "TCN = (MRL, FMB)",
    "NGR = (QPL, KMN)",
    "NDX = (DMX, LTG)",
    "GVJ = (JDG, PCK)",
    "MVF = (KVR, TQK)",
    "MXJ = (FPQ, VBV)",
    "RNH = (DGV, NLQ)",
    "RPD = (RFV, PGG)",
    "JKG = (NHT, NHT)",
    "XNX = (JDB, DQT)",
    "DRL = (GCM, DSK)",
    "TCF = (TCJ, SVQ)",
    "LCL = (NJN, FSN)",
    "MJM = (QSM, MXQ)",
    "JJK = (BTM, MGR)",
    "SPX = (JDG, PCK)",
    "QLC = (DHJ, PVG)",
    "GPC = (XKC, RTT)",
    "TJQ = (XPG, GBN)",
    "HSV = (XPR, MBG)",
    "JKS = (RPH, NTV)",
    "XDP = (KVG, LXQ)",
    "JDS = (NBL, BVJ)",
    "TQK = (NCR, HTP)",
    "BLX = (TFS, LST)",
    "KRR = (LXS, KBF)",
    "XMQ = (KHB, MMC)",
    "KBG = (DBG, MQR)",
    "LRR = (KKL, PBT)",
    "LFV = (HVQ, MNJ)",
    "HGD = (MNL, PDJ)",
    "GLB = (NDP, MKH)",
    "CMB = (VDG, NCM)",
    "TKD = (VCG, BLH)",
    "BQJ = (TSB, RNB)",
    "QBT = (MKB, RKM)",
    "GJQ = (BTG, MMX)",
    "SGF = (TKD, SQH)",
    "RMD = (JRL, XFT)",
    "DDJ = (HRS, XNP)",
    "HNP = (KFQ, BQJ)",
    "FQF = (MNJ, HVQ)",
    "PJT = (FRQ, KFP)",
    "RKM = (NGM, HNP)",
    "VBV = (LVR, CPP)",
    "RBJ = (SKV, MGT)",
    "MPG = (SCD, TKT)",
    "BHR = (BRM, FJC)",
    "VTP = (CKX, PLS)",
    "PBQ = (RQC, HGD)",
    "RMX = (FTP, NGJ)",
    "SMP = (KRR, HGN)",
    "KBF = (RMK, BMQ)",
    "LSL = (JSB, VPL)",
    "KRM = (GDN, XVH)",
    "DHJ = (SPV, KCS)",
    "XNB = (QFH, PGQ)",
    "TGJ = (DBG, MQR)",
    "LHQ = (FNX, KFF)",
    "GCM = (GFJ, BND)",
    "MJQ = (BBK, KVM)",
    "NQF = (SSP, VQJ)",
    "VPL = (DHV, PNQ)",
    "HHX = (SFQ, SGF)",
    "FJL = (MGL, XKH)",
    "HNH = (FDN, XLN)",
    "RLK = (LCL, QVF)",
    "SND = (CPG, CBP)",
    "CNG = (DJS, HVS)",
    "VDN = (QBK, MXJ)",
    "BRM = (SMC, GKF)",
    "VTK = (HRQ, GMQ)",
    "MVX = (KKV, FQP)",
    "TDR = (TMG, MDD)",
    "SQT = (HGF, MPG)",
    "TMN = (HVB, FTF)",
    "GNB = (BFT, QXK)",
    "QXP = (MJM, CBX)",
    "GQK = (MMC, KHB)",
    "QGX = (NDB, QSD)",
    "TMX = (FNX, KFF)",
    "BLD = (NBV, KLQ)",
    "RHC = (NXK, PJT)",
    "XJC = (QKG, QKG)",
    "GBH = (HTG, PRL)",
    "TPT = (TRQ, XXT)",
    "FTF = (BBB, LLG)",
    "QJG = (FKS, PQG)",
    "FVR = (LXP, CDN)",
    "XCA = (FVR, SFL)",
    "VMJ = (KHP, MDV)",
    "NTT = (LFP, BLX)",
    "DMB = (TCN, FLS)",
    "CQR = (LRX, XKS)",
    "JFR = (TMN, DCT)",
    "TRQ = (DDP, TLR)",
    "BXS = (MLN, DLQ)",
    "LLG = (LSK, XMD)",
    "CBP = (RHF, BRD)",
    "PFT = (SMP, BLZ)",
    "TNS = (TMV, TJF)",
    "DHV = (VFX, VVR)",
    "PPL = (CKP, PMT)",
    "QND = (DGQ, TRS)",
    "VBL = (MGG, NGR)",
    "FHM = (BPL, LQC)",
    "KKT = (LRX, XKS)",
    "LHS = (JCB, TQF)",
    "LXL = (LJH, LJH)",
    "BLT = (GGH, FJL)",
    "JQG = (XCT, FRS)",
    "KCS = (JNR, FRK)",
    "SKX = (JKG, JKG)",
    "VKN = (NMS, QBT)",
    "DSL = (FMN, PJN)",
    "TPJ = (VKN, DGS)",
    "CKR = (JDB, DQT)",
    "LKL = (QLQ, NXD)",
    "SMM = (LMB, MCH)",
    "FSN = (TVS, VLF)",
    "KMS = (XNP, HRS)",
    "MTX = (LGG, JKS)",
    "CHM = (CTL, MPK)",
    "HRQ = (QHQ, CTG)",
    "QCG = (JMG, DPL)",
    "TQH = (QXK, BFT)",
    "JXC = (QBD, HRF)",
    "JVF = (QJP, HCX)",
    "TJF = (KCL, XGV)",
    "XDS = (QQB, QQB)",
    "KJG = (QND, XJK)",
    "CTG = (FXN, PNP)",
    "BBB = (LSK, XMD)",
    "DMH = (NHF, JKM)",
    "BGX = (LSS, MPM)",
    "RHF = (VMF, NTR)",
    "KHJ = (JPD, MVX)",
    "SCS = (FNJ, RSM)",
    "VFX = (LXV, XPP)",
    "XLQ = (RMH, SFD)",
    "HDB = (HVR, PBQ)",
    "PTG = (SKX, GPH)",
    "NTR = (LDG, LKV)",
    "KKL = (NVG, DVP)",
    "XKH = (FTN, LBF)",
    "BDS = (TPD, VKQ)",
    "QKG = (FBR, FBR)",
    "LDS = (HQR, BJC)",
    "KKV = (MPP, FKL)",
    "JRQ = (TRQ, XXT)",
    "MNP = (GQP, GQD)",
    "BTM = (GJQ, TRM)",
    "RPH = (GKN, SCM)",
    "TQD = (RCC, NRG)",
    "FQP = (FKL, MPP)",
    "VFV = (QQB, HPB)",
    "XSL = (CBX, MJM)",
    "GKN = (DPB, PMM)",
    "PBK = (QBH, GQL)",
    "HPB = (PCB, RRM)",
    "MCH = (RTG, XJN)",
    "KSL = (FVL, NTT)",
    "TCJ = (PXP, XQM)",
    "RNF = (JTL, QQV)",
    "BXA = (NFG, CQH)",
    "KVK = (PRP, HLP)",
    "NGF = (SSP, VQJ)",
    "PJN = (BJB, HSV)",
    "SFJ = (BJK, PMX)",
    "CPL = (LDJ, RHB)",
    "MKP = (TRJ, BFM)",
    "RPT = (GRG, RSX)",
    "PRQ = (XPH, DLP)",
    "DSR = (KNT, JBB)",
    "VPB = (RMH, SFD)",
    "QLQ = (MKJ, DKP)",
    "FNJ = (PDB, JRF)",
    "SBH = (QKG, JVC)",
    "PDC = (LDS, DTB)",
    "QFP = (MJQ, HFK)",
    "CTL = (RDD, KVK)",
    "LXS = (BMQ, RMK)",
    "VKF = (QBH, GQL)",
    "HJL = (XCT, FRS)",
    "KTK = (LDF, HPD)",
    "RMK = (HFC, JXC)",
    "MGT = (JFR, HXB)",
    "XLN = (QFL, DXN)",
    "FRQ = (HLR, LCV)",
    "FMB = (KFK, LJK)",
    "NFX = (KTL, QLF)",
    "LMB = (RTG, XJN)",
    "JDG = (TGJ, KBG)",
    "MNJ = (GVJ, SPX)",
    "VMF = (LDG, LKV)",
    "SRN = (GCM, DSK)",
    "JCC = (SVQ, TCJ)",
    "NGJ = (HJL, JQG)",
    "XCT = (SCJ, FDV)",
    "FFK = (RFV, PGG)",
    "NFN = (LJH, RMV)",
    "GHV = (GQK, XMQ)",
    "HFK = (KVM, BBK)",
    "MNL = (GLB, TFR)",
    "BPL = (LHQ, TMX)",
    "LJH = (NCJ, NCJ)",
    "FDV = (CQF, KRQ)",
    "PBZ = (SFL, FVR)",
    "MSB = (PPK, TLM)",
    "GGH = (XKH, MGL)",
    "MPK = (KVK, RDD)",
    "VVR = (XPP, LXV)",
    "NMS = (MKB, RKM)",
    "NXK = (FRQ, KFP)",
    "BSQ = (JCS, MBJ)",
    "XMX = (DSL, CTX)",
    "NHF = (VVK, SHX)",
    "MMC = (CGD, TPJ)",
    "GQP = (TLQ, XXG)",
    "TRH = (FJC, BRM)",
    "RLV = (NSR, KVD)",
    "DKN = (PQH, SMM)",
    "MSX = (LCL, QVF)",
    "SKN = (KKR, RVF)",
    "LSK = (PNV, MRS)",
    "RDD = (PRP, HLP)",
    "DRD = (JBQ, BLT)",
    "GBS = (XDP, LJQ)",
    "TFQ = (BLD, TNX)",
    "QGS = (BNH, HJR)",
    "LJK = (CVF, FMQ)",
    "NCR = (CSQ, LPP)",
    "HJQ = (SVM, TPM)",
    "JCS = (QRP, JCK)",
    "KTV = (VDG, NCM)",
    "MMX = (GDG, JDS)",
    "HVS = (GLJ, RNF)",
    "XMD = (PNV, MRS)",
    "VVK = (XDS, VFV)",
    "FBR = (SMP, SMP)",
    "XKJ = (PQG, FKS)",
    "AAA = (LQS, DMB)",
    "LCV = (FMM, QLH)",
    "PPJ = (HVS, DJS)",
    "DGS = (QBT, NMS)",
    "PFG = (LDF, HPD)",
    "HVR = (RQC, HGD)",
    "QXK = (BMB, XQP)",
    "BTN = (GHD, JXP)",
    "DPR = (TRH, BHR)",
    "KVG = (GNB, TQH)",
    "GFJ = (KFG, SQB)",
    "JCK = (SCB, HCM)",
    "QSM = (DRG, DSM)",
    "XPR = (XPV, MSB)",
    "RNB = (TKX, MKP)",
    "RHB = (TFQ, CJK)",
    "PGQ = (VRF, MTX)",
    "CDH = (GNT, NKP)",
    "BVJ = (PRQ, GFQ)",
    "LTG = (QGX, LVL)",
    "XJR = (QXP, XSL)",
    "JCV = (SPH, DDH)",
    "GDN = (PVP, GBJ)",
    "HNX = (KNT, JBB)",
    "SFN = (MMT, CNX)",
    "RGL = (FTP, NGJ)",
    "VCA = (KRR, HGN)",
    "ZZZ = (DMB, LQS)",
    "GMK = (QLQ, NXD)",
    "LKV = (VMG, SDQ)",
    "PMZ = (CQH, NFG)",
    "KBJ = (GHD, JXP)",
    "PNQ = (VFX, VVR)",
    "TPQ = (GNT, NKP)",
    "SPD = (MHQ, BSQ)",
    "XCV = (DMX, LTG)",
    "BVB = (XKC, RTT)",
    "BQL = (RGX, GRH)",
    "JTS = (RSM, FNJ)",
    "SPP = (BLT, JBQ)",
    "VXT = (CPL, JVR)",
    "MTL = (JHN, TQD)",
    "KMN = (DDN, STH)",
    "RQC = (PDJ, MNL)",
    "FTM = (KHJ, BJZ)",
    "RXT = (FVR, SFL)",
    "QXR = (KVR, TQK)",
    "HJR = (QJH, XJR)",
    "BFS = (GQN, DKN)",
    "TKX = (BFM, TRJ)",
    "DGV = (BDS, XML)",
    "DRG = (FRX, DMN)",
    "VNX = (CNG, PPJ)",
    "CSC = (MDV, KHP)",
    "KMQ = (PJT, NXK)",
    "DVP = (SCS, JTS)",
    "LDF = (XMX, GKG)",
    "QFH = (MTX, VRF)",
    "RTT = (PQS, GBD)",
    "KXR = (BDH, BDH)",
    "SMD = (GHT, GGM)",
    "TMB = (DMH, JJX)",
    "KHP = (FHM, MGD)",
    "TLF = (QMB, VNX)",
    "FRK = (VTP, XSF)",
    "KTL = (CHX, XSR)",
    "GRH = (RLK, MSX)",
    "QMD = (NHV, HXL)",
    "KDV = (VRX, NXX)",
    "LGQ = (VKF, PBK)",
    "FVL = (BLX, LFP)",
    "MMT = (NQQ, KSL)",
    "CKP = (HJQ, HGC)",
    "STH = (BKP, GLT)",
    "QBK = (FPQ, VBV)",
    "CTX = (FMN, PJN)",
    "HHQ = (GBH, MQD)",
    "JHV = (PXG, JPL)",
    "FJC = (GKF, SMC)",
    "TMG = (PFG, KTK)",
    "XXG = (CRC, FGM)",
    "BDH = (PBB, PBB)",
    "FPQ = (CPP, LVR)",
    "BKL = (BCJ, TDR)",
    "GKG = (DSL, CTX)",
    "LVL = (NDB, QSD)",
    "BNH = (QJH, XJR)",
    "TBG = (JVR, CPL)",
    "CQH = (HNX, DSR)",
    "VXD = (TKF, PMD)",
    "MGR = (TRM, GJQ)",
    "PDJ = (GLB, TFR)",
    "HXB = (DCT, TMN)",
    "XSM = (SQM, VDN)",
    "HDR = (XPG, GBN)",
    "GFQ = (XPH, DLP)",
    "XKC = (PQS, GBD)",
    "SBN = (TPQ, CDH)",
    "RSX = (LFV, FQF)",
    "PVP = (XNB, MLT)",
    "LDG = (VMG, SDQ)",
    "LXV = (LKL, GMK)",
    "TKT = (SNC, LGQ)",
    "SHX = (XDS, VFV)",
    "GRG = (FQF, LFV)",
    "QQV = (RST, SPD)",
    "CNX = (NQQ, KSL)",
    "DMX = (LVL, QGX)",
    "CRC = (TVK, TNS)",
    "JXP = (FFR, NCG)",
    "BJC = (RGL, RMX)",
    "BFT = (XQP, BMB)",
    "SKV = (JFR, HXB)",
    "JDB = (QGF, RBJ)",
    "XRK = (NGR, MGG)",
    "FXN = (JCV, VSK)",
    "JJQ = (JSJ, BFS)",
    "DDN = (BKP, GLT)",
    "QBH = (XNX, CKR)",
    "MLT = (PGQ, QFH)",
    "SNC = (VKF, PBK)",
    "FTN = (HDB, PQP)",
    "DPL = (LSL, FXH)",
    "TFS = (DPR, PVJ)",
    "HVQ = (SPX, GVJ)",
    "JJX = (NHF, JKM)",
    "KVR = (HTP, NCR)",
    "MQR = (SND, HMN)",
    "MDD = (PFG, KTK)",
    "PCB = (RXT, RXT)",
    "NLT = (GBS, JLR)",
    "GBD = (SMD, PJR)",
    "NHV = (BXS, FDM)",
    "GHT = (KLV, PTG)",
    "SDQ = (LSX, FPH)",
    "TRJ = (QXR, MVF)",
    "HGC = (TPM, SVM)",
    "MHQ = (JCS, MBJ)",
    "CKX = (HPS, HPS)",
    "SQM = (MXJ, QBK)",
    "PQG = (PPL, PSM)",
    "JRL = (CRL, XGS)",
    "NRG = (DRD, SPP)",
    "GHD = (NCG, FFR)",
    "LBF = (PQP, HDB)",
    "MKK = (KNN, PKP)",
    "CPG = (RHF, BRD)",
    "SQB = (KKT, CQR)",
    "VKQ = (THT, KBB)",
    "KFK = (FMQ, CVF)",
    "PJR = (GHT, GGM)",
    "FXH = (JSB, VPL)",
    "JPQ = (PVG, DHJ)",
    "PDB = (SKN, RMF)",
    "JKX = (VXD, SGB)",
    "DTB = (HQR, BJC)",
    "VCG = (QLV, SFJ)",
    "KVM = (SBN, VVF)",
    "QXS = (TCF, JCC)",
    "CJK = (BLD, TNX)",
    "PKP = (VPB, XLQ)",
    "JMG = (LSL, FXH)",
    "FRX = (JRQ, TPT)",
    "KFF = (FKG, NLT)",
    "DPB = (RHC, KMQ)",
    "SCB = (KJG, RHX)",
    "DHN = (XJC, SBH)",
    "QLH = (GPC, BVB)",
    "PMX = (DRL, SRN)",
    "XMK = (HFK, MJQ)",
    "NDB = (JHV, JKP)",
    "LQS = (TCN, FLS)",
    "PGG = (NJD, QCG)",
]

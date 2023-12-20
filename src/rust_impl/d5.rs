use core::ops::Range;
use std::collections::HashMap;

pub struct RangeMapping {
    range_map: HashMap<Range<i64>, Range<i64>>,
}
impl RangeMapping {
    pub fn new() -> RangeMapping {
        RangeMapping {
            range_map: HashMap::new(),
        }
    }

    pub fn get_at(&self, key: i64) -> i64 {
        for (src, dst) in &self.range_map {
            if src.contains(&&key) {
                return dst.start + (key - src.start);
            }
        }
        key
    }

    pub fn insert(&mut self, src: Range<i64>, dst: Range<i64>) {
        self.range_map.insert(src, dst);
    }
}

pub fn parse_input(input: Vec<String>) -> (Vec<i64>, Vec<RangeMapping>) {
    let seeds = input[0]
        .split_ascii_whitespace()
        .skip(1)
        .map(|nums| nums.parse::<i64>().unwrap())
        .collect::<Vec<i64>>();

    let mut mappings = Vec::new();

    for line in input.iter().skip(1) {
        if line.chars().next().unwrap().is_alphabetic() {
            mappings.push(RangeMapping::new());
        } else {
            if let [dst_start, src_start, span] = line
                .split_ascii_whitespace()
                .map(|c| c.parse::<i64>().unwrap())
                .collect::<Vec<i64>>()[..]
            {
                let mut last_mapping = mappings.pop().unwrap();
                last_mapping.insert(src_start..(src_start + span), dst_start..(dst_start + span));
                mappings.push(last_mapping);
            } else {
                unreachable!();
            };
        }
    }
    (seeds, mappings)
}

pub fn solve1(input: Vec<String>) -> String {
    let (seeds, mappings) = parse_input(input);

    let mut out = Vec::new();
    for value in seeds {
        let mut value = value;
        for mapping in &mappings {
            value = mapping.get_at(value);
        }
        out.push(value);
    }

    out.iter()
        .reduce(|a, b| if a < b { a } else { b })
        .unwrap()
        .to_string()
}

pub fn solve2(input: Vec<String>) -> String {
    let (seeds, mut mappings) = parse_input(input);

    let (even, odd): (Vec<_>, Vec<_>) = seeds.iter().enumerate().partition(|(i, e)| i % 2 == 0);
    let seed_spans = std::iter::zip(even, odd)
        .map(|((_, l), (_, r))| (l.clone(), l + r))
        .collect::<Vec<_>>();
    let seed_ranges = seed_spans.iter().map(|(l, r)| l..r).collect::<Vec<_>>();

    let mut rev_mappings = Vec::new();
    for mapping in mappings {
        rev_mappings.push(RangeMapping {
            range_map: HashMap::from_iter(
                mapping
                    .range_map
                    .iter()
                    .map(|(k, v)| (v.clone(), k.clone())),
            ),
        })
    }
    rev_mappings.reverse();

    let max_value = *seed_ranges.iter().map(|r| r.end).max().unwrap();

    // dbg!(max_value);
    for orig_value in 1..max_value {
        let mut value = orig_value;
        let mut debug = Vec::new();
        for mapping in &rev_mappings {
            value = mapping.get_at(value);
            debug.push(value);
        }
        // dbg!(debug);
        if seed_ranges.iter().any(|span| span.contains(&&value)) {
            return orig_value.to_string();
        }
    }
    unreachable!()
}

pub fn sample_input1() -> Vec<String> {
    vec![
        "seeds: 79 14 55 13".to_string(),
        "seed-to-soil map:".to_string(),
        "50 98 2".to_string(),
        "52 50 48".to_string(),
        "soil-to-fertilizer map:".to_string(),
        "0 15 37".to_string(),
        "37 52 2".to_string(),
        "39 0 15".to_string(),
        "fertilizer-to-water map:".to_string(),
        "49 53 8".to_string(),
        "0 11 42".to_string(),
        "42 0 7".to_string(),
        "57 7 4".to_string(),
        "water-to-light map:".to_string(),
        "88 18 7".to_string(),
        "18 25 70".to_string(),
        "light-to-temperature map:".to_string(),
        "45 77 23".to_string(),
        "81 45 19".to_string(),
        "68 64 13".to_string(),
        "temperature-to-humidity map:".to_string(),
        "0 69 1".to_string(),
        "1 0 69".to_string(),
        "humidity-to-location map:".to_string(),
        "60 56 37".to_string(),
        "56 93 4".to_string(),
    ]
}

pub fn sample_input2() -> Vec<String> {
    sample_input1()
}
pub fn full_input1() -> Vec<String> {
    full_input2()
}

pub fn full_input2() -> Vec<String> {
    vec![
        "seeds: 104847962 3583832 1212568077 114894281 3890048781 333451605 1520059863 217361990 310308287 12785610 3492562455 292968049 1901414562 516150861 2474299950 152867148 3394639029 59690410 862612782 176128197".to_string(),
        "seed-to-soil map:".to_string(),
        "2023441036 2044296880 396074363".to_string(),
        "2419515399 3839972576 454994720".to_string(),
        "274688417 699823315 258919718".to_string(),
        "533608135 0 431744151".to_string(),
        "965352286 431744151 161125324".to_string(),
        "3391658630 2936663910 903308666".to_string(),
        "200749950 1177785526 73938467".to_string(),
        "2874510119 1440389999 315892137".to_string(),
        "1916089471 2440371243 20593195".to_string(),
        "0 977035576 200749950".to_string(),
        "1936682666 1957538510 86758370".to_string(),
        "1440389999 2902130623 34533287".to_string(),
        "1126477610 592869475 106953840".to_string(),
        "3190402256 1756282136 201256374".to_string(),
        "1474923286 2460964438 441166185".to_string(),
        "1233431450 958743033 18292543".to_string(),
        "soil-to-fertilizer map:".to_string(),
        "1479837493 1486696129 480988794".to_string(),
        "3637384566 3730606485 267472485".to_string(),
        "70483107 174821741 921411492".to_string(),
        "3586173142 3071290434 51211424".to_string(),
        "1960826287 1166716340 319979789".to_string(),
        "3952751562 3398939385 283772589".to_string(),
        "0 1096233233 70483107".to_string(),
        "1166716340 1967684923 313121153".to_string(),
        "3904857051 3682711974 47894511".to_string(),
        "2902018973 3122501858 276437527".to_string(),
        "991894599 0 174821741".to_string(),
        "3416901681 2902018973 169271461".to_string(),
        "3178456500 3998078970 238445181".to_string(),
        "fertilizer-to-water map:".to_string(),
        "4274676882 2765984054 20290414".to_string(),
        "3642266392 2324011621 382224743".to_string(),
        "3159410287 4157769177 137198119".to_string(),
        "3437898965 2786274468 204367427".to_string(),
        "2136710407 1497332580 94233249".to_string(),
        "4121681656 2706236364 59747690".to_string(),
        "2362529584 1912615374 411396247".to_string(),
        "4181429346 3961317447 93247536".to_string(),
        "270199336 152334204 473273308".to_string(),
        "1977000445 3853228854 108088593".to_string(),
        "2085089038 1304420652 51621369".to_string(),
        "1407624846 2990641895 345516575".to_string(),
        "908901118 638701782 307729932".to_string(),
        "3296608406 1356042021 141290559".to_string(),
        "743472644 625607512 13094270".to_string(),
        "2230943656 3721642926 131585928".to_string(),
        "0 946431714 270199336".to_string(),
        "2773925831 3336158470 385484456".to_string(),
        "4024491135 1815424853 97190521".to_string(),
        "756566914 0 152334204".to_string(),
        "1304420652 4054564983 103204194".to_string(),
        "1753141421 1591565829 223859024".to_string(),
        "water-to-light map:".to_string(),
        "139728365 0 27290780".to_string(),
        "4161521920 2345099742 65970280".to_string(),
        "3549264451 2411070022 15588060".to_string(),
        "846553766 4012820620 62155872".to_string(),
        "3276913175 3215861697 30588309".to_string(),
        "7256118 139495191 27523954".to_string(),
        "3653026602 3908255344 104565276".to_string(),
        "2007806695 3246450006 21131889".to_string(),
        "426542603 2677155019 292403006".to_string(),
        "3265259672 4167732422 11653503".to_string(),
        "2959802238 3267581895 77570040".to_string(),
        "2766290955 2562319792 114835227".to_string(),
        "779480399 3352881787 3460872".to_string(),
        "718945609 995514267 33385697".to_string(),
        "908709638 1675494216 164534584".to_string(),
        "1547970680 1643941067 31553149".to_string(),
        "1579523829 2009572806 335526936".to_string(),
        "782941271 2969558025 63612495".to_string(),
        "752331306 465171569 27149093".to_string(),
        "237284175 1454682639 189258428".to_string(),
        "3757591878 3724399189 59699158".to_string(),
        "2881126182 3784098347 78676056".to_string(),
        "1520219770 2426658082 27750910".to_string(),
        "3564852511 1366508548 88174091".to_string(),
        "2383999106 3681454004 42945185".to_string(),
        "4287237444 3345151935 7729852".to_string(),
        "2242562254 3649815914 31638090".to_string(),
        "3307501484 753751300 241762967".to_string(),
        "34780072 27290780 104948293".to_string(),
        "2028938584 3033170520 182691177".to_string(),
        "3037372278 237284175 227887394".to_string(),
        "3817291036 3356342659 5821939".to_string(),
        "0 132239073 7256118".to_string(),
        "1360895538 1266240382 51601463".to_string(),
        "3823112975 492320662 230498145".to_string(),
        "2274200344 1840028800 109798762".to_string(),
        "4053611120 2454408992 107910800".to_string(),
        "2426944291 1317841845 48666703".to_string(),
        "1073244222 3362164598 287651316".to_string(),
        "1457977942 1203998554 62241828".to_string(),
        "2591192365 1028899964 175098590".to_string(),
        "1412497001 3862774403 45480941".to_string(),
        "2475610994 4179385925 115581371".to_string(),
        "4227492200 1949827562 59745244".to_string(),
        "1915050765 4074976492 92755930".to_string(),
        "2211629761 722818807 30932493".to_string(),
        "light-to-temperature map:".to_string(),
        "3741602262 2758947303 142653736".to_string(),
        "628739598 2901601039 50811783".to_string(),
        "1842260329 1084521599 145122645".to_string(),
        "2990409993 3493390513 390865485".to_string(),
        "4190333929 4159289690 83510514".to_string(),
        "984282519 2952412822 202948629".to_string(),
        "1826968660 3155361451 15291669".to_string(),
        "1329953386 2288178120 328046945".to_string(),
        "830513455 3304469747 74190775".to_string(),
        "1187231148 2616225065 142722238".to_string(),
        "2705943734 836690664 247830935".to_string(),
        "3381275478 1332397059 281233458".to_string(),
        "679551381 605080109 150962074".to_string(),
        "1987382974 756042183 44013157".to_string(),
        "4159289690 4263923057 31044239".to_string(),
        "1772730322 3250231409 54238338".to_string(),
        "2549609472 2131843858 156334262".to_string(),
        "1658000331 3378660522 114729991".to_string(),
        "298584178 195831363 330155420".to_string(),
        "3662508936 525986783 79093326".to_string(),
        "4273844443 4242800204 21122853".to_string(),
        "2953774669 800055340 36635324".to_string(),
        "2031396131 1613630517 518213341".to_string(),
        "265644560 162891745 32939618".to_string(),
        "162891745 1229644244 102752815".to_string(),
        "904704230 3170653120 79578289".to_string(),
        "temperature-to-humidity map:".to_string(),
        "671484955 1144907174 532089323".to_string(),
        "1414132335 1960778188 125717021".to_string(),
        "2631474761 2586973888 1058655511".to_string(),
        "1991131055 744338927 221864400".to_string(),
        "2212995455 192320896 28611061".to_string(),
        "192320896 2186552402 224875394".to_string(),
        "2241895588 966203327 169532208".to_string(),
        "1744764149 431490014 67442815".to_string(),
        "1812206964 2106058626 80493776".to_string(),
        "516655377 1135735535 9171639".to_string(),
        "1559412773 1775426812 185351376".to_string(),
        "2622156499 2577655626 9318262".to_string(),
        "1203574278 220931957 210558057".to_string(),
        "3690130272 4094120212 156346211".to_string(),
        "3946017132 3645629399 348950164".to_string(),
        "525827016 598680988 145657939".to_string(),
        "1892700740 1676996497 98430315".to_string(),
        "3846476483 3994579563 99540649".to_string(),
        "2577655626 4250466423 44500873".to_string(),
        "1539849356 2086495209 19563417".to_string(),
        "2241606516 598391916 289072".to_string(),
        "417196290 498932829 99459087".to_string(),
        "humidity-to-location map:".to_string(),
        "547577859 2546258172 54451455".to_string(),
        "2564186976 3913248498 28610653".to_string(),
        "2460249359 129990669 103937617".to_string(),
        "257798579 3257354132 21143365".to_string(),
        "511274864 3365252234 24536388".to_string(),
        "412475023 3389788622 98799841".to_string(),
        "2843712442 3615348771 251219053".to_string(),
        "0 2984989380 24111266".to_string(),
        "1074541266 4051128852 126947592".to_string(),
        "3109497668 265707418 9056683".to_string(),
        "3268495430 1450483293 18654108".to_string(),
        "1298820860 954974424 392849235".to_string(),
        "1691670095 1469137401 93027519".to_string(),
        "3886041222 2131196811 39611681".to_string(),
        "2797706800 1347823659 46005642".to_string(),
        "3767841776 233928286 19835810".to_string(),
        "743957513 253764096 11943322".to_string(),
        "4068806743 3941859151 109269701".to_string(),
        "2754107115 1910801576 16288912".to_string(),
        "1223331059 2244121482 75489801".to_string(),
        "3118554351 1393829301 56653992".to_string(),
        "3094931495 3009100646 14566173".to_string(),
        "3991994741 893524279 61450145".to_string(),
        "692486724 2192650693 51470789".to_string(),
        "1008564686 2952439802 32549578".to_string(),
        "535811252 3603582164 11766607".to_string(),
        "1784697614 2698363640 44335967".to_string(),
        "755900835 2353038285 193219887".to_string(),
        "278941944 1777268497 133533079".to_string(),
        "3925652903 3488588463 66341838".to_string(),
        "3558101581 2742699607 209740195".to_string(),
        "949120722 3305808270 59443964".to_string(),
        "2624116446 0 129990669".to_string(),
        "1939852817 274764101 520396542".to_string(),
        "3175208343 2037909724 93287087".to_string(),
        "3287149538 2600709627 97654013".to_string(),
        "650681177 1562164920 41805547".to_string(),
        "3787677586 795160643 98363636".to_string(),
        "1829033581 1927090488 110819236".to_string(),
        "4053444886 3897886641 15361857".to_string(),
        "1201488858 2170808492 21842201".to_string(),
        "3384803551 1603970467 173298030".to_string(),
        "2770396027 3278497497 27310773".to_string(),
        "1041114264 2319611283 33427002".to_string(),
        "602029314 3554930301 48651863".to_string(),
        "2592797629 3866567824 31318817".to_string(),
        "24111266 3023666819 233687313".to_string(),
    ]
}

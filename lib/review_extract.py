import csv

def trycast(x):
    try:
        return float(x)
    except:
        try:
            return int(x)
        except:
            return x


def count_cat(category,review):
    n = 0
    for word in category:
        n = n + review.count(word)
    return(n)

cols = ['product_productid', 'review_userid', 'review_helpfulness', 
        'review_score','review_time','act_adv','aac','animation','anime',
        'box','classics','comedy','coc','drama','edu','ex','faith','fantasy',
        'foreign','gay','holiday','horror','indie','family','war','music',
        'thrill','romance','sci_fi','special','sports','westerns']

# Category key words collection
act_adv = ['action','adventur','risk','explosi','fight','daring','dare','escap','hero','blood','brother','duty','honor','violence','warrior','spy','mission','gun','gadget','danger','stunt','alert','plan','dash','bustle','power','treasure','map','fear','island','journey','experience','feat','venture','deed','quest','win','mishap','accomplish','maneuver','effort','hazard','accident','enterprise','undertaking','voyage','expedition','experiment','speculat','wager']
aac = ['african','american','cinema','black','pioneer','divers','bet','communit','hero','naacp','race','africa','discriminat','reggae','hip­hop','histori','preserv','stereotype','slave','segregat','negro','dark','raci','ghetto','color']
animation = ['anima','cartoon','paint','illusion','figurine','computer­generated','figure','puppet','pixel','creative','disney','pixar','funny','enjoy']
anime = ['anime','japan','cartoon','ghibli','studio','akira','fan','manga','artist','graphic']
box = ['box','set','compilation','books','recording','film','package','anthology','essential','never­before','discography','season','complete','series','popular','commemorat','collect','pack']
classics = ['classic','all','time','old','film','memorabl','nostalgi','quote','cultur','communiti','distinguish','unique','transcend','quality','recogni','break','rewatch','re­watch','favorite','talent','human','timeless']
comedy = ['comedy','funny','comic','laugh','satir','humor','sketch','fancy','excite','entertain','parody','mock','lightheart','pun','amuse','stand­up','satire','screwball','joke','improvise','farce','sitcom','camp','fun','hilar','merry','jest','joke','gag','wit']
doc = ['document','biograph','histori','real­world','journal','true','narrat','literary','docudrama','education','nonfiction','reality','fact','opinion','fact','century','politic','personal','expert','memoir','inform','ancient']
drama = ['drama','noir','crime','suspens','noir','crime','drama','serious','cynic','heavy','investigat','dark','melo','erotic','goth','gang','legal','corrupt','case','abominat','malfeasance','misdeed','breach','felony','law','scandal','transgress','violat','wrong','delinq','deprav','rage','wick','realist','theme','alcohol','abuse','drug','addict','emotion','hope','moral','dilemma','prejudice','intolera','poverty','divisi','phenomen']
edu = ['educat','inspir','youth','kids','school','book','read','learn','teens','team','message','tween','teach','docu','role model','issue','icon','boy','girl','important','fascinat']
ex = ['exercis','fitness','fit','muscle','tone','shape','thin','abs','rock­hard','physique','weight','lean','train','hard','workout','pump','inspir','body','build','gym','rat','at­home','iron','dance','sequence','cardio','aerobic','strength']
faith = ['faith','spiritual','religio','god','jesus','church','christ','jew','islam','muslim','buddhis','believe','command','noah','hindi','hindu','angel','life','apostle','pray','strength','devil','passion','dogmas']
fantasy = ['fantasy','magic','myth','supernatural','folk','exotic','world','wonder','escap','extraordinary','sword','sorcer','ring','nether','fairy­tale','legend','imagin','dream','hallucinat','mystic','power','superhuman','force','fly','dragon','bizarre','whim','prince','angel','gnome','dwarve','elf','elves','marvel']
foreign = ['foreign','language','international','country','non­english','dialogue','caption','europe','africa','america','asia','arabi','hebrew','french','itali','italy','aborigin','territor','japan','mayan','bollywood','spanish','palestin','israel','canne','mandarin','hindi','portug','bengal','russia','turk','canton','thai','gujarati','punjabi','german','korea','dutch','tamil','persia','urdu','polish','pashto','jin','wu','telugu','marathi','hausa','min nan','kannada','xiang']
gay = ['gay','lesbian','love','bisexual','transgend','pride','relationship','desire','anti­gay','homosexual','orthodox','intimate','lgbt','fabulous','sex','feeling','prostitute','com','out','closet','romanc']
holiday = ['holiday','season','santa','christmas','snow','rain','spring','summer','fall','halloween','easter','day','eve','hanukkah','carol','charity','reindeer','spirit','timeless','child','family','light','greeting','home','new year']
horror = ['horror','kill','scream','monster','torture','terror','demon','shark','unsettl','dread','fright','panic','alarm','fear','terrify','shock','captiv','macabre','supernatural','unknown','ghost','extraterrestrial','vampire','werewolve','gore','vicious','evil','witch','zombie','cannibal','psychopath','serial']
indie = ['indie','art','house','serious','independent','niche','unconventional','symbol','thought','dream','motivat','festival','specialty','arthouse','cinema','deviat','identity','issue']
family = ['kid','family','friendl','general','paint','young','illusion','age','magic','audience','appropriate','fairy','child','home','favorite','kid','baby','pleas','disney','cute','miracle','goofy','rated­g','happily']
war = ['milita','war','hero','blood','honor','operat','battle','bloodshed','combat','conflict','fight','hostil','strike','struggle','polic','army','martial','aggress','arm','civil','soldier','force','troop','aircraft','ally','armor','attack','bomb','brigade','cadet','captain','capture','cavalry','command','corps','crew','conquest','defeat','enlist','fleet','grenade','guerrilla','gun','headquarters','infantry','invade','machete','medal','missile','navy','offense','parachute','peace','platoon','pentagon','rank','recruit','veteran','tactic','sniper','salute']
music = ['music','video','concert','danc','production','stage','broadway','theater','song','show','choreo','sing','orchestra','sound','vocal','costume','number','rock','disco','classical','cappella','instrument']
thrill = ['myster','thriller','detect','evil','puzzle','police','cruel','suspens','secre','riddle','crypt','perplex','tease','whodunit','crim','twist','psycho','fascinat','mind','trap','accident','investig','thief','disappear','intense','disturb','horrify','kill','murder','truth','discover','tragedy']
romance = ['romanc','romant','lov','heart','triangle','passion','emotion','sex','relation','affection','date','marri','sentiment','friends','chick','cute','feel','match','interest','beaut','like','duel','boyfriend','girlfriend','husband','wife','dating','couple']
sci_fi = ['science','fiction','sci­fi','extraterrestrial','alien','space','robot','psycho','planet','technolog','extrasensory','perception','time','travel','futur','craft','cyborg','interstellar','universe','parallel','life']
special = ['special','interest','specific','hobby','unique']
sports = ['sport','team','football','baseball','hockey','soccer','coach','college','game','athlete','ESPN','quarterback','cheerlead','basketball','skating','NFL','NBA','rival','score','goal']
westerns = ['west','american','old','cowboy','revolve','rifle','horse','boot','native','bounty','hunter','outlaw','settler','town','spur','cavalry','ranch','sling','saloon','wild']


f = open('./moviestrial.csv', 'w')
w = csv.writer(f)
w.writerow(cols)

doc = {}
i=1
with open('./movies.txt', encoding="utf-8", errors="surrogateescape") as infile:
    for line in infile:
        line = line.strip()
        if line == "" and 'review_text' in doc:
            print(i)
            i = i + 1
            review=doc['review_summary'].lower()+' '+doc['review_text'].lower()
            act_adv_n = count_cat(act_adv,review)
            aac_n = count_cat(aac,review)
            animation_n = count_cat(animation,review)
            anime_n = count_cat(anime,review)
            box_n = count_cat(box,review)
            classics_n = count_cat(classics,review)
            comedy_n = count_cat(comedy,review)
            doc_n = count_cat(doc,review)
            drama_n = count_cat(drama,review)
            edu_n = count_cat(edu,review)
            ex_n = count_cat(ex,review)
            faith_n = count_cat(faith,review)
            fantasy_n = count_cat(fantasy,review)
            foreign_n = count_cat(foreign,review)
            gay_n = count_cat(gay,review)
            holiday_n = count_cat(holiday,review)
            horror_n = count_cat(horror,review)
            indie_n = count_cat(indie,review)
            family_n = count_cat(family,review)
            war_n = count_cat(war,review)
            music_n = count_cat(music,review)
            thrill_n = count_cat(thrill,review)
            romance_n = count_cat(romance,review)
            sci_fi_n = count_cat(sci_fi,review)
            special_n = count_cat(special,review)
            sports_n = count_cat(sports,review)
            westerns_n = count_cat(westerns,review)

            total = (act_adv_n+aac_n+animation_n+anime_n+box_n+classics_n+comedy_n+doc_n+drama_n+edu_n+ex_n+faith_n+fantasy_n+foreign_n+gay_n+holiday_n+horror_n+indie_n+family_n+war_n+music_n+thrill_n+romance_n+sci_fi_n+special_n+sports_n+westerns_n)
            
            if total == 0:
                doc['act_adv'] = 0
                doc['aac'] = 0
                doc['animation'] = 0
                doc['anime'] = 0
                doc['box'] = 0
                doc['classics'] = 0
                doc['comedy'] = 0
                doc['doc'] = 0
                doc['drama'] = 0
                doc['edu'] = 0
                doc['ex'] = 0
                doc['faith'] = 0
                doc['fantasy'] = 0
                doc['foreign'] = 0
                doc['gay'] = 0
                doc['holiday'] = 0
                doc['horror'] = 0
                doc['indie'] = 0
                doc['family'] = 0
                doc['war'] = 0
                doc['music'] = 0
                doc['thrill'] = 0
                doc['romance'] = 0
                doc['sci_fi'] = 0
                doc['special'] = 0
                doc['sports'] = 0
                doc['westerns'] = 0
            else:
                doc['act_adv'] = round(act_adv_n / total,4)
                doc['aac'] = round(aac_n / total,4)
                doc['animation'] = round(animation_n / total,4)
                doc['anime'] = round(anime_n / total,4)
                doc['box'] = round(box_n / total,4)
                doc['classics'] = round(classics_n / total,4)
                doc['comedy'] = round(comedy_n / total,4)
                doc['doc'] = round(doc_n / total,4)
                doc['drama'] = round(drama_n / total,4)
                doc['edu'] = round(edu_n / total,4)
                doc['ex'] = round(ex_n / total,4)
                doc['faith'] = round(faith_n / total,4)
                doc['fantasy'] = round(fantasy_n / total,4)
                doc['foreign'] = round(foreign_n / total,4)
                doc['gay'] = round(gay_n / total,4)
                doc['holiday'] = round(holiday_n / total,4)
                doc['horror'] = round(horror_n / total,4)
                doc['indie'] = round(indie_n / total,4)
                doc['family'] = round(family_n / total,4)
                doc['war'] = round(war_n / total,4)
                doc['music'] = round(music_n / total,4)
                doc['thrill'] = round(thrill_n / total,4)
                doc['romance'] = round(romance_n / total,4)
                doc['sci_fi'] = round(sci_fi_n / total,4)
                doc['special'] = round(special_n / total,4)
                doc['sports'] = round(sports_n / total,4)
                doc['westerns'] = round(westerns_n / total,4)
            
            w.writerow([doc.get(col) for col in cols])
            doc = {}
        else:
            idx = line.find(':')
            if idx != -1:
              key, value = tuple([line[:idx], line[idx+1:]])
              key = key.strip().replace("/", "_").lower()
              value = value.strip()
              if key != 'review_summary' and key != 'review_text':
                doc[key] = trycast(value)
              else:
                doc[key] = value
    f.close()
